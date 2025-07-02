import feedparser
import os
import tweepy
import html

# === 1. CONFIGURAÇÕES ===
API_KEY = os.environ['TWITTER_API_KEY']
API_SECRET = os.environ['TWITTER_API_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
RSS_FEED = "https://www.bomdigma.com.br/feed"

# === 2. LÊ O RSS ===
feed = feedparser.parse(RSS_FEED)
latest_post = feed.entries[0]
title = html.unescape(latest_post.title)
summary = html.unescape(latest_post.summary)
link = latest_post.link

summary = summary[:200]

# Adiciona caractere invisível pra evitar tweets duplicados
invisible_char = "\u200B"

first_tweet_text = f"📝 Novo Bom Digma:\n\n{title}\n\n{summary}...{invisible_char}"
second_tweet_text = f"🔗 Leia a edição completa: {link}"

# === 3. AUTENTICA E POSTA (THREAD) ===
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Publica o primeiro tweet
first_tweet = client.create_tweet(text=first_tweet_text)

# Responde com o link
client.create_tweet(
    text=second_tweet_text,
    in_reply_to_tweet_id=first_tweet.data["id"]
)

print("Thread postada com sucesso!")
