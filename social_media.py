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


def viewTimeline(platform):
    for each in platform:
        print(each)


def likePost(platform,PostIndex):
    if PostIndex >= len(platform) or PostIndex<0:
        return "Invalid post index"
    platform[PostIndex["likes"]]+=1
    return platform


def comment_Post(platform,PostIndex,comment):
    if PostIndex >= len(platform) or PostIndex<0:
        return "Invalid post index"
    platform[PostIndex]["comments"].append(comment)
    return platform


def startPlatform():
    print("welcome to the social media platform")
    platform=initializePlatform()
    while True:
        print("1 >> create new post")
        print("2 >> view platform Timeline")
        print("3 >> like post")
        print("4 >> comment post")
        print("5 >> exit")

        userChoice=int(input("please select your option: "))
        if userChoice==1:
            content=input("please add your post content: ")
            platform=createPost(platform,content)
        if userChoice==2:
            viewTimeline(platform)

        if userChoice==3:
            postIndex=int(input("please enter your PostIndex: "))
            platform=likePost(platform,postIndex)
        if userChoice==4:
            postIndex=int(input("please enter your PostIndex: "))
            comment=input("enter your comment: ")
            platform=comment_Post(platform,postIndex,comment)
        if userChoice==5:
            break
startPlatform()