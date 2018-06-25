---
layout: post
title: "Parseval's identity"
date:  2018-06-24
desc: "Machine Learning theory"
keywords: "deep learning machine learning frequency domain fft CNN convolution linear algebra LA"
categories: [ML]
tags: [deep learning machine learning frequency domain fft CNN convolution linear algebra LA]
icon: icon-html
---

Geometrically, it is the Pythagorean theorem for inner-product spaces. In its special case for a single vector $$x$$ it can be written as:

$$ \sum_{n} |\prec x,e_n \succ|^2 = ||x||^2 $$

where

$$ \prec *,* \succ $$

represents an inner product and

$$ ||x||^{2} = \prec x, x \succ $$

This is directly analogous to the Pythagorean theorem, which asserts that the sum of the squares of the components of a vector in an orthonormal basis is equal to the squared length of the vector. Here, we project vector $$x$$ on each of the basis vectors $$e_i$$.

In more general form, the Parseval's identity is:

$$\prec u,v \succ = \sum_i \prec u,w_i \succ \prec w_i, v \succ $$

First, we prove that $$c_i = \prec u, w_i \succ $$.
The vectors $$w_i$$ for $$i=1,...,n$$ are the orthonormal basis for inner-product vector space V. Then for any $$ u \in V$$ there exists $$c_1,c_2, ..., c_n $$ such that $$ u = \sum_i c_i w_i $$. The coefficients $$c_i$$ are called Fourier coefficients. Let's prove that $$c_i = \prec v, w_i \succ $$ using the orthogonormality (orthogonal and normal) vectors $$w_i$$.

$$ \prec v, w_i \succ = \prec \sum_{i=1}^{n} c_i w_i, w_i \succ = \sum_{i=1}^{n} c_i \prec w_i, w_i \succ = c_i $$

$$ \prec w_i, w_j \succ = 1 \mbox{ if } i=j \mbox{; } 0, \mbox{ otherwise} $$

Now, we prove the general form of Parseval's identity:

$$ \prec u,v \succ = \prec \sum_{i=1}^{n} c_i w_i, v \succ = \sum_{i=1}^{n} c_i \prec w_i, v \succ = \sum_{i=1}^{n} \prec v, w_i \succ \prec w_i, v \succ $$

