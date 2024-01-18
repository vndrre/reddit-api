import praw
import credentials
import re
import matplotlib.pyplot as plt
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

reddit = praw.Reddit(client_id=credentials.client_id, 
                     client_secret=credentials.client_secret, 
                     user_agent='by u/andretak23')


subreddit = reddit.subreddit('Python')

words = []

for post in subreddit.hot(limit=100):
    for comment in post.comments:
        tokens = re.findall(r'\w+', comment.body.lower())
        filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
        words.extend(filtered_tokens)


word_counts = Counter(words)

top_words = word_counts.most_common(10)

frequencies = []

labels = []

total = sum([count for word, count in top_words])

for word, count in top_words:
    frequency = count / total
    frequencies.append(frequency)
    labels.append(word)


plt.pie(frequencies, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis('equal')
plt.title(f"Top 10 most used words in r/{subreddit}")
plt.savefig("pie_chart2")