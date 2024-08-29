correct language text

.env_example

security variáveis de ambiente!.. só .env + .gitingore não adianta porque docker built copia .env, portanto tem que ter tb .dockerignore ...OPÇÃO 2: back4app tb tem opção de fornecer as variávies de ambeinte na hora de criar o deploy do app, como se estivesse configurando as variáveis de ambiente direto no servidor. Talvez seja ainda mais seguro pelo o que entendi, mas preferi não usar essa opção por enquanto, até mesmo para testar a segurança - Professor, tenta acessar as vars?!... desfio para Hacker?


css with vue... more than 15 options
https://medium.com/@emperorbrains/10-vue-js-ui-libraries-trends-in-2024-4ae6a9f653f5
https://wpshout.com/vue-ui-component-libraries/#gref
... see script professor.. Tailwind as responsive web
... Vue.js has SFC scope:
https://vuejs.org/api/sfc-css-features.html

.. começar pelo Tailwind e depois fazer o Vue!!
https://tailgrids.com/blog/tailwind-css-integration-with-frameworks-and-tools



# MUSIC PLAYER APP

Music player app is a project of Web Application for the DHBW/WDS's WebDesign Course (semester 2.2024) carried out by [Prof. Jürgen Toth](https://github.com/juergen1976). It is a course for students who are facing this topic for the first time. It is my first web app for example.

As an overview, this web application was developed using basically 2 frameworks, [Django](https://www.djangoproject.com/) as backend and [Vue.js](https://vuejs.org/) as frontend, and the music come from [Deezer](https://www.deezer.com/en/).

This project has tried to follow as much as possible the Adams Wiggins's [12 factors](https://12factor.net/), such as easy code's sharing, backing service and security. Some guidlines of this methodology make no much sense for this project, such as escalability and demands for team work because it is a individual project, but they were implemented as best practice and learning process.

---
---

# Before starting

Here you can find my frist decisions before starting, my literature review and why I decided for some alternatives among the high diverse possibilities of building a dynamic web-site such as a music palyer.

## The challenge

It is my frist app ever and many new topics need to decide and understand before strating.

The topics I have faced on the begining were:
 - general stetps for any app - how to start and how to finish it
 - two colossal topics: frontend and backend
 - programming languages and frameworks
 - architecture and infrastructure: api gateway, server, data bank, load balance, caching, security, PaaS, CaaS.

## Frontend & Backend and the Framework

A music player app requires more elemente for the user experience ([UX](https://en.wikipedia.org/wiki/User_experience)) because they interacts much more dynamically rewriting the current web page with new data from the web server by searching music and different states like play and stop, instead of the more traditional method of loading entire new pages (or static web page) after any user's requires (~ user's clicks). The important key here was then the search engine optimization ([SEO](https://moz.com/learn/seo/what-is-seo)) to imporve the quality and quantity of website traffic and the choice a modern type of aplication for this project, such as the Simple-Page-Aplication ([SAP](https://en.wikipedia.org/wiki/Single-page_application)) for faster transitions that make the website feel more like a native app. 

Therefore, the music app as a dynamic websites wourld more efficent by Server-side programming with frameworks that allow create dynamic websites and deliver customized information in response to HTTP requests ([Mozilla Devs](https://developer.mozilla.org/en-US/docs/Learn/Server-side)).

The framework choise was then a relevant topic to start drawing this project of music app. The choice would be helpful for more foccus afterwards by seraching information.

Follwing the professor's scripts, the most popular SAP's frameworks are:
- [React.js](https://react.dev/) (developed by Facebook)
- [Angular](https://angularjs.org/) (devolped by Google)
- [Vue.js](https://vuejs.org/)(open source)

In this project I opted for [Vue.js](https://vuejs.org/) for any special reason because there are not enought time to test all possibilities and compere the pros and cons, and all of then share some important feature for the choice, such as the programing language (all javascript) free open source (Wikipedia: [Vue](https://en.wikipedia.org/wiki/Vue.js), [React](https://en.wikipedia.org/wiki/React_(JavaScript_library)), [Angular](https://en.wikipedia.org/wiki/AngularJS)). Maybe the most influence for Vue was the positiv comment by the professor by compering these 3 SPA frameworks during the Web Design's lectures.

Nevertheless, they are frameworks for frontend, good for management the user interface (UI) and handle client-side demands. This project rather requirs a backend's framework for more robust development such object relational mapping ([ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)), data bank interaction and APIs, authentification and security ([examples](https://www.gyata.ai/python/orm-object-relational-mapping#advanced-orm-concepts-in-django)). The ORM of Django framework for example provides a high-level, Pythonic abstraction for database management, making it easier to work with databases ([Django ORM](https://www.lycore.com/blog/django-orm-a-guide-to-database-management-in-django/)).


For the backend framework the tendecy was to opt for one based on programing language I had experience before such as python, javascript and R. The points I have considered for the framework's choice was then based on mainly the programe language:
- Python with [Django](https://www.djangoproject.com/) framework was the most interseting one to me due to my former experience, to the rich and powerfull libraries for web developement and to a great oportunity to use a second language in this project without great effort. About libraries and tools for example, [Joy](https://pythonistaplanet.com/advantages-of-django/) has pointed out 11 advantages such tools for security login, ORM and SEO and a interesting MVT:

<img src='https://cdn-0.pythonistaplanet.com/wp-content/uploads/2020/02/Django_MVT-1-683x1024.jpg?ezimgfmt=ng:webp/ngcb19' alt="Django's Model View Template (MVT) Architecture" title="Django's Model View Template (MVT) Architecture">

- Javascript with [Node.js](https://nodejs.org/en) framework could be an interesting option because I would use this language on the frontend anyway, but it is still the language I have less experience.
- [R](https://cran.r-project.org/) is very limited language for web programetion with poor libraries and it would'n be a good option for this project.
- [PHP](https://www.php.net/) was also discarted due to lack of experience. The visual similarity of sintax with javascript was not so much atractive to choose a third programing language in this beginner's project. It was also important, as a frist app, to keep simplicity and to concentrate on other parts of web development for more effective learning process and 3 programing languages increase the complexty.

Some tutorials was also considered to check the frameworks' aprouch with music apps and dynamics website for final decision:
 - Node.js at [Geeks for Geeks](https://www.geeksforgeeks.org/music-player-app-with-next-js-and-api/)
 - Django at [Geeks for Geeks](https://www.geeksforgeeks.org/music-player-using-django/)
 - Django at [Kolavole at DEV](https://dev.to/koladev/building-a-music-streaming-service-with-python-golang-and-react-from-system-design-to-coding-part-1-1c79)
 - Django at [W3Schools](https://www.w3schools.com/django/)
 - Django at [Bytexplain](https://bytexplain.com/how-to-build-a-music-sharing-app-using-django/)
- dynamic web-site with Django by [MMD](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
- professional overview by Altynpara & Khodukina from [Cleaverroad](https://www.cleveroad.com/blog/how-to-create-a-music-streaming-app/)

The final decision was Django framework. With this decision I could jump to the next step such as architecture, infrastructure and hands on the 12 factors in practice.

Some choice's consequence up to here is the complexity of file and scripts organization. They are going to be much more complex with both [front and backend's framework](https://www.geeksforgeeks.org/music-player-using-django/) than one frontend framework only (*e.g.*, [Peseski](https://dev.to/psamim/micro-frontends-after-one-year-with-single-spa-1eoo)) and it was important step to understand were the project could reach on the end.

```
Example of file and scripts organization with both frontend framework only:
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
    <figcaption>Example of file and scripts organization with both front and backend's framework<a href='https://www.geeksforgeeks.org/music-player-using-django/'> [Font]</a></figcaption>
</figure>

## 12 Factors in Practice and the infrascructure from PaaS to CaaS

The 12 factors methodology was the main general guide lines to follow in this project. However, there many ways to implement it. 

A Plattforme as a Service (PaaS) called [Heroku](https://www.heroku.com) is rather the most cited way to simulate the ideal web app production all in one ([Wikipedia](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), [Koyeb](https://www.koyeb.com/blog/herokus-free-tier-legacy-the-shoulders-we-stand-on-15-years-later)). Actually, the same author of the 12 factors, Adams Wiggens, was the team member of Heroku's creation [Wikipedia](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology) and this methodology is very educationl for the best practice on the production of web application ([Akita](https://www.akitaonrails.com/2022/01/10/akitando-112-subindo-aplicacoes-web-em-producao-aprendendo-heroku),[Koyeb](https://www.koyeb.com/blog/herokus-free-tier-legacy-the-shoulders-we-stand-on-15-years-later)).

By the other hand, there are critics for 12 Factors and Heroku ([Nginx](https://web.archive.org/web/20171222082423/https://www.nginx.com/blog/microservices-reference-architecture-nginx-twelve-factor-app/)). The critics concerns on the soluciton more for [microservice](https://learn.microsoft.com/en-us/azure/architecture/microservices/) and it could be more complex for this project. Thus, I have still kept the idea of simplicity of Heroku as the most useful tools to follow the 12 factor.

Unfortunatly Heroku has canceled its free service since 2022 ([Koyeb](https://www.koyeb.com/blog/herokus-free-tier-legacy-the-shoulders-we-stand-on-15-years-later)). Since then alternativ to Heroku was topic for many reviews and forums. Some selection for looking for a free alternative is:
- [Alisdair](https://medium.com/@alisdair_/top-heroku-alternatives-in-2024-6d6831cb6e08): updated (Jan 2024). Offer 3 alternative and a Table of comparision.
- [Reddit forum](https://www.reddit.com/r/rails/comments/155mx7r/heroku_alternative/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button): last post: 1 year. Much more then 3 alternativ.
- [Medium posts](https://medium.com/dictcp/top-6-heroku-alternative-drop-in-replacement-in-2022-ff456fe050e4): updated (<10 months). 6 Alternatives.

Some Heroku's alternativ considered with more details for checking were:
- [Back4app](https://www.back4app.com/)
- [Vercel](https://vercel.com/)
- Kubernets and Dockercontainers
- Complet cloud services such as Google App Engine, AWS and Azure.

The final decision was the Back4app as PaaS to host all application because it works very similar to Heroku linked with GitHub and has [documentation](https://blog.back4app.com/how-to-deploy-a-django-application/) to deploy Django's app. **Container as a Service (CaaS)** is the Back4app's plataforme linked with GitHub and Dockercontainer. 

Vercel would work better for static webpage and as far as I could undestand it would not fit well for this project of music player as a dynamic one. The other alternatives of Cloudservices demands more advanced experience, costs and all element of infrastructure would be dependent on their tecnology sistem (*e.g.*, Google), *i.e.* the project would be restric to one service lossing libertiy.


# Staring the project

## General steps



## Architecture and Infrasctructure

1. **Backend (Django)**:
   - **Function**: Handles business logic and APIs.
   - **Container**: Docker container for the Django server.
   - **Framework**: Django REST Framework for creating RESTful APIs.

Here is very important strategic step! 
Here come the decision for 1 or more Django's app.
For a music player 2 separate apps are very interesting for a clear separation of concerns: 
1. the api app handles the backend logic and provides endpoints for API interactions, making it easier to manage data and ensure modularity.
2. the music_player_app focuses on the frontend user interface and user-specific functionalities like registration, user profile and song management. 

This approach enhances scalability, maintainability, and flexibility, allowing different teams to work on distinct parts of the project independently and facilitating easier future expansion and testing; *i.e.* this strategic per se fits well to the 12 Factors.

2. **Frontend (Vue.js)**:
   - **Function**: Manages the user interface.
   - **Container**: Docker container for the Vue.js development server.
   - **Design**: Implement responsive web design principles.
   - **CSS Framework**: Use Tailwind CSS for styling.

3. **Database (PostgreSQL)**:
   - **Function**: Stores application data.
   - **Container**: Docker container for the PostgreSQL database.

4. **Integration with Deezer**:
   - **Function**: Fetches and plays music using the Deezer API.
   - **Configuration**: API keys stored in environment variables.

5. **Version Control (GitHub)**:
   - **Function**: Manages version control and collaboration.
   - **Configuration**: GitHub repository for versioning code.

6. **Development Environment (VSCode)**:
   - **Function**: Integrated Development Environment (IDE) for writing and managing code.

7. **Container Orchestration (Docker Compose)**:
   - **Function**: Orchestrates multiple Docker containers.
   - **Configuration**: `docker-compose.yml` file to define and manage services.

8. **Hosting (Back4App)**:
   - **Function**: Manages backend and database services.
   - **Configuration**: Deploy backend and database services on Back4App.

### Additional Notes

- **Django REST Framework**: Necessary for creating RESTful APIs in Django.
- **Environment Variables**: Store sensitive information like API keys and database credentials securely.
- **CSS Framework**: Use Tailwind CSS for consistent and responsive design.

### Important Files

- **.dockerignore**: Defines files and directories that Docker should ignore.
- **.env**: Stores environment variables.


security variáveis de ambiente!.. só .env + .gitingore não adianta porque docker built copia .env, portanto tem que ter tb .dockerignore ...OPÇÃO 2: back4app tb tem opção de fornecer as variávies de ambeinte na hora de criar o deploy do app, como se estivesse configurando as variáveis de ambiente direto no servidor. Talvez seja ainda mais seguro pelo o que entendi, mas preferi não usar essa opção por enquanto, até mesmo para testar a segurança - Professor, tenta acessar as vars?!... desfio para Hacker?


# xxxx

For Back4app there is a [tutorial](https://blog.back4app.com/how-to-deploy-a-django-application/) for Django's deployment. 

The general spets are:
1. create a account on Back4app.
2. install Django (with pip) and start Django's project (with ``` django-admin startproject mysite ```). Observation: it is similar to the Djongo's [tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial01/). Here the project file scturcture are create, special the file *manage.py*. However, they have difference on next step.
4 - migration 

It is the s process

# File and code strucutre



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


# Conclusion Remarks


## tips
visualize and plan the file scture before starting the conde was important to understand the entire project.

.gitingore and .dockerignore
SEO
sequency django, git... not git frist!... due to file structure with django e and containers image.

## 2 Django's App and 12 Factors

The strategy of using two apps, api and music_player_app, aligns well with several of the 12 Factors by Adam Wiggins for building scalable and maintainable applications:

Codebase: By having two separate apps in the same Django project, we maintain a single codebase while separating logical concerns, ensuring a clear tracking of different functionalities.

Dependencies: Each app can clearly define and manage its own dependencies, making it easier to maintain and update required libraries.

Config: With separate apps, environment-specific configurations are easier to manage, adhering to the principle of storing configuration in the environment.

Backing Services: This structure allows easier integration and configuration of supporting services like databases, tailored to each app's specific needs.

Processes: Each app can run as independent processes, facilitating better resource management and scaling.

Port Binding: Each app can be configured to listen on specific ports, which is beneficial for separating concerns, especially for the api service.

Dev/Prod Parity: By modularizing the project, each app can be developed, tested, and deployed independently, ensuring consistency across development and production environments.

This modular approach ensures the project is built in line with modern, scalable software development principles, as outlined in the 12 Factors.