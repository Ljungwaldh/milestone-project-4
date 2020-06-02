
# Gamestarter
[Gamestarter](https://ljungwaldh-gamestarter.herokuapp.com/) is a website dedicated to helping aspiring game developers to kick-start their ideas through crowdfunding - be it an interesting new mod for an existing game, or in creating their own full-length video game. The website is designed to be a simple donation platform, where users signing up normally can contribute to video game project that they feel are interesting and worth investing in. On the other hand, signing in as a creator allows budding game developers to get their ideas out on to the platform so that they can start to receive donations from potential fans. In the first release of the website, the experience is designed to be simple, easy to navigate, and to be a seamless donation experience with minimal form filling required. This is mainly aimed towards developers of video games and towards video game enthusiasts.

## UX
### Goals
#### Visitor Goals
The main target audience for Gamestarter is:

 - Video game enthusiasts, especially those who enjoy/seek new experiences
 - English speaking
 - Video game developers, be it an individual or a small video games studio
 - People who are comfortable to donate to projects related to their hobbies
 - People who want to feel part of the process in building potentially great ideas

User goals are:

 - Find a new game/game mod that piques their interest
 - Donate to projects they find interesting
 - Be able to keep up to date with latest developments with one or a number of projects
 - For creators, being able to easily set up their project on the platform so that crowdfunding can be initiated quickly
 - For creators, being able to receive donations as a result of their efforts in communicating an interesting project, via the project's details, through the blog and potentially any rewards they wish to promise to donors

Gamestarter is a great way to address these needs/goals because:

 - Signing-up and getting started as a creator is seamless and requires minimal effort to place project details on the platform, allowing more time for developers to actually developer and try to deliver what donors want
 - Being able to contribute to projects of interest to the user is a smooth and efficient experience too, with minimal amount of clicks to be able to confirm a donation to a given project

#### Business Goals
The goals of the Gamestarter platform include:

 - To become a trusted partner of business accelerators and start-up hubs, where the platform can act as an initial stage of funding and barometer for interest in a given video game/video game project
 - As the platform grows, having the aim to be able to take a small amount of commission per donation as a means to ensure that the crowdfunding experience continues to improve
 - With growth in number of users can the opportunity also open up to advertise relevant merchandise by retailers/sellers (eg. video game consoles, accessories, gaming furniture etc.)
 - Become a hub for great ideas revolving around video game development

### User Stories

1.  As a new visitor to the website, I want it to be clear upon landing on the home page as to what the website's purpose is
2. As a new visitor to the website, I want to be able to sign up and log in efficiently
3.  As a new user, I want to be able to get an idea of who the game developer is, a preview of what is being developed and understand how the donation concept works
4.  As a new user/potential donor, I want to be well informed about the different amounts I can donate to a project
5.  As a user, I want to be able to read content made by the game developer(s) in regards to the progress of the game development
6. As a user, I want to be able to comment on blog posts from a game project in order to feel part of the process and community
7.  As a user, I want to be able to contribute directly to the development of the game(s) via polls, having the chance to write my own ideas in a dedicated section (eg. ideas for the story/storytelling, game level design etc.)
8. As a new user/creator, I want a seamless experience in terms of setting up my game project on the platform
9. As a creator, I want to be able to manage my game projects, including adding, updating and deleting a project of mine as I see fit
10. As a user, I want to be able to have a seamless experience for donating to a given project, with as few clicks required to execute a donation, where only essential details (eg. card details) are required of me to complete a transaction
11. As a user, I want to be able to get in touch with the developer of the website
12. As a user, I want to be able to get an overview of my previous donations
13. As a creator, I want to be able to get an overview of the game projects I currently have up on Gamestarter 

### Design Choices
#### Fonts
For choosing the fonts, I took inspiration from [this article](https://themeisle.com/blog/best-google-fonts/) for the body text and headers lower in hierarchy of `<h1>`. 
For body test, the developer chose **Roboto**, as this is the most used Google font for blogging purposes - this being a clear font for reading purposes. 
Secondly, Inconsolata font was used for header tags `<h2>` to `<h6>`, this font popular in the technology world and thus felt appropriate for a website focused towards video games and developers. 
Lastly, the `<h1>` font choice of **Press Start 2P** was more of a personal choice by the Developer in terms of a main logo font, again giving off a tech/video game theme,
 this being found when the developer scrolled through Google Fonts library.

 #### Colours
I used the following colour scheme, that was influenced by starting off with the blue colour from Bootstrap's `btn-primary` styling and then utilising other colours to provide contrast in places where it made sense (eg. orange used to grab the user's attention towards certain elements)
![gamestarter colour scheme](https://i.ibb.co/L1YbSJt/color-scheme-gamestarter.png)
A simple colour scheme was chosen to provide a clean appearance for users where information will be easy to consume, since the greatest value from this website will be the content provided by users. The developer used [Coolors](https://coolors.co/) to generate this colour scheme.

#### General Styling
Majority of content, when displaying a number of objects, are presented on cards in sets of three, which subsequently stack on one another when on smaller screen devices. For pages that focus on one particular object/project/order, information is presented with the image on the left-hand-side and relevant information displayed on the right-hand-side. The general backdrop is white, aiming for simplicity, with the coloured buttons to help indicated calls-to-action/points of navigation through the website.

## Background: Development Process
This section is dedicated to giving readers some context about how the project idea had changed a number of times, initially increasing in complexity and subsequently decreasing in complexity due to time constraints in regards to the Code Institute project deadline. **User Stories** have also changed over time as a result, and the ones described in the previous section reflect the latest ones formulated. This is to ensure testing of user stories can reflect the end product. This section will also include **Wireframes**, providing the genuine, first mockups created for the project.

#### Original Idea: Patreon website for One Video Games Studio
This idea was initiated from the wireframes initially created by the developer when the project began. The aim was to provide what would be a patreon-type website for a single video games studio (for reference on what is meant by patreon, check out this [website](https://www.patreon.com/). The studio would have a subscription-based model, and depending on the type of subscription a user has signed up for, would provide access to different types on content/user functionality.

##### Wireframes
These Wireframes were created by using [Baslamiq](https://balsamiq.com/) as part of the planning process.

Register:
![register page](https://i.ibb.co/9p5NZtL/register.png)

Login:
![login](https://i.ibb.co/tbxd4fT/sign-in.png)

Landing page:
![landing page](https://i.ibb.co/C6Z3PJ4/landing-page.png)

Profile page:
![profile page](https://i.ibb.co/pWw1LTq/profile.png)

Blog:
![blog](https://i.ibb.co/1M2xCxg/blog.png)

Ideas Board (for Premium users):
![ideas board](https://i.ibb.co/HGmFxDX/ideas-board.png)

#### Idea Iteration 1 Patreon copy but for Video Game Projects
The developer would push towards the challenge of not only just allowing users to become patrons of one games studio, but to try and create a simple replica of Patreon, however having more of a focus towards video game production/projects that can receive donations. In this step, the documentation to best describe the thinking behind this idea, at the time, is the following data schema:
![enter image description here](https://i.ibb.co/k6F4bNW/Ljungwaldh-Milestone-4-Initial-Data-schema.png)
Users would be able to sign up as normal users or as Creators. Normal users would be able to:

 - Subscribe to game projects, and depending on the tier they subscribe to, would be able to access certain blog content of that project
 - Comment on blog posts they have access to, creating a community around a given game project(s)

Those signing up as Creators would be able to:

 - Create the game project(s) they wish to list up on the platofrm
 - Define the subscription pricing and rewards through the subscription descriptions
 - Create blog content for a given game project and assign, if they wish to, tier tags to content so that certain subscriptions types would have access to certain types of content

#### Idea Iteration 2: Donation platform with one-time payments
The developer assessed the added complexity required in order to set up subscriptions with the Stripe payment system and decided,
in the end, against implementing a subscription-based payment model. This came as a result of an update by Stripe on how to set up subscriptions,
part of this involving having to set up a real business account in their platform for a user's account. 
It was also concluded that the complexity of allowing Creators to decide their own prices would require a significant amount of time added to the project scope (that would go beyond the deadline).
Therefore, the developer opted to pre-define the donation prices in order to simplify and be able to create a proof-of-concept in time for the project's time scope. The following data schema can help describe the idea iteration in the form of the data models:
![idea 3 data schema](https://i.ibb.co/jZ6KCv7/Ljungwaldh-Milestone-4-Project-Second-Data-schema.png)

#### Idea Iteration 3: Blog and Commenting functionality removed
The developer opted to remove the Blog and Comment functionality of the donation platform as there was not enough time to implement these features. These features were assessed as non-critical for the project scope and in the first release of this website, and could instead be placed in the pipeline for future features to develop. The final data schema illustrating this, as a result, appears accordingly:
![final idea data schema](https://i.ibb.co/dpR3Cb6/Ljungwaldh-Milestone-4-Final-Data-schema.png)

This data schema best represents the final product on a high level, where screenshots will be provided in the **Features** sections. The data schema will be discussed in further detail in the **Information Architecture** section.

## Features
### Existing Features
#### Features present on every page
**Navbar**:

 - Simple navbar that presents two items when a new visitor enters the website that isn't logged in, these being 'Register and 'Login'. If logged in, options shown are 'My Profile', 'Logout' and 'Find Game Projects'. The 'Gamestarter' icon in the navbar will always redirect to the landing page.
![navbar large screen](https://i.ibb.co/QKZ4XBX/navbar-large-screen.png)
 - Navbar, on smaller devices, switches the navbar items as items within a dropdown, with the dropdown button displayed as a burger icon.
![navbar small screen](https://i.ibb.co/kQmnf3d/navbar-small-screen.png)

**Footer**:

 - Simple Footer with same colour as navbar for consistency. includes copyright information and an email of the website owner
 - Social media icons included as well for further channels of communication/content related to the website
![Footer](https://i.ibb.co/V2sD5nm/footer.png)

**Messages**

 - Helpful messages appear just below the navbar upon certain actions being completed (be it if the user has logged in, if they don't have access to a certain link, if a project has been successfully created/edited etc.). Examples of this can be seen in a number of screenshots below for other features.

#### Landing Page
**Jumbotron Header with Logo**

 - Simple header with Logo to instantly engage visitors as to the
   website they have reached
 - 'Learn More' call-to-action leads to information section lower down

**Introduction and website pitch**

 - Three separate short paragraphs with accompanying images to help introduce and draw in new visitors

**Information Section - What is Gamestarter and How it Works**

 - Two separate Headings with three content boxes underneath each one. The first three boxes look to explain what Gamestarter is in terms of its Purpose, Goal, and what it is in practical terms. 
 - Seconding heading 'How it Works' has the first two boxes hyperlinked to relevant locations for the content (eg. 'Want to Contribute?' directing to 'Find Game Projects' in order to get a user directly to projects they can donate towards, if logged in). 
 - Hover effect on the boxes to give an appealing visual effect and subtle user feedback on what they are currently focused on

**Testimonial Section**

 - Total of three testimonials in a sliding carousel, each with a profile picture and a short text giving a positive review of Gamestarter
![landing page 1](https://i.ibb.co/MBK1hgg/landing-page-1.png)
![landing page 2](https://i.ibb.co/dJ7M4wD/landing-page-2.png)
![landing page 3](https://i.ibb.co/X20c4pb/landing-page-3.png)
![landing page 4](https://i.ibb.co/VCsjSTY/landing-page-4.png)

#### Register page

 - Simple signup form where users enter in their email address, choose and username and password, and check the checkbox if the user wishes to signup as a Creator
 - Foundation of the form is from [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html), while the checkbox for signing up as a Creator is a custom addition to the signup form
 - Allauth provides built-in functionality to give user feedback on security measures, one being to ask the user for another password if it is too similar to the username and/or email provided
![register page](https://i.ibb.co/71xPw43/register.png)

Part of registration process will be to verify the email used for signing up, where users will be directed to this page:

![verify email](https://i.ibb.co/RD1T8Kz/verify-email-1.png)

Once the user obtains the link from mail sent to their email, they'll be able to verify it, and then be successfully registered. A useful message under the navbar indicates that a confirmation email has been sent to the email provided in the sign up form.

#### Login page

 - Login page where users log in with their Username or email, followed by their password
 - Allauth provides built-in feedback on incorrect credentials
![login page](https://i.ibb.co/bJdLQFz/login.png)

#### Profile page

 - Differs depending on if the user signs up as a creator or not. Normal users get one dashboard for previous donations made. Creators will have two dashboards, one for donation history and the other for game projects they've added to the platform that are currently running
 - A 'Load More' button is present for each dashboard, loading more items if they exist, loading three items at a time. This button has a hover effect to give subtle user feedback, informing users this is interactive
 - Each donation/game project item card includes a 'Project Detail' button sop that users can redirect to a page that gives further description of the project
 - Each donation item card gives a short summary, including project title, project image (if applicable), donation type, when the donation was made, and how much was donated
 - Each game project item card (for creator profiles) includes a summary that includes project title, project image (if applicable), and the sum of donations made for the project.

Normal Profile page:
![normal profile](https://i.ibb.co/Rjps8ZD/normal-profile.png)

Creator Profile page:
![creator profile 1](https://i.ibb.co/Y0ssbcH/creator-profile-1.png)
![creator profile 2](https://i.ibb.co/mtgtGrp/creator-profile-2.png)

#### Game Projects
**All Projects page**
The 'Game Projects' option in the navbar will bring users to a repository of all game projects listed on the platform at a given time. 

 - Projects will be presented in three's on larger screens, while on
   smaller screens they will stack on top of each other 
 - Two buttons will be present at the top of the page to to switch
   presentation of projects in a grid view or in a list view
 - A search bar is made available for users to be able to search   
   through game projects, where key words will filter through the   
   title, owner and descriptions of the game projects
 - Each project card will include details such as title, owner, and the
   total amount of donations the project has managed to collect

![all projects grid view](https://i.ibb.co/jTcBhC6/all-projects-1.png)
![all projects list view](https://i.ibb.co/R4773V8/all-projects-2.png)

**Project Detail page**

 - Normal user view will display details of a project when a user clicks on the 'Project Detail' button on a given project card. These details include the title, image (if applicable), owner, sum of donations collected so far, project description
 - Users who are not the owners of the project will be presented with 3 donation options: Basic, Pro, and Premium, with their respective amounts (Note: this labelling/tiers of donation types may hold little relevance for the first release of the website, but will act as a tier for a blog feature in the future)

![non-owner project details](https://i.ibb.co/Kxb1Rsp/project-detail-1.png)

 - If the user is the owner of the page, no donation options will be made available but rather two buttons will be made available: to Update or to Delete the project

![project owner project details](https://i.ibb.co/GJfH8wb/project-detail-2.png)

**Add/Edit/Delete Project (For Project Creator)**

 - These functions are available for users who are the owner of a given project. While all users can read details on any project, Creator users are able to add, edit, and delete their projects
 - For add and edit pages, the user is presented with a form for filling in the title, description, and being able to attach a cover image if the Creator user wishes to. Title and description are required fields while the image attachment is optional, and if no image is attached, a default image will be attached to the project that indicates visually that no image has been attached
 - For the delete functionality, this will provide a Creator user to delete the project from the platform repository. The user gets a notification at the top of the page alerting this, as well as being redirected to the 'All Projects' page

Add Project:

![add project page](https://i.ibb.co/3hkm59s/add-project.png)

Edit Project:

![edit project page](https://i.ibb.co/HnXnmNW/edit-project.png)

Delete Project: 

![delete project function](https://i.ibb.co/rvP5gW9/delete-project.png)

#### Checkout
**Checkout page**

 - Once a user selects a donation type from a 'Project Detail' page, they are redirected to a checkout page
 - The page presents a summary of what the user is donating towards and how much, followed by a field for filling out card details (this element constructed from implementing the [Stripe payment system](https://stripe.com/docs/payments/checkout/accept-a-payment))
 - User is given feedback is card details entered are invalid in any way (be it invalid card number, CVC, and/or expiration date)
 - Once the user submits/confirms the donation with valid card details, a loading overlay is presented over the page to indicate that the payment is being processed

![checkout page](https://i.ibb.co/NFHFnQr/checkout-1.png)

![checkout overlay payment processing](https://i.ibb.co/M8c52n1/checkout-2.png)

**Checkout Success page**

 - If the transaction is successful, the user is redirected to a 'checkout success'
 - The page includes details of the project donated towards, a thank you message, and an order number to indicate that the donation has been recorded
 - Below donation details includes information informing users of a future feature, this being email confirmation of donations, which at the time of writing, isn't implemented yet. The text helps to indicate that should users wish to obtain a confirmation via email, they can get in touch with the website's owner via the provided email address

![checkout success page](https://i.ibb.co/DD4c9QN/checkout-success.png)

### Features Left to Implement

 1. **Blog app**: Blog functionality where game projects can have their dedicated blogs to update donors/fans of the progress on the project/development. This feature would also include commenting functionality for donors, and creators of the game projects could define what content is available to which type of users (based on amount a user has donated, what donation type a donor has paid for etc.)
 2. **Sign-in/Create account via Social Media**: Giving users/new visitors the option to sign up and/or login with their social media accounts (eg. Facebook, Google)
 3. **Stripe Webhooks on Payments**: For the developer to add increased security that would give the website more real-world application, webhooks would be necessary in order to confirm, in the back-end, the status of the user's payment. Also, this would help to alleviate the issue/rare event of a user exiting the page before the transaction was complete, so that the order can be created if it was successful
 4. **Subscription Payment Model**: If the developer decides to keep the donation tiers as ever-present in the future, turning the payments model to a subscription basis would make more sense from a user experience perspective. This would help Creator users define who has access to which types of content in a blog depending on the subscription type. Since implementing subscriptions via Stripe cannot be done with signing up an actual business account on Stripe, this would be a feature to implement should the developer decide to deploy the website on a web domain and deliver it as a real world application/platform
 5. **Email confirmation of Donations/Orders**: Having the added feature of confirmation emails, when a user makes a donation, would improve user experience by giving them transaction documentation in a place where users would usually like to have it - in their email inbox
6. **Let Creator Users define their Pricing, Donation tiers and Rewards**: Allowing Creators to define what tiers and pricing of donations they want for their respective projects could help Creators to personalise their business models more, being able to potentially define their own rewards that come with the pricing they set. This can add some advanced complexity when working with the Stripe Payment system, especially with subscription models, when trying to set dynamic pricing that Creator users can define. This would involve considerable research and time for development to make this a reality - most likely for a real-world release of the platform

## Information Architecture
### Database Choice

-   As a framework Django works with SQL databases. During development locally machine the developer worked with the standard  **sqlite3**  database installed with Django.
-   On deployment, the SQL database provided by Heroku is a  **PostgreSQL**  database.

### Data Models
The Class Meta for each model was defined with `pass`. Since there hasn't been a need to use Meta class for the models, this is defined in this manner to satisfy PEP8 requirements.

#### User (django-allauth)
The User model utilised for this project is the standard one provided by `django.contrib.auth.models`. Using this model helps to add, along with **django-allauth** functionality, a lot of built-in tools to help with creating the registration and login pages and user authentication.

#### Profile app model
Within the `profiles` app, the **Profile** model holds all the data needed for user profiles. The model utilises the User model to add allauth functionality

**Profile Model**
| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | on_delete=models.CASCADE | OneToOneField(User)
Is Creator | is_creator | default=False, null=True, blank=True | BooleanField

 - Profile is created via the sign-up form - this form having the custom field of `is_creator` in order for a new user to have a choice of which user type to sign up as. This is key to have in order to implement the idea of what the website is meant to be and how it will fundamentally function (eg. some users will want to just follow/contribute, others will want to post projects up for receiving donations)

#### Gameproject app models
Inside the `gameproject` app lies two models, a `GameProject` model and `Donation` model.

**GameProject model**
| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=50 | CharField
Description | description | None | TextField
Owner | owner | null=True, blank=True, on_delete=models.SET_NULL | ForeignKey(Profile)
Created at | created_at | blank=False, null=False, default=timezone.now | DateTimeField
Image | image | upload_to='images/', null=True, blank=True | ImageField

 - 'Created at' field utilises `timezone` from `django.utils` to set time and date on when the object is created
 - Images are stored using Pillow to store all image files in an AWS S3 bucket

**Donation model**
| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=50 | CharField
Description | description | None | TextField
Amount | amount | max_digits=6, decimal_places=2 | DecimalField
Game Project | game_project | null=True, blank=True, on_delete=models.CASCADE | ForeignKey(GameProject)

 - The data for this model, unlike the others, is required to be predefine in the admin panel as part of getting the website to function properly. The developer defines 3 objects/donation items (this being recommended should another developer want to run this project locally)

#### Checkout app model
Within the `checkout` app lies one model - the `Order` model.

**Order model**
| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | user | null=True, blank=True, on_delete=models.SET_NULL, related_name='donations' | ForeignKey(Profile)
Donation Item | donation_item | null=True, blank=True, on_delete=models.CASCADE | ForeignKey(Donation)
Stripe Payment Intent ID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField
Game Project | game_project | null=True, blank=True, on_delete=models.CASCADE | ForeignKey(GameProject)
Created at | created_at | blank=False, null=False, default=timezone.now | DateTimeField
Status | status | max_length=2, choices=STATUS, default='PE' | CharField
Order Number | order_number | max_length=32, null=False, editable=False | CharField

 - Status choices are defined in the Order model - this being used to define if a payment is 'pending' or 'paid'
 - Order number is generated from a function for the order Model, utilising the `uuid` import
 - Stripe Payment Intent ID is provided by Stripe's elements and functionality to indicate when a client wish to send a certain payment through the payment system

## Technologies Used
### Tools
- [Gitpod](https://www.gitpod.io/) is the IDE used for developing this project. 
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) to provide built-in user authentication functionality.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) to measure code coverage of python unittests.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to allows the web app to serve its own static files.
- [Imgbb](https://imgbb.com) to store external images for this project that were not entered into the database.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- Heroku for deployment
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.
- [Coolors](https://coolors.co/) to help define the colour scheme for the website
- [LucidChart](https://www.lucidchart.com/pages/) to create data schemas as part of the planning phase of the project

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for Gamestarter donation platform
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

## Testing
Testing is described in a separate [TESTING.md](TESTING.md) file.

## Deployment

### How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    - Google's [Gmail](https://www.google.com/gmail/)  for setting up email function (be sure to enable 2 step verification to be able to create an app password, relevant for when deploying the project)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

#### Instructions
1. Save a copy of the github repository located at https://github.com/Ljungwaldh/milestone-project-4 by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
    ```
    git clone https://github.com/Ljungwaldh/milestone-project-4
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, the developer recommends using Pythons built in virtual environment. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

    - If using Gitpod, you'll be able to set up environment variables in the Settings tab under your account. Do not forget to restart your workspace to activate your environment variables or your code will not be able to see them: 

        "DEVELOPMENT": True,
        "SECRET_KEY": (enter key here)
        "STRIPE_SECRET": (enter key here)
        "STRIPE_PUBLIC_KEY": (enter key here)
        "STRIPE_SECRET_KEY": (enter key here)
        "AWS_ACCESS_KEY_ID": (enter key here)
        "AWS_SECRET_ACCESS_KEY": (enter key here)
        "AWS_STORAGE_BUCKET_NAME": (enter bucket name here)

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

11. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the url. Here log in with your superuser account and create Donation items/tiers (recommended 3) within the new database.

13. Once instances of these items exist in your database your local site will run as expected.

### Heroku Deployment

To deploy the Gamestarter platform to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your AWS access key>`
AWS_SECRET_ACCESS_KEY | `<your AWS secret key>`
DATABASE_URL | `<your postgres database url>`
DISABLE_COLLECTSTATIC | `1`
EMAIL_HOST_PASS | `<your app password generated from your google account, from GMail Advanced Settings -> 'Security'>`
EMAIL_HOST_USER | `<your GMail email address>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY | `<your Stripe public key>`
STRIPE_SECRET_KEY | `<your Stripe secret key>`
USE_AWS | `True`

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url. Here log in with your superuser account and create Donation items/tiers (recommended 3) within the new database.

12. Once instances of these items exist in your database your heroku site will run as expected.

## Credits

 - [Boutique Ado Mini Project](https://github.com/ckz8780/boutique_ado_v1) by [ckz8780](https://github.com/ckz8780) (Chris Zielinski), as part of
   Code Institute learning material providing guidance on how to set up
   a Django project, the fundamentals of working with the Django
   framework, setting up Stripe, setting up email functionality, and
   Django allauth. The mini project provided a great foundation to be
   able to develop this project
   
 - [One Page Wonder theme](https://github.com/BlackrockDigital/startbootstrap-one-page-wonder/blob/master/index.html) from Start Boostrap used as inspiration to build part of the frontend of the landing page, this being the welcome section
 - In terms of a README to follow a good example of and get inspiration from, the developer used this [Github Repository,](https://github.com/AJGreaves/thehouseofmouse) the README and TESTING files as a guide for writing the README and TESTING files for this project. Credits for the repository go to [AJGreaves on Github](https://github.com/AJGreaves)
 - [Heroic Features template](https://github.com/BlackrockDigital/startbootstrap-heroic-features) from Start Boostrap providing inspiration for the heading of my landing page, where in the end the developer opted for a simple jumbotron with the logo and a call-to-action button
 - [Patreon](https://www.patreon.com/home) and the profile/home page (when logged in) provided inspiration for how the Profile page would looked to be set up, focusing towards dashboards
 - 'What Is Gamestarter' and 'How It works' sections in landing page inspired by using this [code snippet](https://bootsnipp.com/snippets/vN7kb) from Bootsnipp by [nahian91](https://bootsnipp.com/nahian91 "Bootstrap snippets by nahian91")
 - This [article](https://medium.com/@gavinwiener/modifying-django-allauth-forms-6eb19e77ef56) from Medium providing guidance on how to customise Django Allauth forms, which was done on the registration form. Article written by [Gavin Wiener](https://medium.com/@gavinwiener)
 - [Kickstarter](https://www.kickstarter.com/) providing inspiration on how a checkout for a donation platform can look like - this focusing on minimalism and users filling in only what is essential for payment (card details)
 - This [code snippet](https://bootsnipp.com/snippets/xbaoX) from Bootsnipp providing inspiration for creating Testmonial carousel for the landing page. Code snippet made by [sangrai](https://bootsnipp.com/sangrai "Bootstrap snippets by sangrai")
 - [Tutorial on LearnDjango](https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial) assisting the developer to set up an image field for the GameProject model, as well as how users would be able to upload images
 - Set up for displaying card items in both the 'profile' and 'all game projects' pages inspired by this [code snippet](https://bootsnipp.com/snippets/M515A). Code snippet made by [noemer](https://bootsnipp.com/noemer "Bootstrap snippets by noemer")
 - 'Load More' button (HTML, CSS and JQuery) provided on the 'profile' page for both donations and game project dashboards inspired by this [code snippet](https://codepen.io/elmahdim/pen/sGkvH) from CodePen. Code snippet made by [Mahmoud Elmahdi](https://codepen.io/elmahdim)
 - Donation options that appear on a 'project detail' page inspired by this [code snippet](https://bootsnipp.com/snippets/kleWM) from Bootsnipp. Code snippet was made by [vsantiago113](https://bootsnipp.com/vsantiago113 "Bootstrap snippets by vsantiago113")
 - Set up previous donations made on 'profile' page to be displayed from most recently made going downwards for older donations. Being able to manipulate data from views.py to be displayed in a certain order was possible through this [Stack Overflow forum](https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending). Credit for the answer goes to [Keith](https://stackoverflow.com/users/1215645/keith) on Stack Overflow
 - A number of images from Pexels.com provided some static images used for the landing page, these including:
	 - [Teenager playing video games](https://www.pexels.com/photo/joyful-teenager-playing-video-game-on-tv-console-3853909/) by Andrea Piacquadio
	 - [Black and white video game controller](https://www.pexels.com/photo/white-and-black-game-controller-989939/) by FOX 
	 - [Man working on Apple computer](https://www.pexels.com/photo/adult-apple-device-business-code-340152/) by hitesh choudhary
	 - [Man smiling by wall](https://www.pexels.com/photo/adult-beard-boy-casual-220453/) by Pixabay
	 - [Woman in the city, winter](https://www.pexels.com/photo/adult-beautiful-blonde-blur-324658/) by freestocks.org
	 - [Smiling man by the beach](https://www.pexels.com/photo/man-wearing-black-zip-up-jacket-near-beach-smiling-at-the-photo-736716/) by Tim Savage

## Acknowledgements

 - I would like to thank my tutors at Code Institute, especially Xavier Astor, Kevin Loughrey and Chris Zielinski for guiding and teaching me how to create a Django application
 - I would like to thank my mentor Anthony Ngene for his ongoing support, guidance, and the challenges he sets me to produce the best possible projects that I can produce
 - I would like to give a huge thanks to friends and family who have provided moral support throughout the whole process