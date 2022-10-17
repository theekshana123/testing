def tweettime(tweeterid):
    tweet_ids = [f'{tweeterid}']
    response = client.get_tweets(tweet_ids, tweet_fields=["created_at"])
    for tweet in response.data:
        p1 = str(tweet.created_at)
        year= int(p1[0:4])
        month=int(p1[5:7])
        date =int(p1[8:10])
        hour =int(p1[11:13])
        minute=int(p1[14:16])
        dateandtime=datetime.datetime(year,month,date,hour,minute)
        return dateandtime

def tweetlink(link):
    tid = re.findall('\d{19}', link)
    tweetid = tid[0]
    ftweet = tweettime(tweetid)
    return ftweet

def totfind(timedifsec):
    total =0
    if timedifsec>0 and timedifsec<=14400:
        print('you earned +0.25')
        total +=0.25
    elif timedifsec>14400 and timedifsec<=43200:
        print('you earned +0.20')
        total +=0.2
    elif timedifsec>43200 and timedifsec<=86400:
        print('you earned +0.2')
        total +=0.2
    elif timedifsec>86400:
        print('you are late')
    else:
        print('something went wrong')

    return total
