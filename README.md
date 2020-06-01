
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
![register page](https://i.ibb.co/71xPw43/register.png)
Part of registration process will be to verify the email used for signing up, where users will be directed to this page:
![verify email](https://i.ibb.co/RD1T8Kz/verify-email-1.png)
Once the user obtains the link from mail sent to their email, they'll be able to verify it, and then be successfully registered. A useful message under the navbar indicates that a confirmation email has been sent to the email provided in the sign up form.
