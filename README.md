# Reddit Sentiment Analysis

Analyze sentiment in Reddit headlines from r/news over the past 7 days using NLP and Python.  
This project collects Reddit post titles, computes sentiment scores, and visualizes daily sentiment trends.

## Project Overview

This project builds an end-to-end data pipeline that:
- Collects **top Reddit post titles** from the past 7 days using the Reddit API (via PRAW)
- Scores each title using **VADER Sentiment Analysis** (from NLTK)
- Visualizes **average daily sentiment** as a time series using `matplotlib` and `seaborn`

## Features

- Accurate post collection per calendar day using `subreddit.new()` and UNIX timestamps
- Sentiment scoring with VADER (compound polarity)
- Data saved in structured CSV format: `reddit_posts.csv`
- Matplotlib line plot showing daily sentiment trend
- Pipenv-based isolated virtual environment
- Secure credentials with `.env` and `python-dotenv`
- Modular, readable code structure (`fetcher.py`, `analyzer.py`, `plotter.py`)

## Technologies

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| Python 3.11     | Core scripting language          |
| PRAW            | Reddit API client                |
| Pandas          | Data manipulation & storage      |
| NLTK + VADER    | Sentiment analysis               |
| Matplotlib      | Visualization                    |
| Seaborn         | Chart styling                    |
| Pipenv          | Dependency & environment manager |
| dotenv          | Environment variable management  |


## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/reddit_sentiment_project.git
   cd reddit_sentiment_project

