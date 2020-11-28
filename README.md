

![responsive image]()

# SLCN Library
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

Wireframes are generally true to the webpage. 

---------  COMPLETE -------

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


### Manual testing

Features that were manually tested:

* Add Interventions/Training
1. Navigate to either the Add Training/Intervention page
2. Fill out all fields in the form
3. Click Submit
4. Navigate to Training/Intervention Page to check addition has been added

* Edit Interventions/Training
1. Navigate to Training/Interventions page
2. Scroll down to collections 
3. Click on desired collection for collapsible to show
4. Click on Edit button
5. Amend appropriate fields as desired
6. Click on 'submit'
7. Navigate to Training/Intervention Page to check amendments have been added



### GitHub

Running 'python3 app.py' from the command line, live previews were used to manually test
different features and functions within Git.   

### Heroku

Running the app through Heroku, 

**Google Developer Tools**
This was used to view the responsiveness of the webpage through the following:
Pixel 2, Pixel XL, iphone 5, SE, 6/7/8 and plus versions, X and ipad and ipad pro.  

## Errors

No errors are reported when running the page.  

## Warnings

## User testing of User Experiences (UX) 



## External Testing

The website was checked through the following Validation service tools:

### W3 validator (for HTML)

### CSS Validator (for CSS)

### JSLint (for Javascript)

### JSHint (for Javascript)

### Esprima (for Javascript)


### Responsive design Mobile friendly test Google

https://search.google.com/test/mobile-friendly?id=zeK6WGGEddR6Yj4lSUtuXw



## User Testing


## Speed

* https://tools.pingdom.com/


## User bugs

No user bugs reported.  
 
# Deployment

## GitHub Pages

## Herokue 





### Repository
All code was written on Github using a newly created repository.


### Updates

Code was tested through the GitPod platform by entering 'python3 -m http.server' into the console or by clicking
the windown icon in the right hand corner for a in-window view of page code representation.

Using GitHub, HTML, CSS. JavaScript and additional resources were updated via the below process:

In the Command line enter: 
```
git Status
```
To give you the names of which files have been modified and require following the below process.
```
git add (insert appropriate file path here e.g index.html)
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


## API's


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



* APIs were sourced form the following pages



https://www.emailjs.com/


 
## Content

### Text 

Text was written by myself and proofread by known Lake District residents.

### Media

http://techsini.com/multi-mockup/

## Acknowledgements 

