---
layout: post
title:  "Log barrier function"
date:   2018-02-22
desc: "Gradient and Hessian for log-barrier methods"
keywords: "log barrier method optimization derivative hessian oracle"
categories: [HTML]
tags: [markov]
icon: icon-html
---

We are given an oracle access to a function value $$f(x)$$, its derivative $$\nabla f(x)$$ and the hessian $$\nabla^2 f(x)$$. Based on this provided values, we can easily find the value $$g(x) = - log f(x) $$, derivative $$\nabla g(x)$$ and hessian $$\nabla^2 g(x)$$.

First, we use the chain rule:
$$
\begin{gather*}
  \nabla^2 (-log(f(x))) = - \nabla ( \nabla log (f(x))) = \nabla \frac{-\nabla f(x)}{f(x)}
\end{gather*}
$$

Next, we use the quotient rule:
$$
\begin{gather*}
  \frac{-\nabla^2f(x) f(x) + \nabla f(x) \nabla f(x)^T}{f(x)^2} =
  \frac{-\nabla^2f(x)}{f(x)} + \frac{\nabla f(x)\ \nabla f(x)^T}{f(x)^2}
\end{gather*}
$$

$$
\begin{gather*}
\nabla g(x) = \frac{-\nabla f(x)}{f(x)}
\end{gather*}
$$

$$
\begin{gather*}
\nabla^2 g(x) = \frac{-\nabla^2f(x)}{f(x)} + \frac{\nabla f(x)\ \nabla f(x)^T}{f(x)^2}
\end{gather*}
$$