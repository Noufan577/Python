import random
import prettytable


class User:
    def __init__(self,username,userid):
        self.username=username
        self.id=userid
        self.followers=set()
        self.following=set()
    def following_count(self):
        return len(self.following)
    def follower_count(self):
        return len(self.followers)
    def followers_list(self):
        list=[]
        for i in self.followers:
            list.append(i.username)
        return list

    def following_list(self):
        list=[]
        for i in self.following:
            list.append(i.username)
        return list


    def follow(self,user2):
        if self!=user2 and user2 not in self.following:
            self.following.add(user2)
            user2.followers.add(self)

def generate_user():
    list="abcdefghijklmnopqrstuvwxyz"
    num=random.randint(1,6)
    return "".join(random.sample(list,num)).capitalize()
Users=[]
for i in range(1,101):
    user=generate_user()
    Users.append(User(user,i))
historyy=[]
for i in range(1000):
    x1=random.choice(Users)
    x2=random.choice(Users)
    if x1!=x2 and (x2 not in x1.following):
        x1.follow(x2)
        historyy.append(f"|{i} {x1.username} followed {x2.username}")

usernames = []
userids = []
followers = []
following = []

for i in Users:
    usernames.append(i.username)
    userids.append(i.id)
    followers.append(i.follower_count())
    following.append(i.following_count())

table=prettytable.PrettyTable()

table.add_column("Userid",userids)
table.add_column("usernames",usernames,"l")
table.add_column("Follower count",followers)
table.add_column("Floowing count",following)

def history():
    for i in historyy:
        print(i)
def opera4():
    x=input("Enter username ")
    while x not in usernames:
        print("User not found ")
        x=input("Enter username ")

        if x=="s":
            print("Thank You ")
            return False
    print(f"Following list of {x} is")
    for i in Users:
        if (i.username==x):
            x=i.following_list()
            i=1
            for k in x:

                print(f"{i} {k}")
                i+=1
    return True
def opera3():

    x=input("Enter username ")
    while x not in usernames:
        print("User not found ")
        x=input("Enter username ")
        if x=="s":
            print("Thank You ")
            return False


    print(f"Followers list of {x} is")
    for i in Users:
        if (i.username==x):
            x=i.followers_list()
            i=1
            for k in x:

                print(f"{i} {k}")
                i+=1
    return True





def main():
    end=True
    print("****************INSTAGRAM*************")
    
    while (end):
        inp=int(input('''Enter 
                    1 for list of users
                    2 for history
                    3 list of foloowers
                    4 list of followuing
                    5 stop             
                    enter       '''))
        if inp==1:
            print(table)
        elif inp==2:
            history()
        elif inp==4:

            end=opera4()
        elif inp==3:
            end=opera3()
        else :
            print("Thank you")
            end=False

main()

