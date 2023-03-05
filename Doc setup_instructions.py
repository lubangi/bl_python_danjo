#installing python python.org

# checking pyton version:

    #     python3 --version
    #     py3 -version
    #     python --version
    #     py --version
#check pip3 (python package index = package manager)
    # pip3 list
#upgrade pip3
    # pip3 list
    # pip3 --version

#extensipn needed:
    # python interpreter vscode
    # sqlite viewer

# activate the interpreter in vscode

    # shift+ cmd+p => open command palette
    # type : python Interpreter
    # choose select python interpreter
    # take the one you want ( recommanded)

#steps

    # creating a direcory
    # creating a virtual environement
    # activation
    # installing django
    # creating a project
    # migratting the db
    #lanch server
    # creating an app

# 1 creating the directory 

    #  mkdir en_test_django
    # cd mkdir en_test_django

# 2. creating a virtual EnvironmentError

    # windows

    # py  -m venv test_env 

    # macos

    # python3  -m venv test_env 
# 3. activation

    # mac 
        # source test_env/bin/activate
    # windows

        # .\env\Scripts\activate
#4 installing django
    #( windows, mac)
    # pip3 install django 
    # or
    # pip3 install django~=x.y.z

    # checking django version
    #     mac
    #     python3 -m django --version
    #     windows
    #     py -m django --version
# 5. creating the django project
      #( windows, mac)
#     django-admin startproject projectName .

#6 launch server
    # windows 
        # py3 manage.py runserver
    # macos
        # python3 manage.py runserver
  # to stop the server 
    # windows 
        # ctrl +c
    # macos
        # ctrl+c
# 6 .b database migration
    # navigate to the created project folder where manage.py is located
    # cd myproject
    # type :
    # python3 manage.py migrate  // this will create the database corresponding to the installed app in the settings.py file
#7 creating the app
    # open new terminal without stopping the running server
    # you must be in the root directory where is manage.py located
    # activate the virtualenvironment
    # then:
      # macos
        # python -m django startapp
      # windows
        # py -m django startapp myappclear





# notes

# Projects and applications

# Throughout this book, you will encounter the terms project and application over and over. In Django, a project is considered a Django installation with some settings. An application is a group of models, views, templates, and URLs. Applications interact with the framework to provide specific functional- ities and may be reused in various projects. You can think of a project as your website, which contains several applications, such as a blog, wiki, or forum, that can also be used by other Django projects.



















