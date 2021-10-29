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

The idea is that we are provided an undirected graph $$G=(V,E)$$ where $$V$$ represents vertices and $$E$$ edges. The problem is to find the probability transition matrix $$P$$ that minimizes the time until which we attain the equilibrium dirstribution for the Markov chain (which means that after a few jumps in the Markov chain, you don't know where the next jump could end, i.e. on which node). In other words (plainly), a Markov chain is a graph in which with pair of vertices we associate probability of transition from one vertex to another. In a typical case, the transition probabilities can be different between the same vertices, depending on which direction we jump, thus it is usually the case: $$P_{ij} \ne P_{ji}$$. However, in this problem we assume that the graph is undirected and the probabilities of jumps between all pairs of vertices are the same: $$P_{ij} = P_{ji}$$. We also allow self-loops, so you can jump out from a vertex and jump in to the same vertex in a transition, this is associated with the probability $$P_{ii}$$.

What are our assumptions? The Markov chain has $$n$$ vertices and we define the current state by $$X(t) \in {1,2,...,n}$$, where $$t$$ is a non-negative integer (you can think about it as a time step which can be much larger than n, as it expresses which node we were occuping at a given point in time). The probablities for each vertex sum up to $$1$$ (you add all probabilities associated with edges connected to the given vertex). More formally:

This is how we define the transition probability matrix $$P$$:
$$
P_{ij} = \text{probability} (X(t+1) = i | X(t) = j), \ i,j = 1,...,n
$$

As all probabilities, they have to be at least 0 (we add another constraint that for a given vertex all the probabilites of jumps add up to 1 so it implies that for a given vertex, a sinlge probability has to be at most $$1$$, we don't add the it here that $$P_{ij} \le 1$$ so that our constraints are not redundant):
$$
P_{ij} \ge 0
$$

We can pose this formulation as an optimization problem:
$$ 
\min_{P \in S^n, t \in R} t \\
\forall_{i} \sum_j P_{ij} = 1 \ \ (P1 = 1) \\
\forall_{ij} P_{ij} \ge 0 \ \ (P \ge 0) \\
\forall_{ij \not\in E} P_{ij} = 0 \\
\forall_{ij} P_{ij} = P_{ji} \ \ (P^T = P) \\
-tI \preceq P - \frac{1}{n}11^T \preceq tI \\ 
$$

In short, given an undirected graph $$G(V,E)$$ on $$V = {1,...,n} $$ we want to construct a random walk $$X(t)$$ on the graph with symmetric transitions: $$P(X(t+1) = j | X(t) = i) = P_{ij} = P_{ji} $$ that minimizes the \textit{mixing time}, the time by which $$X(t)$$ is approximately uniform and independent of $$X(0)$$. Eigenvalues of matrix $$P: 1 = \lambda_1 \ge \lambda_2 \ge ... \ge \lambda_n \ge -1 $$. Hnce, 1 is eigen-vector of $$P$$ with eigenvalue $$1$$. 


The main outcome is that the smaller the second eigenvalue (closer to 0), the faster the mixing time (or we want to maximize $$-\lambda_n).

Claim: mixing time $$ \propto - \frac{1}{log(max(\lambda_2,-\lambda_n))}$$. We want to minimize $$max(\lambda_2, -\lambda_n)$$.


Fastests mixing Markov chain on a graph, credits: Prof. Stephen Boyd for his book on convex optimization, Prof. Nati Srebro (for the main introduction to the problem), Blake Woodworth (for explaining why we have to normalize eigenvectors), Angela Wu (for explaining how to isolate eigenvalues).