# pyStock Recommender: Learning-To-Rank based Equity Screening

## Table of contents
1. [Introduction](#introduction)
2. [Installation & Reproducibility](#installation)
3. [Development roadmap](#development-roadmap)
4. [Jupyter Noteboks](#notebooks)
5. [Development](#development)
6. [Disclaimers](#disclaimers)

## Introduction

This repository analyses stock screening from passive replicas (namely ETFs) of Equity Indexes by means of learning-to-rank machine learning algorithms with the aim to improve cumulative returns maintaining a similar annual volatility. Other financial Risk and Performance Measures (**PMs**, for short) are planned to be benchmarked (compared).

On the other hand, _features construction and selection_ will be based on **PMs** (Financial Risk and Performance Measures).

Simple Trading Rules will be inferred from Rankers in order to outperform passive investments strategies.

These rankers are directly based on supervised Learning-To-Rank (**LTR** from now on) Algos.

**LTR** were mainly developed for other Deep and Machine Learning archetypical scopes such as web search engines.

The repo will be structured along four tiers:

1. **Dataset Construction**.

2. **LTR methods**.

3. **Out-Of-Sample (Test) Portfolio Performance**.

4. **Frontend**

5. **Documentation**

## Installation

## Learning-To-Rank training

## Development roadmap

We are working on expanding the coverage of the repo. Areas under active development are:

  * Data: 
  * Implementation of the following Learning-To-Rank Algos:
      * RankNET
      * LambdaMART      
      *
  * Backtesting And Conclusions: Empirical evidence supporting Equity Screening methodologies based on LTR Algos.
  * Frontend:
      * `streamlit`-based Financial KID (Key Information Dashboard)

## Notebooks

See [`pystock_recommenders/jupyter_notebooks`](https://github.com/falken1983/pystock_recommender/tree/main/jupyter_notebooks/)
for end-to-end data analysis and developments. It includes notebooks such as:

  *   [Index Components Web Scraping](https://colab.research.google.com/github/falken1983/pystock_recommender/blob/master/jupyter_notebooks/index_components_webscraper.ipynb)
  *   [Price Components Public Data Availability Analysis](https://colab.research.google.com/github/falken1983/pystock_recommender/blob/master/jupyter_notebooks/price_components_data_analysis.ipynb)
  *  [Price Components Data Generator (Free Subscription)](https://colab.research.google.com/github/falken1983/pystock_recommender/blob/master/jupyter_notebooks/price_components_free_data_generator.ipynb)
  *  [Price Components Data Generator (`nasdaqdatalink` Premium Subscription)]()
  
The above links will open Jupyter Notebooks in Colab.

### Development dependencies

This library has the following dependencies:

1.  nasdaq-data-link
2.  yfinance
3.  Python 3.9+
4.  Numpy version 1.21+

### Commonly used commands

Clone the GitHub repository:

```sh
git clone https://github.com/falken1983/pystock_recommender.git
```

After you run

```sh
cd pystock_recommender

```

There's a `environments.yml` but it is still under changes. (`conda env`)

## Disclaimers

This repo is under active development, and notebooks may change at any time.
