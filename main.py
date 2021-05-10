import requests
import datetime

refererurl = "https://replit.com/@EpicCodeWizard/ReplAPI-Module"
referername = "ReplAPIit"

def replit_user_avatar(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {image}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return queryjson['data']['user']['image']
  else:
    return None

def replit_user_cycle(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {karma}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return queryjson['data']['user']['karma']
  else:
    return None

def replit_user_name(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {fullName}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return queryjson['data']['user']['fullName']
  else:
    return None

def replit_user_bio(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {bio}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return queryjson['data']['user']['bio']
  else:
    return None

def replit_user_hacker(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {isHacker}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return queryjson['data']['user']['isHacker']
  else:
    return None

def replit_user_accountcreation(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {accountcreation}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return datetime.datetime.strptime(queryjson['data']['user']['accountcreation'], '%Y-%m-%dT%H:%M:%S.%fZ')
  else:
    return None

def replit_user_organization(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {organization{name}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return queryjson['data']['user']['organization']['name']
  else:
    return None

def replit_user_langs(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) {user: userByUsername(username: $username) {languages{id}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    listoflangs = []
    for x in queryjson['data']['user']['languages']:
      listoflangs.append(x['id'])
    return listoflangs
  else:
    return None

def replit_leaderboard():
  information = requests.post('https://replit.com/graphql', json={'query': 'query PostsFeedLeaders($count: Int, $since: KarmaSince) {leaderboard(count: $count, since: $since) {items{username karma}}}', 'variables': {'count': 10}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()['data']['leaderboard']['items']
  return information

def replit_post(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {posts(order: "hot", count: 1) {pageInfo {nextCursor} items {title body voteCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    try:
      return queryjson['data']['user']['posts']['items'][0]
    except:
      return None
  else:
    return None
  
def replit_posts(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {posts(order: "hot", count: 99999) {pageInfo {nextCursor} items {title body voteCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return {"posts": queryjson['data']['user']['posts']['items']}
  else:
    return None

def replit_posts_len(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {posts(order: "hot", count: 99999) {pageInfo {nextCursor} items {title body voteCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return len(queryjson['data']['user']['posts']['items'])
  else:
    return None
  
def replit_comment(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {comments(order: "hot", count: 1) {pageInfo {nextCursor} items {body voteCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    try:
      return queryjson['data']['user']['comments']['items'][0]
    except:
      return None
  else:
    return None
  
def replit_comments(name):
  comments = []
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {comments(order: "hot", count: 99999) {pageInfo {nextCursor} items {body voteCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    comments += queryjson['data']['user']['comments']['items']
    try:
      after = queryjson['data']['user']['comments']['pageInfo']['nextCursor']
      if after is None:
        raise ValueError("Random error to break.")
    except:
      return {"comments": comments}
    while True:
      queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!, $after: String) { user: userByUsername(username: $username) {comments(order: "hot", count: 99999, after: $after) {pageInfo {nextCursor} items {body voteCount}}}}', 'variables': {'username': name, 'after': after}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
      comments += queryjson['data']['user']['comments']['items']
      try:
        after = queryjson['data']['user']['comments']['pageInfo']['nextCursor']
        if after is None:
          raise ValueError("Random error to break.")
      except:
        return {"comments": comments}
  else:
    return None

def replit_comments_len(name):
  comments = []
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {comments(order: "hot", count: 99999) {pageInfo {nextCursor} items {body voteCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    comments += queryjson['data']['user']['comments']['items']
    try:
      after = queryjson['data']['user']['comments']['pageInfo']['nextCursor']
      if after is None:
        raise ValueError("Random error to break.")
    except:
      return len(comments)
    while True:
      queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!, $after: String) { user: userByUsername(username: $username) {comments(order: "hot", count: 99999, after: $after) {pageInfo {nextCursor} items {body voteCount}}}}', 'variables': {'username': name, 'after': after}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
      comments += queryjson['data']['user']['comments']['items']
      try:
        after = queryjson['data']['user']['comments']['pageInfo']['nextCursor']
        if after is None:
          raise ValueError("Random error to break.")
      except:
        return len(comments)
  else:
    return None

def replit_repl(name):
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {publicRepls(count: 1) {pageInfo {nextCursor} items {title description imageUrl runCount forkCount: publicForkCount}}}}', 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    try:
      return queryjson['data']['user']['publicRepls']['items'][0]
    except:
      return None
  else:
    return None

def replit_repls(name, replcount):
  if replcount <= 0:
    return None
  queryjson = requests.post('https://replit.com/graphql', json={'query': 'query userByUsername($username: String!) { user: userByUsername(username: $username) {publicRepls(count: replcount) {pageInfo {nextCursor} items {title description imageUrl runCount forkCount: publicForkCount}}}}'.replace("replcount", str(replcount)), 'variables': {'username': name}}, headers={'referer': refererurl,'X-Requested-With': referername}).json()
  if queryjson['data']['user'] is not None:
    return {"repls": queryjson['data']['user']['publicRepls']['items']}
  else:
    return None