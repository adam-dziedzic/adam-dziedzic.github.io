---
layout: post
title: "Spectral representations for Convolutional Neural Networks"
date:  2018-06-25
desc: "Notes on a paper"
keywords: "deep learning machine learning frequency domain fft CNN convolution "
categories: [HTML]
tags: [deep learning machine learning frequency domain fft CNN convolution]
icon: icon-html
---

# Notes on a paper:
This paper presents a very interesting idea of replacing pooling layers such as max or avg ones with spectral pooling, where the input to the pooling layer is transformed to the frequency domain via FFT, then by the heuristic that the energy of the input in the frequency domain for natural signal or images follows the inverse power law where the most information is cumulated in the low frequencies and the noise is usually represented in the high frequencies, we truncated the signal by discarding the high frequency coefficients. Finally, the truncated signal is transformed back to the time/spatial domain via the inverse FFT. 

# Background:
A square matrix $$A=[A_1\;A_2\;\cdots\;A_n]$$ ($$A_i$$ for the ith column vector of $$A$$) is unitary if its inverse is equal to its conjugate transpose, i.e., $$A^{-1}=A^{*T}=A^{H}$$, where the superscript $$^H$$ denotes the Hermitian operation. In particular, if a unitary matrix is real $$A=A^*$$, then $$A^{-1}=A^T$$ and it is orthogonal. Both the column and row vectors ( $$A_i, i=1,\cdots,n$$) of a unitary or orthogonal matrix are orthogonal (perpendicular to each other) and normalized (of unit length), or orthonormal, i.e., their inner product satisfies: $$<A_i, A_j> = A_i^{H}A_j$$
$$ <A_i,A_j>=A_i^{*T} A_j=\delta_{i,j}=\left\{
\begin{array}{ll}
1 & \mbox{if } i=j  \\
0 & \mbox{otherwise}
\end{array}
\right
$$

These $$n$$ orthonormal vectors can be used as the basis vectors of the n-dimensional vector space.

source: [lectures on Fourier Transorm](http://fourier.eng.hmc.edu/e101/lectures/Image_Processing/node15.html)