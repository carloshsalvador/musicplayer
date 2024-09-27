# MUSIC PLAYER APP

Music player app is a project of web application for the DHBW/WDS's WebDesign Course carried out by [Prof. Jürgen Toth](https://github.com/juergen1976) during the semeter 2./2024. It is a course for students who are facing this topic for the first time. Thus, the project's main goal was the development of a music player. 

As an overview, this web application was developed based mainly on 2 frameworks, the [Django 5.1](https://www.djangoproject.com/) as backend and the [Vue.js](https://vuejs.org/) as frontend, and the data bank was [PostgreSQL](https://www.postgresql.org/) with music from [Spotify](https://open.spotify.com/). These elements are separted on [Dockercontainers](https://www.docker.com/).

Therefore, there are 3 ways to check the musicplayer app after cloning this project:

1. **development modus**

   This is quicker and easier way to see the app runing. After cloning, the steps are:

      1. install all dependecies based on **musicplayer/requirements.txt**
      2. create and set a new file **musicplayer/.env** based on the **musicplayer/.env_example**.
         1. set here the private [Spotify credencials](https://developer.spotify.com/).
         - the credencial for this project will be sent to the Professor.
      3. on terminal, at root **musicplayer/**, execute:
         1. ```python manage.py makemigrations```
         2. ```python manage.py migrate```
         3. ```python manage.py runserver```
      4. on browser, test the app at http://127.0.0.1:8000/

      - OBS: this modus is more simple! The data bank is the Django's default [SQLite](https://www.sqlite.org/), not [PostgreSQL](https://www.postgresql.org/) developed for the production modus (below) and the frontend is [Bootstrap](https://getbootstrap.com/).

2. **production modus** (not full implemented yet):

   1. install all dependecies based on **musicplayer/requirements.txt**
   2. create and set a new file **musicplayer/.env** based on the **musicplayer/.env_example**.
      1. at **musicplayer/.env**, set ```DEBUG=False```
   3. create and run the Dockercontainers based on the file **musicplayer/docker-compose.yml** using the terminal at root **musicplayer/** with the following commands:
      1. ```docker-compose build ```
      2. ```docker-compose up ```
   4. get in the container
      1. ```docker-compose exec web /bin/bash```
      2. ... and run the app from there:
         1. ```python manage.py makemigrations```
         2. ```python manage.py migrate```
         3. ```exit```
   5. on browser, test the app at  http://localhost
      - obs: due to the proxy revers with Ngnix, dont' need start Django server with ```python manage.py runserver```

3. **deployment modus** (not full implemented yet): as a [CaaS at Back4app](https://musicplayer-bw3lchlg.b4a.run/)


The devolepment of this project has tried to follow as much as possible the Adams Wiggins's [12 factors](https://12factor.net/), such as easy code's sharing, backing service and security. Some guidlines of this methodology make no much sense for this project, such as escalability and demands for team work because it is a individual project, but they were implemented anyway as best practice and learning by developing a web application for the frist time.

In this **README.md** the readers can find below the context, dependencies, architecture and infrasctructure and how the app was planed. However, **DETAILED_DOCUMENTATION.md** was developed as a recipt step-by-step for my memory of this project, with detailed description of the development sequence, *i.e.*, the explanation about the steps itself, but not the context.

---
---

# Before starting

Here I share my frist decisions I have faced before starting, my literature review and why I have decided for some alternatives among the high diverse possibilities of building a dynamic web-site such as a music palyer.

## The challenge

It is my frist app and many new topics needed to be decided and understand before strating.

The topics I have faced on the begining were:
   - two colossal topics: frontend and backend.
   - general stetps for any app: how to start and how to finish it?
   - diveristy of programming languages and frameworks.
   - architecture and infrastructure: api, server, data bank, load balance, caching, security, PaaS, CaaS etc.

## Frontend & Backend and the Framework

A music player app requires more elemente for the user experience ([UX](https://en.wikipedia.org/wiki/User_experience)) than a static one because they interacts much more dynamically rewriting the current web page with new data from the web server by searching music and different states like play and stop, instead of the more traditional method of loading entire new pages (or static web page) after any user's requires (~ user's clicks). The important key here was to understand the implications of the search engine optimization ([SEO](https://moz.com/learn/seo/what-is-seo)) to imporve the quality and quantity of website traffic and the choice of the modern types of aplications for projects like this, such as the Simple-Page-Aplication ([SAP](https://en.wikipedia.org/wiki/Single-page_application)) for faster transitions that make the website's feelings more like a native app. 

Therefore, the music app as a dynamic websites had be more efficent by server-side programming with frameworks that allow create dynamic websites and deliver customized information in response to HTTP requests ([Mozilla Devs](https://developer.mozilla.org/en-US/docs/Learn/Server-side)).

The framework choise was then the frist main topic to start drawing this project. The choice would be helpful for more foccus afterwards and to search specific information.

Follwing the professor's scripts, the most popular SAP's frameworks were:
- [React.js](https://react.dev/) (developed by Facebook)
- [Angular](https://angularjs.org/) (devolped by Google)
- [Vue.js](https://vuejs.org/)(open source)

In this project I opted for [Vue.js](https://vuejs.org/) for any special reason because there are not enought time to test all possibilities and compare the pros and cons. Moreover, they share some important feature that would important to me, such as the programing language (the three use javascript) and the free open source (Wikipedia: [Vue](https://en.wikipedia.org/wiki/Vue.js), [React](https://en.wikipedia.org/wiki/React_(JavaScript_library)), [Angular](https://en.wikipedia.org/wiki/AngularJS)). Maybe the most influence for **Vue.js** was the positiv comment by the professor by compering these 3 SPAs frameworks during the Web Design's lectures.

Nevertheless, they are frameworks for frontend, good for management the user interface (UI) and handle client-side demands. This project rather requirs a backend's framework for more robust development such object relational mapping ([ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)), data bank interaction and APIs, authentification and security ([examples](https://www.gyata.ai/python/orm-object-relational-mapping#advanced-orm-concepts-in-django)). The ORM of Django framework for example provides a high-level, Pythonic abstraction for database management, making it easier to work with databases ([Django ORM](https://www.lycore.com/blog/django-orm-a-guide-to-database-management-in-django/)).

For the backend framework the tendecy was to choose one based on programing language I had experience before such as python, javascript and R. The points I have considered for the framework's choice was then based on mainly the programe language that I had to use during the development phase:
- Python with [Django](https://www.djangoproject.com/) framework was the most interseting one to me due to my former experience, to the rich and powerfull libraries for web developement and to a great oportunity to use a second language in this project without great effort. About libraries and tools for example, [Joy](https://pythonistaplanet.com/advantages-of-django/) has pointed out 11 advantages such tools for security login, ORM and SEO and a interesting MVT:

<img src='https://cdn-0.pythonistaplanet.com/wp-content/uploads/2020/02/Django_MVT-1-683x1024.jpg?ezimgfmt=ng:webp/ngcb19' alt="Django's Model View Template (MVT) Architecture" title="Django's Model View Template (MVT) Architecture">

- Javascript with [Node.js](https://nodejs.org/en) framework could be an interesting option because I would use this language on the frontend anyway, but it is still the language I have less experience.
- [R](https://cran.r-project.org/) is very limited language for web programetion with poor libraries and it would'n be a good option for this project.
- [PHP](https://www.php.net/) was also discarted due to lack of experience. The visual similarity of sintax with javascript was not so much atractive to choose a third programing language in this beginner's project. It was also important, as a frist app, to keep simplicity and to concentrate on other parts of web development for more effective learning process and 3 programing languages increase the complexty.

Some tutorials was also considered to check the backend frameworks' aprouch for music apps and dynamics website before the final decision:
 - Node.js at [Geeks for Geeks](https://www.geeksforgeeks.org/music-player-app-with-next-js-and-api/)
 - Vue.js at [Geeks for Geeks](https://www.geeksforgeeks.org/build-a-music-app-using-vuejs/?ref=oin_asr7)
 - Django at [Geeks for Geeks](https://www.geeksforgeeks.org/music-player-using-django/)
 - Django at [Kolavole at DEV](https://dev.to/koladev/building-a-music-streaming-service-with-python-golang-and-react-from-system-design-to-coding-part-1-1c79)
 - Django at [W3Schools](https://www.w3schools.com/django/)
 - Django at [Bytexplain](https://bytexplain.com/how-to-build-a-music-sharing-app-using-django/)
- dynamic web-site with Django by [MMD](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
- a professional overview by Altynpara & Khodukina from [Cleaverroad](https://www.cleveroad.com/blog/how-to-create-a-music-streaming-app/)

The final decision was Django framework. With this decision I could move forward to the next step such as architecture, infrastructure and hands on the 12 factors in practice.

Some choice's consequence up to here was the complexity of file and scripts organization. It was expected much more complex with both [front and backend's framework](https://www.geeksforgeeks.org/music-player-using-django/) than one frontend framework only (*e.g.*, [Peseski](https://dev.to/psamim/micro-frontends-after-one-year-with-single-spa-1eoo)) and it was important step to understand were the project could reach on the end.

```
Expected file and scripts organization with frontend framework only (first figure) and with compbination of both frameworks (second figure):
(Font:see text)

├── apps
│   ├── root
│   │   ├── node_modules
│   │   ├── package.json
│   │   └── src
│   │       └── index.html
│   ├── feature-one (Angular)
│   │   ├── node_modules
│   │   └── package.json
│   └── feature-two (React)
│       ├── node_modules
│       └── package.json
└── scripts
    ├── build.sh
    ├── deploy.sh
    └── start.sh
```

<figure>
    <img src='https://media.geeksforgeeks.org/wp-content/uploads/20240201120202/file.png' alt='Example of file and scripts organization' title='Example of file and scripts organization'>
    <figcaption>Example of file and scripts organization with both front- and backend's framework<a href='https://www.geeksforgeeks.org/music-player-using-django/'> [Font]</a></figcaption>
</figure>

## 12 Factors in Practice and the infrascructure from PaaS to CaaS

The 12 factors methodology was the main general guide lines to follow in this project. However, there many ways to implement it. 

A Plattforme as a Service (PaaS) called [Heroku](https://www.heroku.com) is rather the most cited way to simulate the ideal web app production all in one ([Wikipedia](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), [Koyeb](https://www.koyeb.com/blog/herokus-free-tier-legacy-the-shoulders-we-stand-on-15-years-later)). Actually, the same author of the 12 factors, Adams Wiggens, was the team member of Heroku's creation [Wikipedia](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology) and this methodology is very educationl for the best practice on the production of web application ([Akita](https://www.akitaonrails.com/2022/01/10/akitando-112-subindo-aplicacoes-web-em-producao-aprendendo-heroku),[Koyeb](https://www.koyeb.com/blog/herokus-free-tier-legacy-the-shoulders-we-stand-on-15-years-later)).

By the other hand, there are critics for 12 Factors and Heroku ([Nginx](https://web.archive.org/web/20171222082423/https://www.nginx.com/blog/microservices-reference-architecture-nginx-twelve-factor-app/)). The critics concerns on the soluction mainly for [microservice](https://learn.microsoft.com/en-us/azure/architecture/microservices/), what is not the case of this project. Thus, I have kept the idea of simplicity of Heroku as the most useful tools to follow the 12 factor.

Nevertheless, Heroku has unfortunatly canceled its free service since 2022 ([Koyeb](https://www.koyeb.com/blog/herokus-free-tier-legacy-the-shoulders-we-stand-on-15-years-later)). Since then alternativ to Heroku was topic for many reviews and forums. Some selection for looking for a free alternative was:
- [Alisdair](https://medium.com/@alisdair_/top-heroku-alternatives-in-2024-6d6831cb6e08): updated (Jan 2024): 3 alternative and a Table of comparision.
- [Reddit forum](https://www.reddit.com/r/rails/comments/155mx7r/heroku_alternative/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button): last post: 1 year. Much more then 3 alternativ.
- [Medium posts](https://medium.com/dictcp/top-6-heroku-alternative-drop-in-replacement-in-2022-ff456fe050e4): updated (<10 months). 6 Alternatives.

Some Heroku's alternativ considered to check with more details were:
- [Back4app](https://www.back4app.com/)
- [Vercel](https://vercel.com/)
- Kubernets and Dockercontainers
- Complet cloud services such as Google App Engine, AWS and Microsoft's Azure.

The final decision was the **Back4app** as PaaS to host all application because it works very similar to Heroku linked with GitHub and has a interesting [documentation](https://blog.back4app.com/how-to-deploy-a-django-application/) to deploy Django's apps. The **Container as a Service (CaaS)** is the Back4app's plataforme version linked to GitHub and Dockercontainer, very similar to Heroku.

Vercel is a serverless platform with support for 35+ frontend frameworks and it would work better for static webpage, but not so well for this project of music player as a dynamic one. Moreover, it does not support running docker instances ([Verscel](https://vercel.com/guides/does-vercel-support-docker-deployments)).

The other remaining alternatives of Cloudservices demanded more advanced experience and costs. The Back4app seemed me more easier. Moreover, Back4app is independent and mix all possibilities. With other alternativas would be different and not so much attractive. In these cases, all element of infrastructure would be dependent on their tecnology sistems (*e.g.*, Google), *i.e.* the project would be restric to one service lossing libertiy and it was much advenced out of the scope of this project and requirments of this app.


# Staring the project

Here are the general steps. 

The detailed descriptions with codes and explanations are provided in another document [DETAILED_DOCUMENTATION.md](DETAILED_DOCUMENTATION.md).

## General steps

   1. Git and GitHub
   2. Django and PostSQL
   3. Spotify
   4. Docker
   5. Back4app
   6. Tailwind
   7. Vue.js

## File organization

After the steps above, the expected file organization is:

```
mymusicplayer/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── mymusicplayer/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── music/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── migrations/
│   │   └── templates/
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.js
├── docker-compose.yml
├── .gitignore
└── README.md
```


## Architecture and Infrasctructure

**File Configurations:**

   **.gitignore**: on the root directory (`musicplayer/`) to exclude non-versioned files such as `venv`, `*.pyc`, `*.log`, and `.env`.

   **.env**: stores all environment variables, *i.e.* they are not saved direct on the scripts. The env.var. are loaded when needed by runing the scripts with functions such as `os.getenv()`. [see the example above for **backend/settings.py**]. 

   **.env_example** is the reference file of .env without the private and security information. All users have to set their own .env. 
            
   **.dockerignore**: on the root directory under Docker control for Dockercompose or similar (*e.g.*, Heroku's Procfile). It defines files and directories that Docker should ignore. For security reasons, .env must be set here. This file is normally not considered on recomendations (*e.g.*, [Thompson, 2023](https://www.makeuseof.com/django-secret-key-generate-new/)), but the logic is the same for .gitignore.

   **requirements.txt**: originaly in the main directory because is the base for virutal environmental and others python projects, not only Django (for instance). Later, at the Docker's step, the file was copied and pasted to other folders such a Django, *i.e.* the backend directory (`musicplayer/backend/requirements.txt`), because the `Dockerfile` in such context should copy this file as follows:
      ```COPY requirements.txt requirements.txt``` (see Docker's step below)

   **nginx.conf**: file to control the load balance on production modus for proxy reverse. It is not full implemented yet, still at work. It also requires implementaion on ```docker-compose.yml``` (see comments there).

**Backend (Django)**

Here starts the longest backbone of this project, such additional architeture and security, such RESTful API.

   1. 1. **Project & Apps**

      The `startproject` is the frist obrigatory step followed by `startapp`. However, it is possible to set one or more apps for each project. For this decision it's important to consider the implications for the overall project structure.
      
      Each app handles its own classes, but in the Django framework, these are referred to as Models rather than standard Python classes. This is because each attribute of a model corresponds to a database field, and Django's ORM automatically manages the database schema and interactions when instances of the model are created. This system emphasizes the ORM's role in handling database operations, which is a key reason why Django uses the term "Model" to describe these classes. For example, the atributes of each classes/model can be instanciated with methods already implemented such as `models.AutoField()`, `models.CharField()` and `models.FileField()`.

      For a project like a music player, 2 separate apps are very interesting due to the clear different concerns:

         - ***API***: the **api** app handles the backend logic and provides endpoints for API interactions, making it easier to manage data and ensure modularity. Here the **Song** class is set with the attributes like id, title, category, artist, audio_file, and audio_image. 

         - ***Player***: the **music_player_app** focuses on the frontend user interface and user-specific functionalities such the user's registration on the app. Here the **CustomUser** class is set, but diffeentely of Song's class, it is already done by Django for general use and assocaited with other Django's funcionalties of security. **CustomUser** extends the **AbstractUser** class to customize user authentication and management. It inherits all the standard user attributes like username, email, and password, while also allowing for specific modifications such as custom group and permission handling. This approach leverages Django's built-in authentication system while providing flexibility for further customization.

      The approach of 2 apps enhances scalability, maintainability, and flexibility, allowing different teams to work on distinct parts of the project independently and making easier future expansion and testing; *i.e.* this aproach only fits to the most 12 Factors of Adam Wiggins.

   1. 2. **Data Fetching**

      An addional importante step here is the implemetation of RESTfull API arquiteture, it belongs also to the backend part.
      
      In general, Django's framework implement it automatically using Django REST Framework (DRF) by starting the project and adding apps, but sometimes it needs an extra implementation beyond the **models.py* described above. This is achieved by defining Django's models for the data structures, such as:

         - Song: creating corresponding serializers in the **api/serializers.py** file to convert these models to JSON format.

         - Views: **api/views.py** use DRF's generic views like ```ListCreateAPIView``` and ```RetrieveUpdateDestroyAPIView``` to handle RESTful requests, enabling CRUD operations.

         - URLs: these views are mapped to URLs in the project's **urls.py** file, providing a RESTful API that the frontend can interact with for data fetching and manipulation.

      In such scripts .py (serializers, views, urls) need to import the modules from the library ```djangorestframework``` (with Namespace ```rest_framework``` for import function in scripts' line):
         - `pip install djangorestframework` # CLI
         - `import rest_framework`           # on Python terminal or script

   1. 3. **Security**

      Security is another important topic implented on the backend step.

      Django can implement some security functions to protect the data bank, users and the web site itself.

      However, it require to set more specific environmental variables on the [**backend/settings.py**](https://docs.djangoproject.com/en/5.1/ref/settings/#security) as well on other no-Django's file (see bellow).
      
      The basic Django's security settings for this project was explainded direct on the file **backend/settings.py**. Here just some example:

         - `SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')` 

         - `SECURE_HSTS_SECONDS = 31536000`          # SecurityMiddleware will set this header on all HTTPS responses if non-zero integer value here (e.g. 31536000) [60*60*24*365 # 31536000 = 1 year in seconds]

         - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`   # SecurityMiddleware will add the includeSubDomains directive to the Strict-Transport-Security header if True [= assuming all subdomains are served exclusively using HTTPS], otherwise the site may still be vulnerable via an insecure connection to a subdomain.

**Spotify**:

After the basic backend was implemented, the app was create to have the [Web API](https://developer.spotify.com/documentation/web-api) and Django's files were changed to have the funcionalities, specially search and retrieve data from Spotify content such as tiles, artist, album or show.

**Containers and Orchestration**

Containers are the requirement to deploy at Back4app.com and to work similar to Heroku. For this reason this step come before the deployment at Back4app. The project has aimed at least 4 containers separted (Django, PostgreSQL, NGINX and Vue.js) as a simulation of independent servers for scalability and facility to work with different teams of developers. The best way to manage the independent containers was the Docker-compose service. It orchestrates multiple Dockerfiles with `docker-compose.yml` file at the root of this project. The Dockerfiles theirself are found at each respectiv subfolder.

**Deployment**

Similar to Spotify, Back4app requires also to create an app and then to have a DNS address. There is also a [tutorial](https://blog.back4app.com/how-to-deploy-a-django-application/) for Django's deployment. 

The service use the Dockerfiles to deploy the app at the Back4app's server. This proceed was carried out and the app had the [url](https://musicplayer-bw3lchlg.b4a.run/). After that, it was possible to set the comunication among the containers in Django project. However, this proceed was not fully complete due to the RAM limitation for free version accounts (256MB of RAM). I see possibilities to advance and to reduce the memory use, but there were no more time to finish this project in time. I gave up this proceed to respect the semester's deadline.

**Frontend**

The idea was frist deal with Tailwind and then Vue.js as recommend [elsewhere](https://tailgrids.com/blog/tailwind-css-integration-with-frameworks-and-tools). However, both has been not implement due to the the same reason as before, at deployment phase. 


# Conclusion Remarks

The project has finished sucessfully with a basic version in development modus and partially in advanced modus such as production and deployment. The developent modus version includs all elements to make the app viable. The API from Spotify was implemented at the backend with separated data banck (SQLite). The user can thus search and play music from Spotify. The registration is also working and the user can have their own play list. 

This modus only was very complex for beginner and I have learned a lot. The strategy of using two apps, api and music_player_app, corroborate well with several of the 12 Factors of Adam Wiggins for building modern, scalable software development principles:
   - Codebase: separate apps in the same Django project kept a single codebase with separte logical concerns and a clear tracking of different functionalities.
   - Dependencies: each app can clearly define and manage its own dependencies, making it easier to maintain and update required libraries.
   - Config: more apps allowed the principle of storing configuration in separte the environment.
   - Backing Services: the project's structure allowed integration and configuration of supporting services like databases, tailored to each app's specific needs.
   - Processes: each app could run as independent processes, facilitating better resource management and scaling.
   - Port Binding: each app could be configured to listen on specific ports, which is beneficial for separating concerns, especially for the api service.
   - Dev/Prod Parity: with modular approach, each app could be developed, tested, and deployed independently, ensuring consistency across development and production environments.

At the beginning, the sequencies of proceed and files structure was totally difficult to visualise. The sequences play an important role, like git first of all and containers before deployment.

When project use the tools such as git and containers it naturally increse the complexity and demands security awarness. The enviranmental variables could be easily exposed on the internet. The .env makes only sense if it is set on igoneres' files of Git as well as Docker (or similar such as Heroku). In such way the environmental variables were not on the script shared by creating image for containers as well as by controling version, considering that it is remote on plattaforms such as GitHub and GitLab. The .dockerignore is normally not considered on recomendations associate to .env as security proceeds (*e.g.*, [Thompson, 2023](https://www.makeuseof.com/django-secret-key-generate-new/)), but the logic is the same for .gitignore.

By the other hand, there was alternativ to ingore files such as setting the environmental variable direct on the server or controling then with instruction of Docker's CLI (e.g., E[NV](https://docs.docker.com/reference/dockerfile/#env)). However, .dockerignore file may be a more simple way to exclude files and directories from the build context ([Docker's doc](https://docs.docker.com/reference/dockerfile/#dockerignore-file)).

The backend only was a very big chanllange and took longtime to be implemented. Many key infornation were very poor documented (e.g., [secret key](https://docs.djangoproject.com/en/4.0/ref/utils/) oft reported by users [[Howard](https://code.djangoproject.com/ticket/32451) and [Sam](https://groups.google.com/g/django-developers/c/0nHdj8X_v6Y?pli=1)]) and took long time to find solutions even for simple demands. Every step took longer to advace. Thus, web frameworks are very helpful, but they work almost as a black box and require not straithforward oft adaptaions. 

For the DHBW demands and semester requirements, the project has been finished in the development modus. Nevertheless, the project goes one over the other semester as private project. I hope to reduce the memory demands to fit at Back4app free account and to work more intensive on frontend with Tailwind and Vue.js in the near future.