# get top 10 comments from a list of posts
def get_top_10_comments(posts):
    comments = []
    for post in posts:
        if 'comments' in post:
            for comment in post['comments']:
                comments.append(comment)
    return sorted(comments, key=lambda x: x['likes'], reverse=True)[:10]