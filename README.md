After downloading this prototype, you need to install corresponding environments.

We recommend the pip-tools, by the command 

"python3 -m pip install pip-tools"

We have provided necessary dependencies in the file GamePlatform/requirement.txt. You should open your terminal and enter the folder GamePlatform, then use the command 

"pip-sync requirement.txt"

Now, you have installed all necessary environments.


Next, you can start to run our project. You need to open two terminals. In the first one, go to the path in the folder GameCollection/, then run the command 

"python3 manage.py runserver"

This is the command to start the backend server. Now you can open your browser and use the url localhost:8000 to enter the backend hello world. If you use the localhost:8000/admin, you will see the backend management page. The username is "root", and password is "123456789". Then, you can see all information that are stored in the back end.

Now we need to use the second terminal to open front end pages. Go to the path GameCollection/frontend/ and run the command 

"npm run serve"

Wait for a few moments, then open the browser with url localhost:8080. You can see the homepage of our front end page. As for the rest of our functions, you may refer to our product prototype file on wiki, which contains detailed instructions and pictures about functions of our product.
