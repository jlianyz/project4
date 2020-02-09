# The Sweet Tooth
## Full Stack Frameworks with Django Milestone Project 
### Introduction
The project consists of an ecommerce site for an online pastry shop called The Sweet Tooth. Visitors to the site are able to read up about the shop’s background, contact the shop, view and search for the pastries available for purchase. They have to create a user account and log in to make the purchases. The site can be found here, and the information is structured into:

**1. About us page**
  * Shop background
  * Shop FAQs
  * Bakers info

  
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

#### Desktop and tablet version
* Fixed attachment baking related images are shown in section headers for static pages, while still having the text clearly visible as opacity of background image is reduced
* Information is presented in 3-column rows. Pagination is used to ensure that pages are not too long. Sufficient margins are added between columns to keep layout clean and neat
* Landing page images are shown in a carousel, with the option for users to click to speed up the rate at which images change.
* A modal is added on the landing page as a call to action, which users can easily close either by click on the “x” or outside of the modal. 


#### Mobile version
* Single columns so that page is not overly cluttered
* Navbar is mobile responsive
* For section headers, the background is a color gradient instead of an image so that the page loads quicker. It is also difficult to find a suitable background image for jumbotrons this small.
* Modal is removed as it takes too much space when clicked


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
* Sqlite3 as the database

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

Manual checs include:

##### Accounts app 

| Test case                                                                                          | Test description                                                                                                                                                                                                                                                                                                                                                                                                     | Outcome |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Registered user is able to log in                                                                  | If username and password is correct, user is logged in and appropriate text is returned<br><br>If username and/or password is wrong, user is unable to log in and error message shows<br><br>If username is not registered, user is unable to log in and error message shows                                                                                                                                         | Pass    |
| User is able to register                                                                           | When all required fields are filled in and passwords match, user is able to register and is redirected to appropriate page<br><br>When one or more required fields are missing, error message shows and user is unable to submit form<br><br>When username is taken, user is prompted to choose another name<br><br>When user’s chosen passwords do not match, error message shows and user is unable to submit form | Pass    |
| Logged in user is able to log out                                                                  | When user clicks on log out button, user gets logged out<br><br>Log out option in dropdown navlink only shows for logged in user                                                                                                                                                                                                                                                                                     | Pass    |
| Logged in user is able to update details                                                           | When user clicks on update profile button, form with account details shows, with the correct user details displayed<br><br>User is able to make changes and submit the update details form<br><br>Update details option in dropdown navlink only shows for logged in user<br><br>After user updates details, the updated details are reflected                                                                       | Pass    |
| Logged in user is able to view account details on main profile page, with correct messages showing | All the fields in the profile page are correct                                                                                                                                                                                                                                                                                                                                                                       | Pass    |
***

### Deployment

***
### Credits
**Images**

The images were taken from [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/) and a friend's photography site (http://www.danielshechter.com/) 

**Text**

The text was adapted from [Edith Patisserie](https://www.edithpatisserie.com/)

**Typography**

The fonts were taken from [Google fonts](https://fonts.google.com/)

**Quantity adder**

I adapted the code from [our teaching assistant's github](https://github.com/Code-Institute-Submissions/TGC-CI-Project4-V2/blob/master/products/templates/shop-single.html)

**Logo and favicon generator**

I generated the favicon using [Hatchful](https://hatchful.shopify.com/)