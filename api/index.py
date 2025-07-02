import feedparser
import os
import tweepy
import html

def handler(request, response):
    API_KEY = os.environ['TWITTER_API_KEY']
    API_SECRET = os.environ['TWITTER_API_SECRET']
    ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
    ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
    RSS_FEED = "https://www.bomdigma.com.br/feed"

    feed = feedparser.parse(RSS_FEED)
    latest_post = feed.entries[0]
    title = html.unescape(latest_post.title)
    summary = html.unescape(latest_post.summary)
    link = latest_post.link

    summary = summary[:200]
    invisible_char = "\u200B"

    first_tweet_text = f"📝 Novo Bom Digma:\n\n{title}\n\n{summary}...{invisible_char}"
    second_tweet_text = f"🔗 Leia a edição completa: {link}"

    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )

    first_tweet = client.create_tweet(text=first_tweet_text)
    client.create_tweet(
        text=second_tweet_text,
        in_reply_to_tweet_id=first_tweet.data["id"]
    )

    response.status_code = 200
    response.body = "Thread postada com sucesso!"

# Para Vercel Python, o nome da função precisa ser "handler"
