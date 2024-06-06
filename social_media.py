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