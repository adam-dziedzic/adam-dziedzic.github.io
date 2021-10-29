---
layout: post
title:  "Free adversarial training"
date:   2020-02-16
desc: "notes on a paper"
keywords: "deep learning machine learning adversarial training"
categories: [HTML]
tags: [deep learning machine learning adversarial training]
icon: icon-html
---

## Notes on papers: [fast adversarial training](https://papers.nips.cc/paper/8597-adversarial-training-for-free.pdf) 

## General idea
There were at least 2 papers at last NIPS 2019 that improved the performance of adversarial training. One of them is called 'Adversarial training for FREE!': https://arxiv.org/pdf/1904.12843.pdf The idea is simple and effective: reuse the gradients computed for parameters to generate adversarial examples.

Main points:

1. The same time for standard and adversarial training.

2. As effective as Mądry's adversarial training.

3. This method scales to ImageNet.

4. There are system optimizations that can tackle main performance issues in the adversarial research.

5. The FREE method provides smaller accuracy than standard adversarial training on ImageNet, even though the FREE method works better on CIFAR-10 and CIFAR-100.

Description:

In a typical adversarial training, in the internal maximization loop, we compute the gradients with respect to the input image many times (e.g. 7 by Mądry) for the PGD attack. In the external minimization loop, we compute the gradients once to update the parameters.

The FREE method proposes to reuse the gradients computed for training (to update model parameters) and also use them for generating the attack. To increase the number of updates for PGD, they use the same batch multiple times (replay it), each time computing gradients with respect to parameters and input. To maintain the same training time, they divide the number of epochs by the number of replay steps performed on a single batch. They replay each mini batch m times before switching to the next mini batch. This strategy provides multiple adversarial updates to each training image, thus providing strong/iterative adversarial examples. Finally, when a new mini-batch is formed, the perturbation generated on the previous mini batch is used to warm-start the perturbation for the new mini-batch.  

The 1st reviewer of this paper noticed that: "The idea of 'warm starting' each new minibatch with the perturbation values from the previous minibatch is not particularly founded, and no justification or ablation study is provided to analyze the impact of this choice. What happens when no warm start is used? How much does the final attack differ from the initialization value? Is this pushing the attack towards some notion of universal perturbation?" This observation was thouroughly exploited in the the paper on fast adversarial training: https://openreview.net/pdf?id=BJx040EFvH