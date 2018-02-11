---
layout: post
title:  "Fastests mixing Markov chain on a graph"
date:   2018-02-09
desc: "convex optimization used to find fastest mixing Markov chain on a graph"
keywords: "markov chain"
categories: [HTML]
tags: [markov]
icon: icon-html
---

I talked to my friend who studied statistics about my course on convex optimization. He asked about a type of problems that we are trying to solve in the course. The first one that came to my mind was on fastest mixing Markov chain on a graph. I think that I there are many bits and pieces that are really required to fully understand the problem (depending on your background), but I will try to dissect the problem to the smallest possible parts to make each of them clear, and finally show you the whole picture of beautiful Markov chains combined with convex optimization.

The idea is that we are provided an undirected graph $$G=(V,E)$$ where $$V$$ represents vertices and $$E$$ edges. The problem is to find the probability transition matrix $$P$$ that minimizes the time until which we attain the equilibrium dirstribution for the Markov chain (which means that after a few jumps in the Markov chain, you don't know where the next jump could end, i.e. on which node). In other words (plainly), a Markov chain is a graph in which with pair of vertices we associate probability of transition from one vertex to another. In a typical case, the transition probabilities can be different between the same vertices, depending on which direction we jump, thus it is usually the case: $$P_{ij} \ne P_{ji}$$. However, in this problem we assume that the graph is undirected and the probabilities of jumps between all pairs of vertices is the same: $$P_{ij} = P_{ji}$$. We also allow self-loops, so you can jump out from a vertex and jump in to the same vertex in a transition, this is associated with the probability $$P_{ii}$$.

What are our assumptions? The Markov chain has $$n$$ vertices and we define the current state by $$X(t) \in {1,2,...,n}$$, where t a non-negative integer (you can think about it as a time step which can be much larger than n, as it expresses which node we were occuping at a given point in time). The probablities for each vertex sum up to 1 (you add all probabilities associated with edges connected to the given vertex). 

$$
P_{ij} = probability (X(t+1) = i | X(t) = j), \ i,j = 1,...,n
$$

$$
P_{ij} \ge 0
$$

Fastests mixing Markov chain on a graph"


Credits: Prof. Stephen Boyd for his book on convex optimization, Prof. Nati Srebro (for the main introduction to the problem), Blake Woodworth (for explaining why we have to normalize eigenvectors), Angela Wu (for explaining how to isolate eigenvalues).