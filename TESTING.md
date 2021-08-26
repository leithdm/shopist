
# Testing <!-- omit in toc -->

## Table of Contents
- [HTML Validator](#html-validator)
  - [W3C HTML Markup Validation Service](#w3c-html-markup-validation-service)
- [CSS Validator](#css-validator)
  - [W3C CSS Validation Service](#w3c-css-validation-service)
- [JavaScript](#javascript)
- [Python](#python)
- [Compatability and Responsiveness](#compatability-and-responsiveness)
  - [Manual Testing](#manual-testing)
  - [Functionality, Usability, Data Management](#functionality-usability-data-management)
    - [Chrome Dev Tools - Lighthouse](#chrome-dev-tools---lighthouse)
- [User Stories](#user-stories)
- [Bugs](#bugs)

<br/>


# HTML Validator

## [W3C HTML Markup Validation Service](https://validator.w3.org/)

<br/>

- [Home Page (store/index.html)]()
- [Footer (store/footer.html)]()
- [Navbar (store/navbar.html)]()  
- [Product Details (store/product_details.html)]()  
- [Login (author/login.html)]()
- [Signup (author/signup.html)]()
- [Profile (profiles/profile.html)]()
- [Profile (profiles/order_detail.html)]()
- [Checkout Index (checkout/index.html)]()
- [Checkout ThankYou (checkout/thank_you.html)]()

<br/>

**Result:** the W3C Validator for HTML does not understand the Jinja templating syntax, therefore shows repeat Errors. 
See sample output below for `store/index.html`. 
Aside from the Jinja warnings and errors, all other code is valid for each of the .html pages listed above. 

![Home Page HTML Validator](static/testing/index.html-testing.PNG)




----------

<br/>

# CSS Validator

## [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

<br/>

![CSS Validator](static/testing/css-testing.PNG)

**Result:** No Errors, 6 warnings.


![CSS Warnings](static/testing/css-warnings-testing.PNG)

<br/>

----------

# JavaScript

I was able to leverage Bootstrap to provide most of the JavaScript functionality on this site. 
However, the following code was also added to `footer.html` in order to print the current year for Copyright purposes. 

`<script>document.write(new Date().getFullYear());</script>`

**Result:** This code passed through [JSHint](https://jshint.com/) without any errors. 


<br/>

----------

# Python

[PEP8 Online](http://pep8online.com/)

**Result:** All .py files are PEP8 compliant. 


<br/>

----------

# Compatability and Responsiveness

## Manual Testing

- Browser compatability: To ensure a broad range of users can successfully use this site, it was manually tested across 
  the 6 major browsers:

  - Chrome v.87
  - Edge v.85
  - Firefox v.81
  - Safari v.12
  - Opera v.71
  - Internet Explorer v.6-11 (tested via [BrowserStack](https://www.browserstack.com/test-in-internet-explorer)).
  

- Site responsiveness was tested using [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) using 
  profiles for a wide variety of devices.


- Physical Devices tested included:
  - iPhone 5 (iOS: 12.4.9)
  - iPhone 6 (iOS: 12.4.9)
  - Samsung Galaxy A10 (Model SM-A105FN, Build/QP1A, on Android 10)
  - MacBook Pro (Retina, 13", Late 2013, OS Catalina)
  - Apple iMac 27" (also running Windows 10 Pro ver. 2004, OS 19041.630)

<br/>

**Result:** Both browser compatability and site responsiveness testing can be summarised in the table below. 
Responsiveness was good on all of the devices listed, both physical and simulated. Brower compatability was good across 
all the major browsers, except for Internet Explorer 6-11.

![Responsive Design](static/testing/responsiveness.png)

<br/>

----------

## Functionality, Usability, Data Management

I created a comprehensive Testing Document to assess site functionality, usability and data management which can be viewed 
as a PDF **[here](static/testing/manual-testing-procedure.pdf).**

**Overview of Testing Procedure:**
1. Testing Account Creation and Log in.
2. Testing Create, Read, Update, Delete of Products.
3. Testing Create, Read, Delete of Product Reviews.
4. Testing 404, 403, 500 Errors.
5. Testing URL Protection.
6. Testing Search Functionality. 
7. Testing Stripe Payment Functionality. 

**Result:** Site performed as expected. Please see the Testing Document referenced above. 

<br/>

----------

### Chrome Dev Tools - Lighthouse

Automated testing was performed using [Chrome Dev Tools - Lighthouse](https://developers.google.com/web/tools/lighthouse). 
Lighthouse is an open-source, automated tool for improving the quality of web pages. It performs audits under 
the following headers:
1. Performance
2. Accessibility
3. Best Practices
4. SEO

**Result:** see summary results below for **Desktop *index.html***. 
- For *Best Practices* x5 insecure requests were found as the site does not use HTTPs. As that is not within the remit
of this project, these warnings were ignored. 

![Desktop](static/testing/lighthouse-desktop.png)


<br/>

----------

# User Stories


**Result:** The majority of user stories have been successfully implemented, with a :white_check_mark: to denote items that 
have been implemented. User stories related to an adminstrator account have been pushed into a later sprint. 

<br/>

"**__As a *non-registered user*, I__** ______________________________________________"

- :white_check_mark: should be presented with products on the main page. 
- :white_check_mark: should be able to click on a product on the main page to view the product description, reviews, etc. 
- :white_check_mark: should be able to search through products.
- :white_check_mark: should be able to register an account with the site in order to purchase products, and review them. 

<br/>

"**__As a *registered user*, I__** ______________________________________________"

- :white_check_mark: should be able to login to the site in order to purchase products. 
- :white_check_mark: should be presented with a profile page showing my details. 
- :white_check_mark: should be able to make purchases using Stripe. 
- :white_check_mark: should be able to view purchase history from my profile page.
- :white_check_mark: should be able to write reviews on any other products.   
- :white_check_mark: should be able to logout of my account. 

<br/>


----------

# Bugs


[Go back to README.md file](README.md).