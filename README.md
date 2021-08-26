


- [Overview](#overview)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Frameworks](#frameworks)
    - [Color Scheme](#color-scheme)
    - [Icons](#icons)
    - [Typography](#typography)
  - [Wireframes](#wireframes)
  - [Schema](#schema)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Front-End Technologies](#front-end-technologies)
  - [Back-End Technologies](#back-end-technologies)
    - [Django](#django)
    - [Heroku](#heroku)
    - [Python](#python)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

<br/>

---

## Overview

Shopist is an e-commerce site for purchasing boutique products. You can view the deployed site 
[here](https://shopist-dml.herokuapp.com/). 

<br/>

## UX

This project is part of the [Code Institute](https://codeinstitute.net/) Full Stack Software Development course, 
specifically **Module 4: Full Stack Frameworks with Django**. 

The objective for this milestone project is to "*build a full-stack site that allows your users to manage a common 
dataset about a particular domain*".

<br/>

### User Stories

- User Stories were written from the perspective of x2 different user(s):
    - the non-registered user that wants to view products, reviews on those products, without purchasing. 
    - the registered user that wants to purchase products, review their profile and purchase history, and leave reviews on products.

<br/>

"**__As a *non-registered user*, I__** ______________________________________________"

- should be presented with products on the main page. 
- should be able to click on a product on the main page to view the product description, reviews, etc. 
- should be able to search through products.
- should be able to register an account with the site in order to purchase products, and review them. 

<br/>

"**__As a *registered user*, I__** ______________________________________________"

- should be able to login to the site in order to purchase products. 
- should be presented with a profile page showing my details. 
- should be able to make purchases using Stripe. 
- should be able to view purchase history from my profile page.
- should be able to write reviews on any other products.   
- should be able to logout of my account. 

<br/>

### Design

- The overall concept was to have a minimalist yet modern color scheme, with a modern sans serif typography. 

<br/>

#### Frameworks

- [Django 3.2.5](https://docs.djangoproject.com/en/3.2/releases/3.2.5/) is a framework that is used to render the back-end Python with front-end Bootstrap. 

<br/>

#### Color Scheme

Minimalist colors are employed. 

- ![#212529](https://via.placeholder.com/15/212529/000000?text=+) `#212529` body text and background
- ![#868e96](https://via.placeholder.com/15/868e96/000000?text=+) `#868e96` block quotes
- ![#ffa500](https://via.placeholder.com/15/ffa500/000000?text=+) `#ffa500` main page jumbotron
- ![#0085A1](https://via.placeholder.com/15/0085A1/000000?text=+) `#0085A1` hover

<br/>

#### Icons

- [Font Awesome 5.6.1](https://fontawesome.com/) icons are used for the social media links, and the quotes in the 
footer.

<br/>

#### Typography

- [Google Fonts](https://fonts.google.com/) were used across the site, namely:
  - [Lora](https://fonts.google.com/specimen/Lora) - for body text.   
  - [Open Sans](https://fonts.google.com/specimen/Open+Sans) - for headings. 

<br/>

### Wireframes

- Wireframes were created using [Balsamiq Wireframes](https://balsamiq.com/) and can be viewed by clicking on links 
  below.

<br/>


|    Home Page   |    Registration Page     |    Login Page    |    Individual Post    |    Profile Page    
|    :----:      |    :----:                |    :----:        |    :----:             |    :----:        |
|[Desktop/Mobile](wireframes/main.png)|[Desktop/Mobile](wireframes/registration.png)|[Desktop/Mobile](wireframes/login.png)|[Desktop/Mobile](wireframes/post.png)|[Desktop/Mobile](wireframes/profile.png)

<br/>


### Schema

The database consists of x3 collections, which we can represent as follows:

![Schema](wireframes/schema.PNG)


---

## Features

### Existing Features
  - **Register Account:** Anybody can register for free and create their own unique account. There is authentication and authorization to check certain criteria is met before an account is validated. All passwords 
    are hashed for security purposes.
  - **Log In to Account:** For existing users, there is more authentication and authorization incorporated to check 
    that the hashed passwords and username match the database.
  - **Log Out of Account:** Users can easily log out of their account by clicking the logout button. 
  - **View All Products:** On the *index* page, all products are initially displayed, based on date of submission. Pagination is enabled. 
  - **Search Products:** The user can search for a relevant products, searched by product name. 
  - **CRUD Profile:** A registered user can create, read, update and delete their profile details. They can also create, read, delete their reviews. 
  - **Read Purchase History:** A registered user can read their purchase history.

<br/>

### Future Features
A full list of future features **can be viewed in the 
[Product Backlog](https://github.com/leithdm/milestone-project-3/projects/1)**, but we will briefly mention some 
of them here:

<br/>

---

## Technologies Used

- [VSCode](https://code.visualstudio.com/) - used as the primary IDE.
- [GitHub](https://github.com/) - used for remote storage of code.
- [TinyPNG](https://tinypng.com/) - used to optimize (.jpg, .png) images for faster loading.
- [Balsamiq](https://balsamiq.com/) - used to create the project's wireframes.

### Front-End Technologies

- [HTML5](https://en.wikipedia.org/wiki/HTML5) - used to provide content and structure.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - used to provide styling.
- [JavaScript ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Google Fonts](https://fonts.google.com/) - used to provide font styling.
- [Am I Responsive?](http://ami.responsivedesign.is/) - used to show site responsiveness.

### Back-End Technologies

#### Django
- [Django 3.2.5](https://docs.djangoproject.com/en/3.2/releases/3.2.5/) is a framework that is used to render the back-end Python with front-end Bootstrap. 

#### Heroku
- [Heroku](https://www.heroku.com/) - to host the site.
  
#### Python
- [Python 3.9](https://www.python.org/downloads/release/python-390/) - back-end programming language. 

<br/>

---

## Testing

The testing process can be viewed [here](TESTING.md).

<br/>

---

## Deployment

**Local Deployment**

In order to run this project locally on your own system, you will need the following installed:

- [Python3](https://www.python.org/downloads/) to run the application.
- [PIP](https://pypi.org/project/pip/) to install all app requirements.
- Any IDE such as Microsoft [Visual Studio Code](https://code.visualstudio.com/).
- [GIT](https://git-scm.com/) for cloning and version control.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green Clone or download button and downloading the project as a 
  zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:

`git clone https://github.com/leithdm/medium-bloggy.git`

- Navigate to the correct file location after unpacking the files.

`cd <path to folder>`

Create a `env.py` file with the relevant credentials. See the sample env.py file below, for example:



```
import os

os.environ.setdefault("STRIPE_PUBLISHABLE_KEY", "YOUR_STRIPE_PUBLISHABLE_KEY")
os.environ.setdefault("STRIPE_SECRET_KEY", "YOUR_STRIPE_SECRET_KEY")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("DEBUG", "TRUE")

```

- Install all requirements from the requirements.txt file using this command:

`sudo -H pip3 -r requirements.txt`


- You should now be able to launch your app using:

`python3 manage.py runserver`

- The site should be running on `localhost` on an address similar to `http://127.0.0.1:5000`.
<br/>

**Remote Deployment:**

This site is currently deployed on Heroku using the master branch on GitHub. To implement this project on Heroku, 
the following steps were taken:

1. Create a **requirements.txt** file so [Heroku](https://www.heroku.com/) can install the required dependencies to run 
   the app.

`sudo pip3 freeze --local > requirements.txt`

2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.

`echo web: python run.py > Procfile`

3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can 
   *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.

4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables 
   as follows:

```
AWS_ACCESS_KEY_ID: <your_AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY: <your_AWS_SECRET_ACCESS_KEY>
DATABASE_URL: <your_DATABASE_URL>
SECRET_KEY : <your_secret_key>
STRIPE_PUBLISHABLE_KEY: <your_STRIPE_PUBLISHABLE_KEY>
STRIPE_SECRET_KEY: <your_STRIPE_SECRET_KEY>
USE_AWS: True
```
5. Your app should be successfully deployed to Heroku. 

<br/>

---

## Credits

### Media

- Pictures used on this site were obtained from [Unsplash](https://unsplash.com/). 
  Credit goes to the following photographers: 
  [Alex Block](https://unsplash.com/photos/oH34atgXJsQ), 
  [Rohit Tandon](https://unsplash.com/photos/9wg5jCEPBsw), 
  [KiwiHug](https://unsplash.com/photos/MS9Tnh3if1o)
  
- [Logomakr](https://logomakr.com/) was used to create the site logo. 

<br/>

### Acknowledgments

- [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/?originalSubdomain=ng) - for his mentorship 
  and guidance.