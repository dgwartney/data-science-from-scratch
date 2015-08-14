empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

joels_grade = grades["Joel"]
print(joels_grade)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)

daves = grades.get("dave", 'hello')
print(daves)

no_ones_grade = grades.get("No One")
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print(num_students)


tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}


tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print("user" in tweet_keys)
print("user" in tweet)
print("joelgrus" in tweet_values)

from loremipsum import get_paragraphs

words = []
for sentence in get_paragraphs(5):
    words.extend(sentence.split())

print(len(words))

def print_word_count(word_count):
    for i, j in word_counts.items():
        print(i, j)

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print_word_count(word_counts)
print("")

word_counts = {}
for word in words:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

print_word_count(word_counts)
print("")


word_counts = {}
for word in words:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

print_word_count(word_counts)
print("")


from collections import defaultdict
word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1

print_word_count(word_counts)
print("")


from collections import Counter
c = Counter([0, 1, 2, 0])

word_counts = Counter(words)
print_word_count(word_counts)
print("")

for word, count in word_counts.most_common(10):
    print(word, count)

