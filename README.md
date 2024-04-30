# ***WineShack - Portfolio Project 4***
---
# **Site Overview**

- **Description :** **WineShack** is a website offering wine enthusiasts a place to source great wine.  **WineShack** offers users the ability to search for various wines by grape variety, price, winery region and by rating - where the wines have been rated by other local enthusisats. 
- **Key project goal :** To enable wine enthusistast to find and purchase wine from around the world. **WineShack** store, give users an easy checkout function with effortless profile and order management.
- **Audience :** This website is aimed at those 18 years and older. It offers overs of wine a place to purchase wines but also family members, friends, work colleagues the opportunity to gift wines the wine lover in their lives.
- **Live version :** Live version of **WineShack** page can be viewed at [https://wineshack-c948e5d21774.herokuapp.com/](https://wineshack-c948e5d21774.herokuapp.com//).

![Mockup](/testing/images/Amiresponsive.png)

---

# **Table of content**

## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
    * [***How Is This Will Be Achieved:***](#how-this-will-be-achieved)
    * [***Wireframes***](#wireframes)
    * [***Color Scheme***](#color-scheme)
    * [***Technology Used***](#technology-used)
    * [***Languages Used***](#languages-used)
    * [***Frameworks, Libraries & Programs Used***](#frameworks-libraries-&-programs-used)
1. [**Common Features**](#common-features)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
    * [*Testing*](#testing)
    * [*Testing User Stories from User Experience (UX) Section*](#testing-user-stories-from-user-experience-ux-section)        
    * [*Further Testing*](#further-testing)
1. [**Accessibility**](#accessibility)
1. [**Known Bugs**](#known-bugs)
1. [**Deployment**](#deployment)
1. [**Content**](#content)

## **Planning stage**
### **Target Audiences:**
* Those who are interested in Wine and wine tasting.
* Those who have wine enthusiasts in their lives and are looking for gift ideas.
* Users who are looking to expand their wine knowledge and tasting palette.


### **User Stories:**
* As a user, I want to easily find wine based on a search criteria.
* As a user, I want to a fast and secure checkout experience.
* As a user, I want to save my order history and payment details.
* As a user, I want to be able to update my profile information easily.
* As a site administrator,  I want to be able to update and edit product information.
* As a site administrator,  I want to be able to umanage my users and their profile information.
* As a site administrator,  I want there to be as much automation as possible so purcahses can be made 24/7, worldwide.




### **Site Aims:**
* To enable users a quick search and find process, filtering items by desired criteria i.e. wine region, wine tasting rating.
* To enable users to quickly checkout, even without saving their payment details if they prefer.
* To provide a wide range of products all with reviews to support choosing a wine.
* Enable users to save and update thier delivery details for easier checkout when returing to purchase. 

### **How This Will Be Achieved:**
* A user profile is available for users to opt into. While on the checkout page the user can opt to save thier delivery information to their profile. Or to checkout without creating a profile.
* Users who do decide to create a profile can also use thier profile page to store thier purchase history.
* Users can use the search functionalty to search for wines based on a range of criteria. THere are also drop down menus whcih also filter the products. 
 

### **Wireframes:**
I used Canva to create a visual representation of the WineShack site - below are the initial idea designs:

* Desktop Wireframes:

* Landing Page:
This page will be the first view of the site the users get - I want this to be minimal and clean and give the users an easy way to navigate to the products.
    * ![Landing page](testing/images/landing%20page.png)

* Products Page
This page will display all the products available and will offer the user further sorting and filtering options to find their desired products.
    * ![Products](testing/images/products.png)

* Profile Page:
This page will be concise and will enable the user to update thier details easily, this information will be automatically populated into the checkout form.
    * ![Profile](testing/images/account.png)

Checkout Page:
* This page, although will have a lot of information, I will hopefully be able to make it look easy to navigate and easy to complete, providing the user with all th informtion needed to complete thier purchase.
    * ![Checkout](testing/images/checkout.png) 



### **Color Scheme:**
I wanted the colour scheme to be clean and fresh so I opted for a black and white design. This enabled me to highlight the wines on display without distracting the user. From my research this is also a common feature on other e-commerce sites.

FOnts used are also clean and minimal again to ensure there is no distraction when users are searching/reviewing wines.

### **Technology Used:**
### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)
-   [Javascript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)



### Frameworks, Libraries & Programs Used

1. [jQuery](https://jquery.com/)
    - was used to support event handling and CSS animation throughout the site.
1. [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used to apply styling and responsivness thorughout the site.
1. [Jinja:](https://jinja.palletsprojects.com/en/3.1.x/)
    - Jinja was used to enable template inheritance throughout the site.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on the forms on the activity page, alongside the social media icons within the footer.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the command line terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub was used to store the project code after being pushed from Git.
1. [Canva:](https://www.canva.com/)
    - Canva was used to create the wireframes during the design process.
1. [ImageColorPicker:](https://imagecolorpicker.com/)
    -Image Color Picker was used to select the colors for my background, container backgrounds and text. 


### **Common Features**

The navigation element used from the bootstrap framework. A base template was used then extended using Jinga reducing the amount of code written but also reducing the duplication of code. 

Within the product pages there is the ability to see more information about the product.

Within the checkout pages a form using Cripsy Forms was used to render details to the page as well as then save the details within other parts of the site.

### **Future-Enhancements**

* Within the profile page, a future development would be to add more profile details. Including the ability to store favourite wines, to review wines and have a record of personal wine tasting reviews.

* The addition of knowledge pages would also be included, to further support the user through their wine tasting journey.

* A highlight of popular wines could be a good addition to the main page, to highlight to users as they enter the site.


### **Testing Phase**

### **Testing**

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/nu/) 
    
    Homepage:

    Initial tests show various errors to be corrected.
    ![Initial test results](testing/images/htmlvalidatorerrors.png)
    After fixing the errors, the final test results confirm no errors or warnings.
    ![Final test results](testing/images/htmlvalidator.png)


    Products Page:

    Initial tests show various errors to be corrected.
    ![Initial test results](testing/images/HTML_Validator_Errors_ProductsPage.png)
    After fixing the errors, the final test results confirm no errors or warnings.
    ![Final test results](testing/images/HTML_Validator_ProductsPage.png)

    
    Product Details Page:

    Initial tests show various errors to be corrected.
    ![Initial test results](testing/images/HTML_Validator_Error_ProductDetailsPage.png)
    After fixing the errors, the final test results confirm no errors or warnings.
    ![Final test results](testing/images/HTML_Validator_ProductDetailsPage.png)

    Add Products Page:

    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_AddProduct.png)

    Edit Products Page:

    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_editPage.png)

    Profile Page:

    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_ProfilePage.png)

    Registration Page:
    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_RegistrationPage.png)

    Sign in page:
    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_LoginPage.png)

    Log out page:
    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_logoutPage.png)


    Bag Page:

    Initial tests show various errors to be corrected.
    ![Initial test results](testing/images/HTML_Validator_Error_BagPage.png)
    After fixing the errors, the final test results confirm no errors or warnings.
    ![Final test results](testing/images/HTML_Validator_BagPage.png)


    Checkout Page:

    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_checkoutpage.png)

    Checkout Success Page:

    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/HTML_Validator_CheckoutSuccess.png)



    CSS:
    -   [W3C CSS Validator](https://jigsaw.w3.org/css-validator) 


    Initial tests show no errors found, and a reccomendation offered.
    ![Initial test results](testing/images/CSS_Validator.png)

    



### Testing User Stories from User Experience (UX) Section

1. As a user, I want to easily find wine based on a search criteria.

    1. Users are able to search for wines using the search bar at the top of the homepage and within the products page. Drop down menus further sorting wines into categories can be found on the products page and the homepage. 

    2. Within the products page, users can further sort the products using the filter functionality to the right of the page. On the left of the page, users can see how many products have been filterd and have the ability to return to the home page, removing the filters applied. 
        
2. As a user, I want to a fast and secure checkout experience.
    1. The site uses Stripe to complete the users checkout experience. Stripe provides the user with security and confidence as they checkout. Webhooks are used throughout the checkout process to enable an issues to be caught and rectified and additional functionality is woven within the webhooks to allow fallbacks should any part of the transaction fail. 
    2. Users can follow their purchases with pop up's informing them of what has been added to thier bag, how much more they should spend to obtain free delivery.

3. As a user, I want to save my order history and payment details.
    1. The users have the option to save their payment and delivery details to a profile, or can checkout without a profile and receive their email confirmations. If they choose to create a profile, they will have the option to navigate to their profile page following successful checkout - here they can see past orders and update thier personal details.
    

4. As a user, I want to be able to update my profile information easily.
    1. Users can update their personal information while on the profile page. Information saved within the profile page is then populated into the relevant fields of the checkout page if the users return to purchase wine again.
    

5. As a site administrator,  I want to be able to update and edit product information.
    1. Site administrators have additional functionality available to them if they have signed in with superuser credentials. This includes edit and delete buttons available on all products within the products page. Also, an additional drop down menu is displayed under the accounts menu - this allows superusers the ability to add and edit products.  
    

6. As a site administrator,  I want there to be as much automation as possible so purcahses can be made 24/7, worldwide.
    1. Automation is woven througout the site to enable 24/7 access. This includes automatic emails at key points within the registraion and checkout process. Tooltips are used to provide the user with notifications.  



### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer and Microsoft Edge.
-   The website was viewed on a variety of devices such as Desktop, Laptop and android phones.


### Accessibility
I wanted to ensure the site supported all visitors, I included the following in my code to ensure this:

* All images contain an alt tag, which is dynamically added with each image. The alt tag is the wine name. 
* The site is responsive to different screen sizes 
* I used semantic elements throughout the design

### ***Known Bugs***

* Although there are no known bugs within the site. There is a lot of functionality which can be added.   


## **Deployment**
The site is hosted on Heroku, following deployment to Git Hub. To enable the products to be hosted the site is connected to AWS storage, which holds the static files for the site. 

Gmail was integrated into the site using this process:
 - Obtain GMail username and app key (password) - GMAIL SMTP to be used as mailing client.
* Navigate to https://accounts.google.com/ and follow all steps for registering new email address
* Login to google with newly created email address and password.
* Navigate to https://accounts.google.com/ once again
* Select Security > Signing in to Google > 2-Step Verification > App Passwords
* Enter a name of the app password and select Generate
* An app password will be provided
* Update settings.py in the project directory

ElephantSQL was the database used to store the database:
* Navigate to https://www.elephantsql.com/ and follow all steps for registering new account
* Login to ElephantSQL with newly created account credentials
* Navigate to + Create New Instance
* Select Name, Plan and Region
* Confirm the instance by pressing Create Instance
* Obtain database URL in format postgres://NAME:PASSKEY@flora.db.elephantsql.com/NAME
* Update settings.py in the project directory

Deployment to Heroku:
* Register & Log In with heroku
* Navigate to New > Create New App
* Select Name of the app that is unique
* Navigate to Settings > Reveal Config Vars
* Add all variables from env.py to ConfigVars of Heroku App
* Add the Heroku app URL into ALLOWED HOSTS in settings.py
* In root create file name Procfile
* Navigate to Deploy > GitHub > Connect
* Navigate to Deploy > Deploy Branch
* Use 'open app' button at top of page to open the site


### **Content:**
* I used Code Institue's walk through videos to support this project.
* I used Font Awesome for the icons throught the site [Font Awesome](https://fontawesome.com) 
* Images were taken from [Pexels](https://www.pexels.com/)
