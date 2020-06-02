# Gamestarter - Testing Details
## Automated Testing

### Validation Services

The following validation services and linter were used to check the validity of the website code.

-   [W3C Markup Validation](https://validator.w3.org/)  was used to validate HTML.
	- Only errors to appear related to forgetting to add `alt=''` attribute and description to the images used for the landing page testimonial carousel. This was promptly fixed, where descriptions were provided on the images should they fail to load on the page
    
-   [W3C CSS validation](https://jigsaw.w3.org/css-validator/)  was used to validate CSS.
    
-   [JSHint](https://jshint.com/)  was used to validate JavaScript.
    
    -   To save on loading times and to keep my JavaScript code organized I chose to break up the JS into several separate files
    - Stripe in this checkout app javascript file was highlighted as an 'undefined variable'. Since this variable is part of the Stripe payment setup, this single issue brought up by JSHint could be ignored as it cannot consider the external dependency during the validation
    -  [Pylint-django](https://pypi.org/project/pylint-django/)  was used to validate Python.
    

**IMPORTANT**

If you wish to run any of these tests for yourself, before going further please make sure you have already cloned this project from the  [milestone-project-4 repository](https://github.com/Ljungwaldh/milestone-project-4)  by following the steps in the  [README.md]([https://github.com/Ljungwaldh/milestone-project-4/blob/master/README.md](https://github.com/Ljungwaldh/milestone-project-4/blob/master/README.md)#how-to-run-this-project-locally)  under "How to run this project locally" and that you have the entire project running on your own IDE.

### Python Testing

#### How to run Python tests

To run the existing Python tests:

1.  Activate your virtual environment.
2.  In the terminal enter the following command:

```
python manage.py test

```

3.  If you wish to run the tests within a specific app only you can specify with:

```
python manage.py test <app name here>

```

4.  The test results will be shown within the terminal.

_NOTE: The  `python`  part of these commands assumes you are working with a windows operating system. Your Python command may differ, such as  `python3`  or  `py`_

### Coverage

[Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/)  was used to provide feedback during testing to check that enough of my code had been tested.

#### How to run coverage

1.  Activate your virtual environment.
2.  In the terminal enter the following command:

```
coverage html

```

3.  Open the newly created  `htmlcov`  directory in the root of your project folder.
4.  Open the  `index.html`  file inside it.
5.  Run the file in the browser to see the output.

### Test-Driven Development
The developer managed to achieve some degree of test-driven development, attempting to write automated tests after an app had been mostly/fully developed (please see the commit history for evidence of the test-driven development done. In setting up the automated tests for each app, a test file would be created for each `views.py`, `forms.py` and `models.py` files in the respective apps.
Below is the resulting coverage html file rendered in the browser:
![coverage html report for testing](https://i.ibb.co/hXmPmKY/coverage-html-testing.png)

Total coverage achieved for the whole application was 71%. Due to time constraints there have been areas that could've been expanded further (especially in the `views.py` files of `profiles`, `gameproject` and `checkout` apps. Since it was also the first time the developer was applying test-driven development and writing automated tests, the developer's knowledge and experience prevented him from being able to write more advanced tests and to aim for higher coverage. To make up for this, thorough manual testing has also been done to compliment the automated tests.

## User Stories Testing
In this section, testing is done on the user stories described in the **UX** section of the README file. These tests are done to see how well the final application meets the needs of users.

**1.  As a new visitor to the website, I want it to be clear upon landing on the home page as to what the website's purpose is**
The landing page looks to make sure that any new visitors are as well-informed as possible as to what the website is, what it's purpose is, and how it works. This is all done through the welcome pieces of text, followed by the Information section and Testimonials

**2. As a new visitor to the website, I want to be able to sign up and log in efficiently**
Simple and easy-to-fill-out forms are provided on both Register on Login pages. With the allauth feature for verifying emails as part of registration, this could be seen as a step that makes it slow. However, this helps to ensure secure registration of users.

**3.  As a new user, I want to be able to get an idea of who the game developer is, a preview of what is being developed and understand how the donation concept works**
In the first release of the website, elaborate profiles describing users/game developers more personally are not present, and neither a blog feature for developers/Creator users to provide more content. These are features to be introduced in a future release of the website. For now, users can get a summary of game projects, who owns them, and be able to learn more about projects through their descriptions

**4.  As a new user/potential donor, I want to be well informed about the different amounts I can donate to a project**
When a user accesses a project's details (providing they are not the project owner), they are clearly provided the donation options below the project details

**5.  As a user, I want to be able to read content made by the game developer(s) in regards to the progress of the game development**
Since the blog feature could not be implemented in time for the first release of this website, this user story could not be satisfied.

**6. As a user, I want to be able to comment on blog posts from a game project in order to feel part of the process and community**
For the same reasoning as user stories 3 and 5, this user story could not be fulfilled in the first release of this website

**7.  As a user, I want to be able to contribute directly to the development of the game(s) via polls, having the chance to write my own ideas in a dedicated section (eg. ideas for the story/storytelling, game level design etc.)**
For the same reasoning as user stories 3, 5, and 6, this user story could not be fulfilled in the first release of this website

**8. As a new user/creator, I want a seamless experience in terms of setting up my game project on the platform**
Signing uop as a Creator user is as simple as checking the checkobx in the registration form. Once the account and email is verified, the Creator user can simply go to the Game Projects page, click Add Project, fill out the form, and the project will be up and live on the platform - ready to receive donations
**9. As a creator, I want to be able to manage my game projects, including adding, updating and deleting a project of mine as I see fit**
In user story 8 being able to add projects is already explained. Once a project has been created, and the Creator user accesses the project details of their project, they will have two buttons available - Update and Delete. Update will direct the Creator user to the same form as adding a project, but will fields pre-populated, and if anything is changed and confirmed, the changes will be reflected in the project details.

**10. As a user, I want to be able to have a seamless experience for donating to a given project, with as few clicks required to execute a donation, where only essential details (eg. card details) are required of me to complete a transaction**
As explained in the README file in the **Credits** section, the website Kickstarter influenced the design choice of having a simple, minimalistic checkout and payment page, where only filling in card details are required to complete a donation

**11. As a user, I want to be able to get in touch with the developer of the website**
In the footer of each page users can find an email address of the website's developer as well as social media links to find the relevant social media profiles/pages that belong to the Gamestarter

**12. As a user, I want to be able to get an overview of my previous donations**
If the user has already made previous donations to game projects, these individual instances of donations made are recorded and displayed in the user's profile page. These are shown in three's, with most recent donations displayed at the top. A 'Show More' button helps to render more items in the user's history should there exist more previous donations.

**13. As a creator, I want to be able to get an overview of the game projects I currently have up on Gamestarter**
Similarly to user story 12 (except the user must be a Creator), any game projects created previously and that are still present on the platform can be found on the user's profile page. This list of records is formatted in the same way as previous donations, and also has a 'Load More' button and functionality. Another way for Creators to check what projects they have up on the platform is by using the search bar on the Game Projects page, searching for their username to ensure it will display results where the owner's name matches the search query.

## Manual Testing
