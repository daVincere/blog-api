# mPharma Technical Task  
Build an application where a user can post an article, follow and unfollow the users in their platform  

## Milestones  
[x] Basic Django Setup [Static Folders, DB, App Structure, URL Mapping, Error Handling]
[x] Post App. [This takes care of the posting]
[x] Accounts App. [For Authentication, Login and SignIn]
[-] Follow/Unfollow Feature [Research and work]
[-] API-fy the whole app.  

## URLS   

1. `127.0.0.1:8000/posts/`  Post listing  
2. `127.0.0.1:8000/posts/create` Post creation  
3. `127.0.0.1:8000/posts/<slug>` Posts  
4. `localhost:8000/signup/` Signing Up  
5. `localhost:8000/login/` Logging In  
6. `localhost:8000/userlist/` List of Users  

### API [Partial]  
1. `localhost:8000/api/posts` Lists all the posts.  
2. `localhost:8000/api/post/<slud>` Gets you the post data  

	