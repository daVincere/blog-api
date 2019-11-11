# mPharma Technical Task  
Build an application where a user can post an article, follow and unfollow the users in their platform  

## Milestones  
[x] Basic Django Setup [Static Folders, DB, App Structure, URL Mapping, Error Handling]  
[x] Post App. [This takes care of the posting]  
[x] Accounts App. [For Authentication, Login and SignIn]  
[-] Follow/Unfollow Feature [Research and work]  
[-] API-fy the whole app.  


## Steps to start  
#### Cloning the Repository  
1. `git clone https://github.com/davincere/blog-api.git`  

#### Installing a virtual environment in the root directory of the project  
1. `pip install virtualenv v`  
2. `source v/bin/activate`  

#### Installing dependencies and running the project  
1. `pip install -r requirements.txt`  
2. `python manage.py collectstatic`  
3. Be sure to set up a postgreSQL database with the config listed in `settings.py`  
4. `python manage.py makemigrations`  
5. `python manage.py migrate`  
6. `python manage.py createsuperuser`  
	complete the steps to creating a user profile  
7. `python manage.py runserver`  


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

	