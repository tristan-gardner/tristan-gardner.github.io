
import os
import tweepy
import time

## Make sure the twitter account has less than twenty lists befor running this program

def userSearch(api,q,members, max_members, cutoff, list_id):
    z = 0
    for person in tweepy.Cursor(api.search_users, q).items():
        if len(members) >= max_members:
            #print("full2")
            return members
        id = person.id
        followers = person.followers_count
        if id not in members and id != 17967668 and person.lang == "en":
            if followers > cutoff:
                print(z, person.screen_name)
                z+=1
                api.add_list_member(list_id = list_id, id=id)
                members.add(id)

def generate():
    # setup
    # Consumer Key (API Key)
    cons_key = 'pNnQDzpuvtblJO1LCuR4Qm5SO'
    # Consumer Secret (API Secret)
    cons_secret = 'thKKhQzJG97oK8w5w4g9btOADMg6gIgfAnc70RO93X750CzcTf'
    # Access Token
    access_token = '17967668-61FOP0CFYZxyL6m9xYtJxZWIx0F5r0GlHFJ14xXUA'
    # Access Token Secret
    access_token_secret = '4Nekfkg9Z3yldXIuOHC9lAkV9AKOiCGFHZ987Teg55gU5'

    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Bot code below
    keyword = input('Enter search term: ')
    max_members = input('Enter Maximum number of members for the list: ')
    followers = input('Enter minimum number of followers required: ')
    q = keyword
    create = True # set to false to add to a list, true to create a new one
    screen_name = "upraise_pr"
    list_id = 0
    if create:
        l = api.create_list(q,"private",q)
        list_id = l.id
    max_members = int(max_members)
    cutoff =  int(followers) #only add to list if they have more than cutoff followers
    buzzwords = {"marketing", "cmo", "PR", "public", "relations", "ceo", "company", "press", "promotion", "content", "agency", "firm", "coverage"}

    members = set()
    i = 0
    z = 0
    while api.rate_limit_status()["resources"]["application"]["/application/rate_limit_status"]["limit"] > 1:
        try:
            for stat in tweepy.Cursor(api.search, q = q, result_type = "popular").items():
                if len(members) >= max_members:
                    #print(len(members))
                    #print(members)
                    #print("Full1")
                    return members
                id = stat.user.id
                followers = stat.user.followers_count
                if id not in members and id != 17967668 and stat.user.lang == "en":
                    if followers > cutoff:
                        #print(i, stat.user.screen_name)
                        i+=1
                        api.add_list_member(list_id = list_id, id=id)
                        members.add(id)
            #print("1 done")
            for person in tweepy.Cursor(api.search_users, q).items():
                if len(members) >= max_members:
                    #print("full2")
                    return members
                id = person.id
                followers = person.followers_count
                if id not in members and id != 17967668 and person.lang == "en":
                    if followers > cutoff:
                        #print(z, person.screen_name)
                        z+=1
                        api.add_list_member(list_id = list_id, id=id)
                        members.add(id)
            #userSearch(api, q, members, max_members,cutoff, z)

                    
            

        except tweepy.TweepError as e:
            if 'Failed to send request:' in e.reason:
                #print("Time out error caught.")
                flag = True
                time.sleep(15)
                continue

            
    return members

def userRelevant(user, hashtagKey, recurrence, pages):
    # setup
    # Consumer Key (API Key)
    cons_key = 'pNnQDzpuvtblJO1LCuR4Qm5SO'
    # Consumer Secret (API Secret)
    cons_secret = 'thKKhQzJG97oK8w5w4g9btOADMg6gIgfAnc70RO93X750CzcTf'
    # Access Token
    access_token = '17967668-61FOP0CFYZxyL6m9xYtJxZWIx0F5r0GlHFJ14xXUA'
    # Access Token Secret
    access_token_secret = '4Nekfkg9Z3yldXIuOHC9lAkV9AKOiCGFHZ987Teg55gU5'

    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    
    count = 0
    #print(statuses[0].entities.get("hashtags")[0]['text'])
    for i in range(pages):
        statuses = api.user_timeline(id = user, page = i)
        #print(i)
        for item in statuses:
            hashtags = item.entities.get("hashtags")
            text = item.text
            text = text.split(" ")
            words = []
            for hashtag in hashtags:
                word = hashtag['text']
                if word.lower() in hashtagKey:
                    count += 1
                    if count == recurrence:
                        return True

            for word in text:
                if word in hashtagKey:
                    count+=1
                    if count == recurrence:
                        return True
    return False            
        

def generateSpecific():
    # setup
    # Consumer Key (API Key)
    cons_key = 'pNnQDzpuvtblJO1LCuR4Qm5SO'
    # Consumer Secret (API Secret)
    cons_secret = 'thKKhQzJG97oK8w5w4g9btOADMg6gIgfAnc70RO93X750CzcTf'
    # Access Token
    access_token = '17967668-61FOP0CFYZxyL6m9xYtJxZWIx0F5r0GlHFJ14xXUA'
    # Access Token Secret
    access_token_secret = '4Nekfkg9Z3yldXIuOHC9lAkV9AKOiCGFHZ987Teg55gU5'

    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Bot code below
    keyword = input('Enter search term: ')
    max_members = input('Enter Maximum number of members for the list: ')
    followers = input('Enter minimum number of followers required: ')
    hashtag = input('Enter hashtags seperated by a space: ')
    tweetSets = input('Enter number of tweets to scan through (1 = 20 tweet, 2 = 40...): ')
    recurrence = input('enter number of times hashtags must be present in recent tweets: ')
    q = keyword
    terms_list = hashtag.split(" ")
    term = set()
    for word in terms_list:
        term.add(word.lower())
    recurrence = int(recurrence)
    pages = int(tweetSets)
    max_members = int(max_members)
    create = True

    screen_name = "upraise_pr"
    if create:
        l = api.create_list(q,"private",q)
        list_id = l.id

    cutoff = int(followers) #only add to list if they have more than cutoff followers

    members = set()
    i = 0
    z = 0
    while api.rate_limit_status()["resources"]["application"]["/application/rate_limit_status"]["limit"] > 10:
        try:
            for stat in tweepy.Cursor(api.search, q = q, result_type = "popular").items():
                if len(members) >= max_members:
                    #print("Full1")
                    return members
                id = stat.user.id
                followers = stat.user.followers_count
                if id not in members and id != 17967668 and stat.user.lang == "en":
                    if followers > cutoff and userRelevant(id, term, recurrence,pages):
                        #print(i, stat.user.screen_name)
                        i+=1
                        api.add_list_member(list_id = list_id, id=id)
                        members.add(id)
            for person in tweepy.Cursor(api.search_users, q).items():
                if len(members) >= max_members:
                    return members
                id = person.id
                followers = person.followers_count
                if not id in members and followers > cutoff and id != 17967668 and userRelevant(id, term, recurrence,pages) and person.lang == "en":
                    api.add_list_member(list_id = list_id, id=id)
                    #print(z, person.screen_name)
                    z+=1
                    members.add(id)            


        except tweepy.TweepError as e:
            if 'Failed to send request:' in e.reason:
                #print("Time out error caught.")
                flag = True
                time.sleep(15)
                continue
            
    return members


def main():
    while True:
        choice = input('enter 1 for basic search or 2 for advanced search: ')
        if choice == '1':
            generate()
        else:
            generateSpecific()
        print()

if __name__ == "__main__":
    main()




