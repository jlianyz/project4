# The Sweet Tooth
## Full Stack Frameworks with Django Milestone Project 
### Introduction
The project consists of an ecommerce site for an online pastry shop called The Sweet Tooth. Visitors to the site are able to read up about the shop’s background, contact the shop, view and search for the pastries available for purchase. They have to create a user account and log in to make the purchases. The site can be found [here](https://jlyzproject4.herokuapp.com/products/), and the information is structured into:

**1. About us page**
  * Shop background
  * Shop FAQs
  
**1. Bakers page**
  * Bakers info and photo on flip card
  
**2. Contact us page**
  * Feedback form
  * Location and delivery hours

**3. Product list page**
  * Search bar
  * Dropdown filter to search by category
  * Links to individual products which contain more details with options to add product to cart

**4. Member page**
  * Registration and log in options for new/existing members
  * Once logged in, able to view and update account details, and logout
  
**5. Shopping cart**
  * Shows products selected
  * Option to make payment by credit card

### User stories
##### As someone who is a regular to this online pastry shop and is looking for pastries to buy, I want to:
* Search for the pastries based on category or key words
* Know if any of the pastries are healthy or meet my specific dietary requirements, if any
* Be able to contact the shop or leave feedback
* Update my personal and account details as and when necessary
* Make my purchases securely using a credit card
* Check my shopping cart to make sure that I have selected the right goods before making my purchase
* Get my password if i forgot it


##### As someone who has not been to this online pastry shop before and is looking for pastries to buy, I want to:
* Read up about the shop’s bakers and background
* Search for the pastries based on category or key words
* Know if any of the pastries are healthy or meet my specific dietary requirements, if any
* Have attractive images of the pastries to be enticed by
* Be able to contact the shop or leave feedback
* Subscribe to their list to know about latest updates
* Create an account easily to make my purchases
* Update my personal and account details as and when necessary
* Make my purchases securely using a credit card
* Check my shopping cart to make sure that I have selected the right goods before making my purchase


##### As someone who is just browsing the online shop with no intention to make purchases, I want to:
* Be able to read up about the shop and its bakers
* Search for and view the products without having to create a user account
* Be able to contact the shop or leave feedback


***

### UX

* **Value**: The site clearly helps users achieve their goals of either searching for product/shop information or making purchases, as it contains relevant information that is easily found
* **Usability**: The website is easy to navigate for users to find what they want with minimal clicks. There is a fixed navbar on top with clearly labelled sections. Links are also relevant, eg. When users are logged in, the nav link of the ‘Members’ area’ changes to “update profile” and “logout”, instead of “register” and “login”. 
 There are links to individual categories of baked goods to allow them to find their desired products easily. 
 The search bar in the product list section allows users to search for products by just typing any word that is in the product. There is also a drop down filter to search for products by category. 
 The fixed footer bar contains social media icons for users to constantly access them easily.
 The site is also mobile responsive so users can easily browse both on desktop and mobile.
* **Desirability**: The website is easy to navigate for users to find what they want with minimal clicks. There is a fixed navbar on top with clearly labelled sections. Links are also relevant, eg. When users are logged in, the nav link of the ‘Members’ area’ changes to “update profile” and “logout”, instead of “register” and “login”. 
* **Call to action**: There are multiple buttons at prominent places to drive users to action. Eg. on the landing page carousel, there is a “shop now” button leading to the products page. On the products page, there are options to “add to cart” both on the product list and product details pages. In the view cart page, if it is empty, there is a prompt to drive the user to the product page to shop. In the fixed footer, there is a call to action to sign up for the mailing list.


***

### UI and features
##### Overall
* The site has consistent typography, with all headers in “Kanit” and all paragraphs in “Alata”. Font sizing is also consistent, with heads, subheaders and text in H1, H3 and P respectively. 
* The colour scheme is pastel and playful, with a focus on pinks and purples. This is suitable for a pastry shop. All text is easily read against the background
* Site is not overcrowded – sufficient negative space to ensure design looks balanced and not cluttered
* Use of bootstrap grid layout throughout so that divs are all evenly spaced
* Landing page images are shown in a carousel, with the option for users to click to speed up the rate at which images change
* Fixed attachment baking related images are shown in section headers for static pages, while still having the text clearly visible as opacity of background image is reduced


#### Desktop and tablet version
* Information is presented in 3-column rows. Pagination is used to ensure that pages are not too long. 
* Sufficient margins are added between columns to keep layout clean and neat

#### Mobile version
* Single columns so that page is not overly cluttered
* Navbar is mobile responsive


### Technologies used
* HTML
* CSS
* Javascript
* [Bootstrap](https://getbootstrap.com/) to create a mobile responsive and stylish webpage
* [JQuery](https://jquery.com/) to simplify DOM manipulation
* Python3 
* Django 2.2.6 as it's main framework
* [Uploadcare](https://uploadcare.com/) to upload images and resize them
* Django Crispy forms to present the Django forms in bootstrap format
* Gunicorn to deploy the project to Heroku
* [Stripe](https://stripe.com/en-sg) API to process the payment
* [Heroku](https://dashboard.heroku.com/login) as a host for the project
* Postgres as the database

***

### Features left to implement
In future, I would like to:
* To create an articles section for admin to add baking/pastries related articles
* To allow users to add ratings and reviews for pastries
* To add a live chat bot to answer user queries in real time

***

### Testing

This site is tested to be responsive on the following devices:
* Iphone 5/6/7/8
* Ipad
* Ipad Pro (best viewed in landscape mode)
* Safari
* Chrome
* Firefox
* Edge
* IE

Manual checks include:

##### Accounts app 

| Test case                                                                                          | Test description                                                                                                                                                                                                                                                                                                                                                                                                     | Outcome |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Registered user is able to log in                                                                  | If username and password is correct, user is logged in and appropriate text is returned<br><br>If username and/or password is wrong, user is unable to log in and error message shows<br><br>If username is not registered, user is unable to log in and error message shows                                                                                                                                         | Pass    |
| User is able to register                                                                           | When all required fields are filled in and passwords match, user is able to register and is redirected to appropriate page<br><br>When one or more required fields are missing, error message shows and user is unable to submit form<br><br>When username is taken, user is prompted to choose another name<br><br>When user’s chosen passwords do not match, error message shows and user is unable to submit form | Pass    |
| Logged in user is able to log out                                                                  | When user clicks on log out button, user gets logged out<br><br>Log out option in dropdown navlink only shows for logged in user                                                                                                                                                                                                                                                                                     | Pass    |
| Logged in user is able to update details                                                           | When user clicks on update profile button, form with account details shows, with the correct user details displayed<br><br>User is able to make changes and submit the update details form<br><br>Update details option in dropdown navlink only shows for logged in user<br><br>After user updates details, the updated details are reflected                                                                       | Pass    |
| Logged in user is able to view account details on main profile page, with correct messages showing | All the fields in the profile page are correct                                                                                                                                                                                                                                                                                                                                                                       | Pass    |

##### Cart app

| Test case                                              | Test description                                                                                                                                                                                                                   | Outcome |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Cart icon in navbar shows number of items in cart      | When logged in user adds/removes a product to the cart, the number increases/decreases<br><br>When user completes a transaction, the number resets to 0                                                                            | Pass    |
| Only logged in user can view cart                      | When un-logged in user clicks on the cart icon, they are prompted to login or register for an account                                                                                                                              | Pass    |
| User is able to view items in cart                     | When cart is empty, a message asking them to shop, with a button to the products page shows up<br><br>If there are items in the cart, they show up in a 3-col row with the correctly sized image, product name, quantity and price | Pass    |
| User is able to update quantity of each item from cart | When user changes quantity and clicks on update quantity button, product quantity changes accordingly (does not go <0).                                                                                                            | Pass    |
| Session clears when user logs out                      | When user logs out, the cart becomes empty and number next to cart item resets to 0                                                                                                                                                | Pass    |

##### Checkout app

| Test case                                         | Test description                                                                                                                                                                                                                                                  | Outcome |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| User is able to check out items in the cart       | When user clicks on ‘Proceed to payment’ button, he gets redirected to payment page<br><br>At payment, items selected are displayed correctly in table form                                                                                                       | Pass    |
| Payment amount reflects correct amount to be paid | Check that sub total amount matches total cart value<br><br>Check that delivery fee is added correctly<br><br>Check that total amount is delivery fee plus sub total amount                                                                                       | Pass    |
| User is able to complete the payment form         | If required fields are incomplete, user cannot submit the form<br><br>If expiry date of card is in the past, user cannot submit<br><br>If CVV number does not have exactly 3 digits and/or credit card number does not have exactly 16 digits, user cannot submit | Pass    |
| Payment goes through                              | User gets redirected to payment success page upon payment<br><br>Cart resets to 0                                                                                                                                                                                 | Pass    |
| Payment is received                               | Payment shows up in admin account and in stripe dashboard                                                                                                                                                                                                         | Pass    |

##### Product app

| Test case                                                                      | Test description                                                                                                                                                                                                                                             | Outcome |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Products are showing up correctly in the product list page                     | On product page, product image, name and price, and add to cart button are showing in each card in a 3-col row<br><br>All created products are showing and all links are working<br><br>Pagination works                                                     | Pass    |
| When individual product card is clicked, user goes to the product details page | Product details are showing correctly with bigger image on the left, product price, description and tag on the right with buttons to add to cart and go back to product list page<br><br>When user clicks to add quantity, correct quantity is added to cart | Pass    |
| User is able to search for product                                             | User can type any part of the product name and the search still works<br><br>User is able to reset search by clicking on "all products"                                                                                                                                                   | Pass    |
| User is able to filter product by category                                     | Dropdown menu works<br><br>Dropdown links work<br><br>Correct category is showing for correct link<br><br>On hover, the dropdown button changes color                                                                                                        | Pass    |

Automated testing includes:
* [Auto Pep 8](https://pypi.org/project/autopep8/) to ensure Python formatting is correct
* [HTML and CSS formatter](https://codebeautify.org/htmlviewer/) to ensure that HTML and CSS formatting is correct

##### Known errors
For IE, the flip card in the bakers section does not work.
***

### Deployment
Heroku deployment - this is done as a last step to ensure that all installed packages are included in the requirements.txt file 
1.	Sign up for a [Heroku](https://www.heroku.com/) account
2.	Install Heroku using bash: `sudo snap install heroku --classic`
3.	Install dependencies (gunicorn, Pillow, psycopg2, whitenoise, dj_database_url)
4.	Add Whitenoise to middleware inside settings.py
5.	Log into heroku account with `heroku login -i`
6.	Create a new app in bash: `heroku create <app_name>`
7.	Copy over uploadcare and Stripe key details from bashrc into Heroku Config vars
8.	Create a Procfile and add the following line: `web: gunicorn <PROJECT_FOLDER>.wsgi:application`
9.	Add heroku app url to allowed hosts in settings.py, and also change the static directory to STATIC_ROOT
10.	Create the requirements.txt file using bash: `pip3 freeze --local > requirements.txt`
11.	Commit and push the project to heroku
* `git add .`
* `git commit -m "commit name"`
* `git push heroku master`
12. Set up Postgre database with `heroku addons:create heroku-postgresql`
13. Get the updated databse url by typing `heroku config`, and copy it into settings.py and Heroku's Config vars
14. Migrate database and create a superuser to make changes to it


I deployed the site to Github with the following steps:
1. Go to this repository's github [link](https://github.com/jlianyz/project4)
2. Click on settings --> Github Pages
3. Select "none" for the Source and then select "master branch"

To deploy the page locally:
1.	Go to the github [link](https://github.com/jlianyz/project4)
2.	Click on the Clone/download button and copy the URL 
3.	Set up and install your own Stripe and uploadcare accounts, and also install crispy forms
5.	To run the application locally, type `python3 manage.py runserver 8080` in bash
***
### Credits
**Images**

The images were taken from [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/) and a friend's photography [site](http://www.danielshechter.com/) 

**Text**

The text was adapted from [Edith Patisserie](https://www.edithpatisserie.com/)

**Typography**

The fonts were taken from [Google fonts](https://fonts.google.com/)

**Logo and favicon generator**

I generated the favicon and logo using [Hatchful](https://hatchful.shopify.com/)