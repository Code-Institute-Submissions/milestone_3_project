

![responsive image](https://github.com/samc85/milestone_3_project/blob/master/images/readme_page.png)

https://github.com/samc85/milestone_3_project

https://milestone-3-project.herokuapp.com/


# Speech Language and Communication Needs Library
This website is a resource for a teachers and education staff to use to best support students with Speech, Language and Communication Needs.  By providing
two libraries one for Training Courses and one for suitable Interventions, this resource will help education staff be better prepared and more informed
with their training needs and provision choices.  


### Company mission statement:

The SLCN library seeks to provide a one stop resource for education staff that supports the training and intervention needs to best meet the needs of their students.


# User Experience (UX)

The webpage is designed to be simple, efficient and easy to use.  Their is a purposeful lack of pictures or resource heavy content.  The site is designed to be as 
efficient and easy to use on a range of devices that would be prevalent in schools, including ipads, desktops and phones, so that users can access the site from 
anywhere.   



# Design

### Description of pages

Home Page, About Page and Help Page

The above three pages represent the static part of the website.  These are pure information pages designed to inform the user on the purpose, content and how to use the webpage.  
They are broken down as follows:

Home Page
* About the page with information about Speech and Language Needs in the UK

About Page
* About the company and its intended missions statement.  What the website aims to provide for users.

Help Page
* How to use the webpage and a contact form in which further support can be added.

Intervention and Intervention Add Pages
* View, search and add intervention collections.  Further functioning within these pages allow you to edit, delete and view interventions.

Training and Training Add Pages
* View, edit and add training collections.


# User Stories

* As a user, I wish to be able to find information about the app purpose.
* As a user, I wish to be able to use the site without too many instructions or technical expertise.
* As a user, I wish to be able to search for relevant interventions to meet the needs of my students.
* As a user, I wish to be able to view a range of training courses for myself and my staff
* As a user, I wish to be able to edit what both I have, and others have added to ensure consistency and reliability.
* As a user, I wish to be able to delete what I or others have added, to ensure appropriateness.
* As a user, I wish to be able to add or edit interventions and training with ease, through simple to use Formatters
* As a user, I wish to have access to other information sources to inform my choices.


# Wireframes

Wireframes are generally true to the webpage, however some details have evolved as the project began.

[Wireframes](https://github.com/samc85/milestone_3_project/tree/master/images/wireframes)



# Features

The following features are present on the webpage:

## Navbar
* Easy to follow links for navigation.
* Navbar collapses to side-bar for mobile design in order to aid ease of use on smaller devices.

## Add Content
* Users are able to add their own interventions and training to the respective pages, using the categorized form.

## Edit Content
* Users are able to edit both theirs and others content.

## Delete Content
* Users are able to delete both theirs and others input.

## Contact Form
* Users are able to request help using a contact form

## links
* Users can follow links to other Speech and Language Resources.

# Features Left to Implement

As this is designed for schools, safeguarding of student details is paramount.  An additional
feature of adding student profiles and linking to interventions undertaken can be implemented
once security of data is properly implemented.


# Database

The Database used is the nonSQL MongoDb.  Database consisted of 2 collections, being

* Interventions
* Training 

These were designed as follows:



## Interventions   

| Title     | Key in collection      | Data Type   |
| -------   | -------------------    | ----------- |
| Id        | _id                    | ObjectId    | 
| Name      | intervention_name      | string      |
| Area      | intervention_area      | string      |
| Website   | intervention_website   | string      |
| Rating    | interention_rating     | string      |
| Duration  | intervention_duration  | string      |
| Resources | intervention_resources | string      |
| Cost      | intervention_cost      | string      |



## Training

| Title          | Key in collection      | Data Type   |
| -------        | -------------------    | ----------- |
| Id             | _id                    | ObjectId    | 
| Name           | training_name          | string      |
| Type           | training_type          | string      |
| Delivery       | delivery_method        | string      |        
| Start          | start_date             | string      |
| Duration       | training_duration      | string      |
| Area           | training_area          | string      |
| Qualification  | qualification          | string      |
| Cost           | training_cost          | string      |
| Provider       | training_provider      | string      |



# Technologies Used

## Languages

1. Html5
2. CSS
3. Javascript
4. Python 

## Libraries and Tools 

1. JQuery
2. Materialize
3. EmailJS (API)
4. Flask
5. Jinja 
6. Mongo DB
7. Google Fonts
8. GitHub
9. GitPod
10. Heroku
11. Font Awesome



# Testing


## Manual testing

Features that were manually tested:

#### Error testing

In testing for errors, test were completed that deliberately aimed to 'break' the functions of the page.  This included carrying out tests
that:

1. Missed out fields when using forms 
2. Searching for incorrect or known words/phrases that were not in the collections
3. Attempting to edit collections without filling out specific fields

All error testing came through without any 'breaks' in the webpage structure or function/navigation.

During manual testing, one error came up during the 'Search' function.  This was a 500 error, where a type error was raised.  This appeared to have no 
impact on the functionality however as the search worked in all tests.  Upon discussion with my Code Institute Mentor, research via Slack and Stack Overflow, it was not
deemed impactful.  Matching code to previous written or learnt 'Search' functions did not seem to also demonstrate any 'code' errors.  
Upon reading the error further through the developer tools, which stated expected string received 'null', led to placing a 'str()' operation into the code.  For example,
the original code reading

```
interventions = list(mongo.db.interventions.find({"$text": {"$search": query}}))
```

and the revised code read (without any subsequent errors)

```
interventions = list(mongo.db.interventions.find({"$text": {"$search": str(query)}}))
```

Upon subsequent testing, no errors have appeared, both when searching for correct and incorrect collection names.

#### Add Interventions/Training
1. Navigate to either the Add Training/Intervention page
2. Fill out all fields in the form
3. Click Submit
4. Navigate to Training/Intervention Page to check addition has been added


#### Edit Interventions/Training
1. Navigate to Training/Interventions page
2. Scroll down to collections 
3. Click on desired collection for collapsible to show
4. Click on Edit button
5. Amend appropriate fields as desired
6. Click on 'submit'
7. Navigate to Training/Intervention Page to check amendments have been added

#### Delete Interventions/Training
1. Follow steps 1 to 3 on above section
2. Click on 'delete' button
3. Navigate to Training/Intervention Page to check correct files delivery_method

#### Search for Interventions
1. Navigate to Interventions page using the Navbar
2. Read the 'search' guide at the top of the page
3. Enter in appropriate search phrase
4. Click search
5. View search results, if no results, try a different phrase
6. If still no results, intervention can be added following previous 'Add..' section

#### Navigate using the Navbar
1. Click on desired items on Navbar
2. Title on each page should reflect the desired page destination


#### Email Contact Form
1. Navigate to Help page using Navbar
2. Scroll to bottom of the page to the Contact Form
3. Fill out all fields and submit
4. Alert will appear indicating if successful or navigation
5. If unsuccessful ensure all required fields have been correctly filled out


## GitHub

From the command line, enter below to view live previews.  This was done to test the different
tools and features of the webpage in conjunction with Google Developer Tools. 
```
python3 app.py 
```

## Heroku

Running the app through Heroku, website was checked for errors using Google Developer tools and the above functionality in order to maintain consistency between platforms.
No discrepencies existed that weren't consistent between sites and subsequently fixed.


## Google Developer Tools
This was used to view the responsiveness of the webpage through the following:
Pixel 2, Pixel XL, iphone 5, SE, 6/7/8 and plus versions, X and ipad and ipad pro.

Google Developer Tools was also used to identify any console errors that appeared throughout page
creation.

## Devices
The app was tested on a range of phsyical devices as well as through the Google Emulator.  These include,
Dell 11inch Laptop, Macbook Pro, Ipad Pro (11inch), iphone 7, 11 and 12, ipad mini (2nd Gen) and Dell
Desktop Computer.

All devices performed as expected, with the app performing consistently with as shown in the
Google Developer tools.  


## Errors

No errors are reported when running the page.  

## Warnings

No warnings present.  

# User testing of User Experiences (UX) 

User testing were as follows:  

* A range of potential users were asked to test the app.  
* These included targeted profesionals of different ages.
* A range of devices were used including, desktops, ipads, phones and laptops (detailed above).

No broken links or errors were reported by users. 

In meeting User Stories, the app performs as below, with pictures accompanying each User Story:

Pictures are located at:


[User Stories](https://github.com/samc85/milestone_3_project/tree/master/images/userstories)



Each picture is labelled to match the appopriate User Story.


User Story 1
* As a user, I wish to be able to find information about the app purpose.

User can find this by navigating to the Home and About pages.

User Story 2
* As a user, I wish to be able to use the site without too many instructions or technical expertise.

User can find this through the use of simple colour scheme and clear navigation links.  The use of dropdowns and 
minimal button options aids this experience as well.  

User Story 3
* As a user, I wish to be able to search for relevant interventions to meet the needs of my students.

User can search for interventions using the search funciton on the page.  

User Story 4
* As a user, I wish to be able to view a range of training courses for myself and my staff

User can navigate to training page to view courses that have been added.

User Story 5
* As a user, I wish to be able to edit what both I have, and others have added to ensure consistency and reliability.

User can navigate to either the interventions/training page and edit existing interventions/training.

User Story 6
* As a user, I wish to be able to delete what I or others have added, to ensure appropriateness.

User can navigate to training/intervention page and delete unwanted collections.

User Story 7
* As a user, I wish to be able to add or edit interventions and training with ease, through simple to use forms

User can naviagte to the add interventions page and add new ones via the add form and navigate to the interventions
page and edit collections using the edit button.

User Story 8
* As a user, I wish to have access to other information sources to inform my choices.

User can navigate to the Home page for further information and also to the footer for external links.





# External Testing

The website was checked through the following Validation service tools, any errors are described within:

### 1.  W3 validator (for HTML)

### 2. CSS Validator (for CSS)
    
CSS Validator flags one Value Error for the Materalize CDN.  Upon checking, the Value Error is consistent with 
    the Materalize CDN links on the webpage.  Details are below:

       *URI : https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css*
    
       *Value Error : letter-spacing only 0 can be a unit. You must put a unit after your number : 0.4*

    

### 3. JSLint (for Javascript)

### 4. JSHint (for Javascript)

### 5. Esprima (for Javascript)


### 6.  Responsive design Mobile friendly test Google

https://search.google.com/test/mobile-friendly?id=zeK6WGGEddR6Yj4lSUtuXw

## Speed

* https://tools.pingdom.com/


## User bugs

No user bugs reported.  
 
# Deployment

## GitHub Pages

### Repository
All code was written on Github using a newly created repository.  This is created by signing up to Github and
creating a New Respository in the user Profile section.

The following tools were added to the repository as detailed below:

Flask

```
pip3 install Flask
```

Python files

```
touch app.py
touch env.py
touch .gitignore
```

The git ignore file should contain the env.py to ensure that secret codes are not shared publicly.  



### Updates

Code was tested through the GitPod platform by entering 'python3 -m http.server' into the console or by clicking
the windown icon in the right hand corner for a in-window view of page code representation.

Using GitHub, HTML, CSS. JavaScript and additional resources were updated via the below process:

In the Command line enter: 
```
git status
```
To give you the names of which files have been modified and require following the below process.
```
git add -A  (or insert appropriate file path here e.g index.html)
```
```
git commit -m '(insert description of update e.g Font style updated to ...)'
```
```
git push  
```

and all changes will be pushed to the repository.  

## Forking the GitHub Repository 

Forking the GitHub Repository creates a copy of the original where another person is able to view and /or make changes without affecting the original repository.  This can be completed through the following steps:

* Log into GitHub and locate the GitHub Repository
* At the top of the Repository locate the "Fork" button.
* Clicking this button will now create a copy of the original repository in one's own GitHub account.

## Local Clone 

If a person wished to make a local clone, the following steps should be followed:

* Log into GitHub and locate the GitHub Repository.
* Under the repository name, click "Clone or Download"
* To clone the repository using HTTPS, under "Clone with HTTPS" copy this link.
* Open Git Bash
* Change the current working directory to the location upon which you want the cloned directory to be made.
* Type 'git clone', and then paste the URL previously copied e.g:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-Repository
```

* Press enter and your local clone will be created.  



## Heroku

1. Create a requirements.txt file by typing into the terminal line:

```
pip3 freeze --local > requirements.txt
```



2. Create a Procfile by typing 

```
echo web: python app.py > Procfile.
```

3. *Add*, *commit* and *push* these changes to Github, followng steps above.

4. Navigate to the www.heroku.com

5. Create new app and give it a unique name.

6. Choose the *region* that is closest to you.

7. Go to the *Deploy* tab and choose *Github*.

8. Search for the desired repository and connect.

9. Go to Heroku *Settings* and navigate to *Config Vars*.

10. Set the following as below:

```
IP = 0.0.0.0
MONGO_DBNAME = [Name of MongoDB]
MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT = 5000
SECRET_KEY = [Secret key]
```
Go to the Deploy tab and Deploy Branch, ensuring that the master branch is selected.

11. On the Heroku project page (make sure you are on the correct project) click on 'open app' on
the top right.  Ensure you have saved and pushed your recent changes on GitHub as this will only 
deploy the most recent version.

# API's


### EmailJS API

The below link gives the appropriate steps for creating an EmailJS API key.

https://www.emailjs.com/docs/

Further instruction is included within the following link:

https://www.emailjs.com/docs/tutorial/overview/

and explanation of how emailJS works is linked below:

https://www.emailjs.com/docs/introduction/how-does-emailjs-work/


## Credits

* https://www.w3schools.com/   was used as a point of reference

* Code Institute Course resources were used to revise/check back as a point of reference

* Code for HTML, CSS and Javascript was beautified using HTML, CSS and Javascript Formatters.

* Support with writing code referenced the following additional websites:

    https://www.codeacademy.com

    BrowserStack for Code queries

    Code Institute Slack Channel

* APIs were sourced form the following pages

    https://www.emailjs.com/


 
## Content

### Text 

Text was written by myself.

### Media

http://techsini.com/multi-mockup/



