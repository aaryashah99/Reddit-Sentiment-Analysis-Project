from reddit_sentiment.fetcher import fetch_posts
from reddit_sentiment.analyzer import analyze_sentiment
from reddit_sentiment.plotter import plot_sentiment
import os

def main():
    print("Fetching Reddit posts...")
    df = fetch_posts()

    print("Analyzing sentiment...")
    df = analyze_sentiment(df)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/reddit_posts.csv", index=False)
    print("Saved data to data/reddit_posts.csv")

    print("Plotting sentiment...")
    plot_sentiment(df)

if __name__ == "__main__":
    main()
