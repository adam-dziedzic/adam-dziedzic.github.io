---
layout: post
title:  "The Data Flow model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-order Data Processing"
date:   2018-04-26
desc: "notes on a paper"
keywords: "databaes streaming google sigmod 2015"
categories: [HTML]
tags: [databaes streaming google sigmod 2015]
icon: icon-html
---

# The Data Flow model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-order Data Processing

## These are my notes on the paper:

### Strong points:

1. The paper presents a new conceptual and principled model for stream processing. The main contribution is focus on the session windows - unbounded and unaligned windows with windowing based on a specific key. This was motivated by a use case where Google was receiving an influx of input events, that were just a single instances of specific users' actions. However, the semantic of a session was needed to reason about users' activities within a longer interaction with a system. The goal was achieved by the Window Merging operation with the following stages in the pipeline: Assign Windows, Drop Timestamps (preserve only the window spans), Group by key (e.g. user_id), Merge Windows and Group also by Windows (here is the case where we create single sessions for the users), Expand to Elements.
2. An important conceptual contribution is about the adaptability over time - we simply know that the watermarks are only logical and can be either incorrect (as lagging events from the past are coming later than expected) or simply too slow for the processing needs. Simply, the watermark is a global progress metric it can be held back for the entire pipeline by a single slow datum. The percentage of a watermark is a good trade-off. Processing majority of the data quickly is much more useful than processing 100% of the data more slowly - thus introducing percentile watermark triggers in the model. Moreover, having regularly updated, partial views on the data is much more valuable than waiting until mostly complete views are ready once the watermark passed the end of the session.
3. Clear distinction between the event time (as recorded by the source of the event) and the processing time (as recording in the processing system of the event).
4. The system has to be flexible and adjust to users' need in terms of: cost, processing time (latency) and correctness.
5. The use quite refined language with phrases such as: "a similar dance occurs for the values 3, 8, and 1, ..." (page 1801, last paragraph before Section 3).
6. They postulate the setup with a single implementation written in a unified model that could run in streaming and batch mode. In their case, the core windowing and triggering code is quite general, and a significant portion of it is shared across batch and stream implementations.

### Weak points:
1. We do not get sufficient information about the engineering of systems that follow the Data Flow model (this paper was published in the industrial track).

## More comments that are not arranged in a specific order:

1. The system became an Apache Beam project: https://beam.apache.org/

2. Paradigms:
   1. Unified:  Use a single programming model for both batch and streaming use cases.
   2. Portable: Execute pipelines on multiple execution environments.
   3. Extensible: Write and share new SDKs, IO connectors, and transformation libraries.

3. This interface can sit on top of different data sources (an ambitious approach).

4. Interesting bits of information in the paper:
   1. 6 use cases that they had at Google that led them to the design.
   2. Iintroduction: an amazing job of constructing the arguments.

5. When you write a paper for a conference you want to put in as many : no idiots statements - don't say explicitly about what the reviewers might be worried about. Bunch of statements like that in the paper. Non-technical stuff - lots of people work on the problem (streaming systems) - they go through the full stream of systems: Niagra, Esper (the 1st open-source streaming system), Storm, Pulsar, Spark Streaming, Flink, they bucket them and try to say what they think is lacking in the systems - one sentence what the group did right and wrong.

6. Important excert: "None of these shortcomings are intractable, and systems in active development will likely overcome them in due time. But we believe a major shortcoming of all the models and systems  mentioned  above  (with  exception  given  to  CEDR and Trill), is that they focus on input data (unbounded or otherwise)  as  something  which  will  at  some  point  become complete.  We believe this approach is fundamentally flawed when  the  realities  of  today’s  enormous,  highly  disordered datasets clash with the semantics and timeliness demanded by consumers.  We also believe that any approach that is to have broad practical value across such a diverse and varied set of use cases as those that exist today (not to mention those  lingering  on  the  horizon)  must  provide  simple,  but powerful, tools for balancing the amount of correctness, latency, and cost appropriate for the specific use case at hand. Lastly, we believe it is time to move beyond the prevailing mindset of an execution engine dictating system semantics;
properly designed and built batch, micro-batch, and streaming systems can all provide equal levels of correctness, and all three see widespread use in unbounded data processing today."

7. Logical data independence - this is mostly physical model independence. Query optimization. Abstraction - semantic of what is going to happen.

8. Leaky abstraction. The SQL language abstracts away the procedural steps for querying a database, allowing one to merely define what one wants. But certain SQL queries are thousands of times slower than other logically equivalent queries. On an even higher level of abstraction, ORM systems, which isolate object-oriented code from the implementation of object persistence using a relational database, still force the programmer to think in terms of databases, tables, and native SQL queries as soon as performance of ORM-generated queries becomes a concern.

9. That's not a really useful way to think about the unbounded data.

10. On a given database, think about a database at a given time. More data is continually coming in.

11. You can be more efficient, in reality, unbounded datasets have been processed using repeated runs of batch systems since their conception, and well-designed streaming systems are perfectly capable of processing bounded data. From the perspective of the model, the distinction of streaming or batch is largely irrelevant, and we thus reserve those terms exclusively for describing runtime execution engines.

12. Jujutsu (/dʒuːˈdʒuːtsuː/ joo-JOOT-soo; Japanese: 柔術, jūjutsu About this sound listen (help·info)), also known in the West as Ju-Jitsu or Jiu-Jitsu, is a Japanese martial art and a method of close combat for defeating an armed and armored opponent in which one uses either a short weapon or none.
In the paper: some Jujutsu moves - take the attack and claim this is exactly what we do.

13. Another interesting excerpt: "It is lastly worth noting that there is nothing magical about this model. Things which are computationally impractical in existing strongly-consistent batch, micro-batch, streaming, or Lambda Architecture systems remain so, with the inherent constraints of CPU, RAM, and disk left stead-fastly in place." Of course, there is nothing magical here!!!

14. In terms of form - no evaluation (industrial paper), incredibly well set up framework in the introduction - it's slightly cynical (believing that people are motivated by self-interest; distrustful of human sincerity or integrity).

15. Defensive arguments in the introduction. It's a very crowded space.

16. They try to come up with a comprehensive model. Can we modify different types of streaming, window, engine semantics - rather than to pick one and claim that this is how it should be. However, you have to give up some performance.

17. Understand patterns/anti-patterns for your own research.

18. MapReduce was rejected by SIGMOD and VLDB. Finally, it was accepted at the OSDI.

19. Meta-information: about stream processing - we have several requirements - semantics and performance. Can we separate - set them independently - the upper level - a semantic buffer - buffer for the tuples - whether it's a window. Lower part is an incremental view maintenance. This paper does not have an engine included, Apache Beam has no engine. The engine is closed-source. Given an engine and semantic - engine fault? if not a semantic concept supported. How can you build a better system? Paraphrase: can you really decouple the semantics from the performance with the engine. Non-stream query.

20. Beam can sit on top of Spark streaming. Spark streaming is built on top of Spark and RDDs.

21. If Beam become the most popular streaming interface - the typical things that people do with it.

22. It's also about missing data.

23. Incorporate semantic into the underlying engine.

24. The narrow waist architecture - abstraction layer, the semantic level on top of it.

25. User facing semantics: usually SQL.

26. Underlying Relational Algebra with a bunch of extensions.

27. Different notions - SQL - logical views - the notion of logical consequences.

28. Logical data independence - through views.

29. Between relational algebra and engine implementation is the physical independence.

30. Views hide the underlying database schema.

31. Plug in a new engine - it should support the relational algebra ++.

32. When the relational model was proposed. Conventional wisdom - a baeutiful academic exercise - the great debate - very early SIGMOD - relational people - and people who did an ad-hoc stuff. Ingres and system R - we think that it's a right model. The first implementation of the relational algebra. Some parallels with this and programming language folks. In the initial days - high level languages - you need to write hand tuned assembly - none really does it. With the PL folks and the idea of a high level language. The underlying architecture did not change that much. Problem - most architecture people would disagree with that. The idea of RDD is very different from the traditional tables in databases. Column store is overhaul from the row-store. Look at a query and figure out an optimal course of action. In a long run, abstraction wins out. The hard coded solution breaks. IRS crushes on the tax day - they were running on the 30 old system. Burning platform - it's gonna run and burning. Looking at these figure. You are in favor of BigDAWG - there is some reality to it. BEAM is a one-size fits all solution.

33. Multi-core came up - leaky abstraction open MP - parallelize - cache conscious algorithms - you should not worry about the stuff. You have to have a decent system and big market share so that everybody will follow you.

34. Spark - solve 80% of streaming problems that people have. It's one of the constant struggles in systems - where do you draw the abstraction. Architecture - at some point, the underlying system is too complicated - the abstraction is too big.

35. Programmers don't kmow enough to provide setting to the machine - instead specify to the requirements of the system. There is gonna be some problem with the cache conscious problem.

36. Which abstraction catch on - where do you draw them? Ingres QUEL language much better than SQL.

## Technical stuff:

1. Fundamental thing on which their system is based is the notion of windows - unbounded stream of data and you need to process it - you have to delineate the blocks of data. Jennifer Widom - http://ilpubs.stanford.edu:8090/758/

2. CQL (2003), a Continuous Query Language, is supported by the STREAM prototype Data Stream Management System at Stanford. CQL is an expressive SQL-based declarative language for registering continuous queries against streams and updatable relations. We begin by presenting an abstract semantics that relies only on ``black box'' mappings among streams and relations. From these mappings we define a precise and general interpretation for continuous queries. CQL is an instantiation of our abstract semantics using SQL to map from relations to relations, window specifications derived from SQL-99 to map from streams to relations, and three new operators to map from relations to streams. Most of the CQL language is operational in the STREAM system. We present the structure of CQL's query execution plans as well as details of the most important components: operators, inter-operator queues, synopses, and sharing of components among multiple operators and queries. Examples throughout the paper are drawn from the Linear Road benchmark recently proposed for Data Stream Management Systems. We also curate a public repository of data stream applications that includes a wide variety of queries expressed in CQL.

3. Windowing:
   1. fixed window
   2. sliding window - each window defines a relation - run SQL on the separated relation -
   3. extensible window - gunning tally of the window - at some
   4. session window

4. The window parameters:
   1. time domain: event and processing time
   2. a) accumulating vs. b) discard vs. c) accumulating and retracting - what do you do for the new windows in terms of the past data

4. More details: 
   1. Accumulate - add to my previous value.
   2. Discard - run the relational algebra - I get a new answer and discard the old one.
   3. Accumulate and retract - ignore the previous value and treat the new value as the source of the truth.

5. Processing time - these two times are relevant - skew between them changes as the system runs.

6. Fundamental statement: you can never rely on a notion of completeness. Conceptually - you need to keep every window - every window anybody has asked for.

7. Retract - when you hit the end of the window - send an anti-result - do the - if a past was 7, and new version is 8, then first send -7 and then they send 8.

8. Accumulating takes some additional space. The whole thing backs to the application question - clear answer - there is no magic - if data is not there, data is not there. Semantics - some hope of understanding - at any time stuff can show up.

9. Watermarks - everything up to this point in time already appeared. You can define your own watermark. Accumulating vs. discarding vs. retract and accumulate. Element based windows - account window - every 3 records are windowed - whatever order they come - just group them. The window can be a predicate. You can watch some stock ticker. One quote and the next quote. Unclear whether they support that in their case.

10. Session semantic - virtual stream over a specific key - per user.

11. Sessions are windows that capture some period of activity over a subset of the data, in this case per key. Typically they are defined by a timeout gap. Any events that occur within a span of time less than the timeout are grouped together as a session. Sessions are unaligned windows. For example, Window 2 applies to Key 1 only, Window 3 to Key 2 only, and Windows 1 and 4 to Key 3 only.

12. From the first time I see the user - and the default activity window is 30 minutes, if nothing happens I close the session.

13. Watermark - the idea of repeat clause. Can combine the late data after the watermark. Some point at which I'm pretty sure/confident I saw close to 100% of the data. Problems, too fast - a lot of data show up after the watermark - exception handling. They might be too slow - one solution to the late data is that you wait - their fundamental assumption is that you never know. Stupid argument - too fast - it doesn't work very well.

14. The notion of watermark - adapt over time and percentile watermark triggers in the model.

15. Streaming used for real time recommendation.

16. Example section: Processing time (y axis), event time (x axis) - when things really happen, processing time lags event time. They show values instead of when the event happened. Ideal - processing time aligned with the event time. The skew between the ideal time and the processing time. Watermarks are used to trigger the operations on the windows. For the system - how your actual watermark is generated - aggressive enough! Trade-off between how exact you're and how you generate the results. Confidence - how much - the probability of more data showing up.

17. 6 different ways how we see the streaming system at Google. Big joins of the log tables - the answers were so wrong we couldn't trust it, sessioning thing, billing (fact that you had to deal with the old data), statistics collection (do not need the exact answer), recommendation engine does not have to be perfect, stock market example - based on the shape of the data.

18. Apache Beam ~ PL1 - include every language that somebody ever came up with.
