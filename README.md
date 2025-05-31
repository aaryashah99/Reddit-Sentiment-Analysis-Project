# Reddit Sentiment Analysis Pipeline

A modular Python pipeline that scrapes Reddit posts, performs sentiment analysis, and visualizes the results. Built for automation, extensibility, and clear insights from real-time social data.

> NLP + Reddit API + Visualization = Insightful sentiment tracking

---

## Project Structure

| File/Folder         | Purpose                                               |
|---------------------|-------------------------------------------------------|
| `analyze.py`        | Main runner script to execute the entire pipeline     |
| `reddit_sentiment/` | Internal module with fetch, analysis, and plotting logic |
| `.env.example`      | Environment variable template                         |
| `.gitignore`        | Excludes `.env`, `__pycache__`, etc.                 |
| `Pipfile`           | Dependency and environment manager via `pipenv`       |

---

## Key Features

- Fetches Reddit posts using Reddit API (via `praw` or custom wrapper)
- Applies sentiment analysis (likely using `TextBlob`, `VADER`, or `transformers`)
- Saves cleaned data to CSV
- Visualizes sentiment trends over time
- Organized using modular Python components

---

