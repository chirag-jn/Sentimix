from defaults import *

tweets = []

cur = {}

with open("Data/train_conll.txt", "r", encoding="utf-8") as f:
    for i in f:
        i = i.strip().lower()
        arr = i.split('\t')
        if len(arr)==3:
            tweets.append(cur)
            cur = {}
            cur['id'] = arr[1]
            if arr[2] == 'negative':
                cur['bias'] = -1
            elif arr[2] == 'positive':
                cur['bias'] = 1
            elif arr[2] == 'neutral':
                cur['bias'] = 0
            else:
                print('Error here')
                print(arr)
                break
        elif len(arr)==2:
            if 'tokens' in cur:
                cur['tokens'].append(arr)
            else:
                cur['tokens'] = [arr]
        # elif len(arr)==1:
            # tweets.append(cur)

print((tweets))

savePickle(tweets, 'tweets')