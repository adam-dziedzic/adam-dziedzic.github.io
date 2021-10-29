---
layout: post
title:  "Notes on a paper: Multi-Scale Convolutional Neural Networks for Time Series Classification"
date:   2018-02-05
desc: "Personal comments on a paper."
categories: [HTML]
tags: [cnn time-series]
icon: icon-html
---

1. Category: a research prototype of harnessing CNNs to analyze time-series data.
2. Context: deep learning application for time-series. Related to papers on machine/deep learning and time-series analysis (data mining and management). The paper has a theoretical basis with comprehensive analysis on the UCR data set.
3. Correctness: it assumes that the classification of time-series can be done more efficiently than with other methods for the time-series data.
4. Contributions: new architecture of CNNs for the TSC (Time-Series Classification).
5. Clarity: the paper is well written in general - a little bit less attention was given to the experimental part in terms of description.

There are 3 types of classifiers for the time-series data:
1. **Distance based**: the simplest one use Euclidean distance or DTW (aligns two time-series with dynamic warping) to measure the distance between time-series with 1KNN classification.
2. **Feature based**: each time-series is characterized with a feature vector, SAX (Symbolic Aggregation approXimation) is a typical example where time-series is discretized (divided in windows) based on piece-wise mean value.
3. **Ensemble methods**: combine many different classifiers to achieve higher accuracy. The weight of distinct classifiers in an ensemble can be assigned based on the cross validation accuracy. The flat Collective Of Transform-based Ensemble (COTE) is an ensemble of 35 classifiers based on features from time and frequency domains.

The shaplets - signature subsequences of time-series. The shaplets are features that can be pre-determined a searched for in a new time-series.

A key reason for the success of CNNs is its ability to automatically learn complex feature representations using its convolutional layers. The paper shows that it is possible to automatically learn the feature representation from time series. It was shonw that the feature based classfier (LTS - Learning shaplets) can be seen as a special case of convolution. Is a simple way they show that the Euclidean distance used in LTS between a shapelet (a features subsequence that can appear in a time-series) and a new time-series that has to be classified can be expressed as a convolution with added Euclidean (L2) norm of the part of the new time-series and a constant L2 norm (arbitrarily chosen) for a filter (kernel). Let start from notation:

$$T = \{t_1,t_2,...,t_n\}$$ is a time series.
$$f = \{f_1,f_2,...,f_n\}$$ is a filter.
1-dimensional discrete convolution (the filter is flipped thus it is a standard convolution and not a cross-correlation):
$$
(T \cdot f)[i] = \sum_{j=1}^{m} f_{m+1-j}t_{i+j-1} 
$$

The expression of Euclidean dinstance between a shaplet and new-time series as a convolution:

$$
  ||T,f||_{2}[i] = \sum_{j=1}^m(t_{i+j-1} - f_{m+1-j})^2 \\
  = \sum_{j=1}^{m}t^2_}i+j-1} + \sum_{j=1}^{m}f^2_{m+1-j} - 2 \sum_{j=1}^{m}t_{i+j-1}f_{m+1-j} \\
  = \sum_{j=1}^{m} t^2_{i+j-1} + \sum_{j=1}^mf_j^2 - 2(T \cdot f)[i]
$$

$$\sum_{j=1}^{m} t^2_{i+j-1} $$ is a constant for each time-series (the L2 norm of the time-series).

$$ \sum_{j=1}^mf_j^2 $$ each filter is restricted to the same L2 norm.

A question is how we can use convolution to apply different distance measures? If we can do that, then we can leverage the GPUs and faster parallel computation.

The MCNN is a mutli-scale convolutional neural network with time-series as input and a class label as output. The main idea is to capture temporal patterns at different time-scales. The architecture is divided into 3 parts:
1. Transformation of the input time-series with 3 branches:
    - identity mapping (input is not changed)
    - down-sampling in time domain
    - spectral transformation in frequency domain
2. Local convolutions (applied to each branch separately) with max pooling
3. Full convolution with max pooling and Softmax

The number of parameters in the local convolutional layer was reduced by down-sampling the time-series instead of increasing the filter size.

The power of CNNs is in processing a huge amount of data. The analyzed dataset from UCR archive is relatively small so data augmentation by slicing is performed on the training and test data. The data is divided into windows (about 90\%) of the initial time-series, each window is set with the same label as the intial time-series and added as a new data point.

In terms of images, a simple two-cell/pixed filter can find edges in an image. A filter with two values for time-series $$ f=[1,-1] $$ gives a gradient between two neighboring points. MCNN is able to learn such filters. Filters are of different sizes and an example of 15 value filter is given - the max pooling applied after convolution with the filter gives a discriminative value that distinguishes between time-series belonging to 2 different classes. It's impressive that a single convolution filter can already achieve high accuracy to classify a dataset.

The grid-search was adopted for hyper-parameter tuning based on cross validation. The hyper-parameters in MCNN include the filter size, pooling factor, and batch size. The search space for the filter size is {0.05, 0.1, 0.2} which denotes the ratio of the filter length to the original time series length, the search space for the pooling factor is {2,3,5}, which denotes the number of outputs of max-pooling (the pooling is applied to 2,3,5 values from the time-series). Binomail and Wilcoxon signed rank tests are used to compare the models.

A multi-channel CNN has been proposed in another paper to deal with multivariate time-series.

MCNN outperforms a standard non-specialized CNN for time-series classification. However, it's still less accurate than COTE ensemble classifier. 

Link to the original paper: https://arxiv.org/pdf/1603.06995.pdf

