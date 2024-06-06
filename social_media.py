def initializePlatform():
    Media=[]
    return Media
# print(initializePlatform())

def createPost(platform,content):
    post={}
    post["content"]=content
    post["likes"]=0
    post["comments"]=[]
    platform.append(post)
    return platform
# plat=initializePlatform()
# content="currently working on cspp"
# print(createPost(plat,content))

def viewTimeline(platform):
    for each in platform:
        print(each)
# platform=initializePlatform()
# content="currently working on cspp"
# platform=createPost(platform,content)
# content="solving given challenges"
# platform=createPost(platform,content)
# viewTimeline(platform)

def likePost(platform,PostIndex):
    if PostIndex >= len(platform):
        return "Invalid post index"
    post=platform[PostIndex]
    post["likes"]+=1
    return platform
# platform=initializePlatform()
# content="currently working on cspp"
# platform=createPost(platform,content)
# content="solving given challenges"
# platform=createPost(platform,content)
# print(likePost(platform,1))

def comment_Post(platform,PostIndex,comment):
    if PostIndex >= len(platform):
        return "Invalid post index"
    post=platform[PostIndex]
    post["comments"].append(comment)
    return platform
# platform=initializePlatform()
# content="currently working on cspp"
# platform=createPost(platform,content)
# content="solving given challenges"
# platform=createPost(platform,content)
# platform=likePost(platform,1)
# print(comment_Post(platform,1,"That's Great"))