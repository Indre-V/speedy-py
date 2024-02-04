# Speedy-Py

Speedy-Py typing test is a tool designed to evaluate typing speed and accuracy. It provides users with a platform to assess their typing skills in terms of words per minute (WPM) and accuracy rate. The test typically presents users with a passage or a series of random words that they need to type accurately and swiftly within a specified time frame.

By practicing regularly with Speedy-Py, users can enhance their typing skills and become more efficient at keyboard-based tasks.


[Deployed Application Link](https://speedy-py.herokuapp.com)


![Speedy-Py](docs/typing-test-responsive-display.png)

- [Speedy-Py](#speedy-py)
- [Contents](#contents)
- [User Experience (UX)](#user-experience--ux-)
  * [Colour Scheme](#colour-scheme)
  * [Design Choices](#design-choices)
  * [How to Play](#how-to-play)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [Website Goals and Objectives](#website-goals-and-objectives)
  * [Target Audience](#target-audience)
- [Logic](#logic)
  * [Python Logic](#python-logic)
  * [Data Model](#data-model)
  * [Database structure](#database-structure)
- [Features](#features)
  * [Existing Features](#existing-features)
    + [Title and Introduction Section](#title-and-introduction-section)
    + [Options menu](#options-menu)
    + [Game Over Menu](#game-over-menu)
    + [Leaderboard](#leaderboard)
  * [Future Enhancements](#future-enhancements)
- [Testing](#testing)
  * [Accessibility](#accessibility)
  * [Bugs](#bugs)
  * [Responsiveness Tests](#responsiveness-tests)
  * [Code Validation](#code-validation)
    + [PEP8 Testing](#pep8-testing)
    + [Error Handling](#error-handling)
  * [User Story Testing](#user-story-testing)
  * [Manual testing](#manual-testing)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Browser Testing](#browser-testing)
- [Deployment](#deployment)
  * [To deploy the project](#to-deploy-the-project)
  * [To fork the project](#to-fork-the-project)
  * [To clone the project](#to-clone-the-project)
- [Technology](#technology)
  * [Languages used](#languages-used)
  * [Python Libraries:](#python-libraries-)
  * [Tools](#tools)
- [Credits](#credits)
  * [Disclaimer](#disclaimer)


# User Experience (UX)

It is deployed with Heroku to ensure a seamless user experience for players.

##  Colour Scheme

The color scheme chosen for the HTML page with a terminal view was taken from the background image and was obtained from the <b>coolors.co</b> generator. The "run program" button's color was changed to blend in with the background.

![Colour Scheme](docs/docs/palette.png)

High contrast colors are used to show terminal outputs on a black background to improve readability and accessibility. Warnings are red, standard prompts are yellow, and inputs for are blue. Menus and confirmation messages are both green. 

## Design Choices

Background image is generated by [Gencraft](https://gencraft.com/ "Gencraft"). 

## How to Play

## User Goals

* Improve typing speed and accuracy.
* Enhance overall typing skills.
* Track personal progress over time.
* Enjoy a fun and engaging typing experience.

## User Stories 

As a user, I would like to:
  * Clearly understand the purpose of the application from the first interaction.
  * Use the program in real-life scenarios to enhance my typing skills.
  * Receive clear feedback for the actions I take within the application.
  * Be challenged by having to input actual words rather than random letters.
  * Compare my score to others on the leaderboard.
  * Easily and intuitively navigate through the typing test.
  * Learn how I can improve my typing speed and accuracy based on my score.
  * Have the option to save my results for future reference.
  * Access my previous test results to track my progress.
  * Have the ability to delete specific scoresheets or data entries if needed.


## Website Goals and Objectives

* Provide a user-friendly interface for typing exercises.
* Offer a range of typing tests and exercises tailored to different skill levels.
* Implement features such as timers, accuracy meters and progress tracking.
* Allow users to customize their typing practice sessions based on preferences.
* Foster a sense of community through leaderboards and achievements.
* Provide tips how to improve the skills.


## Target Audience

* Students of all ages, including school children, college students, and language learners.
* Professionals who rely  on typing for their daily work tasks, such as writers, programmers and office workers.
* Gamers interested in improving their typing speed and accuracy for gaming competitions or communication.
* Educators seeking effective tools to teach typing skills in classrooms and online learning environments.
* Users looking to enhance their typing abilities in a fun and interactive manner.


[Back to top](#contents)

# Logic

## Python Logic

A flow diagram of the logic behind the application was developed using [Lucid Chart](https://www.lucidchart.com/).

As the flow chart was created at the outset of the project, it does not fully reflect all elements of the application.

![Flow Chart](docs/flow-chart.png)

For PDF version [click here](docs/flow-diagram.pdf)

## Data Model


## Database structure

Google Sheets service is used to store project's database in the spreadsheet.

[Back to top](#contents)

# Features

## Existing Features

### Title and Introduction Section

### Options menu

### Game Over Menu

### Leaderboard

The Leaderboard feature was created using Google Sheets.

## Future Enhancements

* Continuously update and improve the application based on user feedback and technological advancements.


[Back to top](#contents)


# Testing

## Accessibility

[WebAIM](https://webaim.org/resources/contrastchecker/) online tool was used to check terminal colour contrast. 

- Using clear instructions
- Asking for user input before continuing
- Validating inputs before moving on to the next step
- Testing the game to make sure it does not crash from user input
- Using ARIA labels in the README

## Bugs 


[Back to top](#contents)

## Responsiveness Tests


[Back to top](#contents)


## Code Validation

### PEP8 Testing
The python files have all been passed through [PEP8 Online](http://pep8online.com/)

![PEP8](docs/pep8-test-result.png)


### Error Handling



## User Story Testing


[Back to top](#contents)



## Manual testing

Details of manual testing can be found in [TESTING.md file()]


[Back to top](#contents)


## Lighthouse Testing

....   tested in the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and [Microsoft Edge Dev Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/open/?tabs=cmd-Windows) using Lighthouse Testing tool which inspects and scores the website for the following criteria:

* Performance - how quickly a website loads and how quickly users can access it.
* Accessibility - test analyses how well people who use assistive technologies can use your website.
* Best Practices - checks whether the page is built on the modern standards of web development.
* SEO - checks if the website is optimised for search engine result rankings.

Tests for Desktop on Lighthouse Chrome:
![Lighthouse-Desktop-Chrome-Index](docs/lighthouse-desktop-chrome-index.png "Lighthouse-Desktop-Chrome-Index")

Tests for Mobile on Lighthouse Chrome:
![Lighthouse-Mobile-Chrome-Index](docs/lighthouse-mobile-chrome-index.png "Lighthouse-Mobile-Chrome-Index")

Tests for Desktop Lighthouse Edge:
![Lighthouse-Desktop-Edge-Index](docs/lighthouse-desktop-edge-index.png "Lighthouse-Desktop-Edge-Index")

Tests for Mobile on Lighthouse Edge:
![Lighthouse-Mobile-Edge-Index](docs/lighthouse-mobile-edge-index.png "Lighthouse-Mobile-Edge-Index")


[Back to top](#contents)


## Browser Testing


[Browser Compatibility Manual Test](docs/browser-compatibility-test-results.pdf "Browser Compatibility Manual Test")


[Back to top](#contents)

# Deployment

## To deploy the project

This site was developed using [Gitpod](https://www.gitpod.io/), stored on [Github](https://github.com/) and deployed with [Heroku](https://dashboard.heroku.com/apps).

Deploying on Heroku:
  * From the homescreen, click "New" and select "Create new app"
  * Choose app name, select region and click "Create"
  * Go to "Settings" and add PORT : 8000 to the Config Vars (CREDS : {contents of creds.json file} also added but excluded from Github for security reasons)
  * Add heroku/python and heroku/nodejs buildpacks (in that order)
  * Go to "Deploy" and connect Github repository
  * Select "Enable Automatic Deploys" and click "Deploy Branch"
  * The link to deloyed application: https://speedy-py.herokuapp.com/

_Any changes required to the website, they can be made, committed and pushed to GitHub._

[Back to top](#contents)

## To fork the project

Forking the GitHub repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.

- Log in to GitHub.
- Locate the repository.
- Click to open it.
- The fork button is located on the right side of the repository menu.
- To copy the repository to your GitHub account, click the button.

## To clone the project

- Log in to GitHub.
- Navigate to the main page of the repository and click Code.
- Copy the URL for the repository.
- Open your local IDE.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the URL you copied earlier.
- Press Enter to create your local clone.

[Back to top](#contents)

# Technology

##  Languages used

-   [Python](https://www.python.org/) - high-level, general-purpose programming language.
-   [Markdown](https://en.wikipedia.org/wiki/Markdown) - markup language used to write README and TESTING documents.


## Python Libraries:

- [colorama](https://pypi.org/project/colorama/) - for adding colour to terminal text.
- [datetime](https://pypi.org/project/DateTime/): used to get today's date for the leaderboard entry.
- [gspread](https://pypi.org/project/gspread/): to allow communication with Google Sheets. 
- [requests](https://pypi.org/project/requests): enables data retrieval from APIs.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html):  used to validate credentials and grant access to google service accounts.
- [pandas](https://pypi.org/project/pandas/) - used for sorting and displaying leaderboard data in user-friendly format. 
- [textwrap](https://docs.python.org/3/library/textwrap.html) - built-in python module - used to wrap lines over 79 char to next line e.g. long book description. 
- [PrettyTable](https://pypi.org/project/prettytable/) - python library for easily displaying tabular data in a visually appealing ASCII table format.
- [os](https://docs.python.org/3/library/os.html?highlight=os#module-os) 
  - `os.system` is used in order to clear the terminal when beginning a new game.
  - `os.environ` is used to get Oxford API credentials from environment variables (defined in env.py).

## Tools

* [GitHub](https://github.com/ "GitHub")
* [GitPod](https://www.gitpod.io/#get-started "GitPod")
* [Heroku](https://dashboard.heroku.com/apps "Heroku")
* [Lucidchart](https://lucid.app/documents#/dashboard "Lucidchart")
* [PEP8 Validation](http://pep8online.com/ "PEP8 Validation")
* [TOC Generator](https://ecotrust-canada.github.io/markdown-toc/ "TOC Generator")
* [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive")
* [Responsive Design Checker](https://responsivedesignchecker.com/ "Responsive Design Checker")
* [WebAIM](https://webaim.org/resources/contrastchecker/ "Web Aim")
* [Image Resize](https://www.iloveimg.com/ "iLoveIMG")
* [Google Sheets API](https://developers.google.com/sheets/api "Google Sheets API")

[Back to top](#contents)


# Credits

- Feedback, advice and support:

  - [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

- Code inspiration and learning content:

  - [Project Portfolio-3 channel on Slack](https://slack.com/intl/en-ie/ "Slack")
  - [Love Love Sandwiches Project](https://codeinstitute.net "Love Sandwiches Project")
  - [W3C Schools](https://www.w3schools.com/ "W3C Schools")
  - [StackOverflow](https://stackoverflow.com/ "StackOverflow")
  - [CodePen](https://codepen.io/pen/ "CodePen")
  * [Date and time in Python](https://www.programiz.com/python-programming/datetime/current-datetime "Programiz")
  * [Pandas Sort: Your Guide to Sorting Data in Python](https://realpython.com/pandas-sort-python/ ("Padas Sort"))
  * [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python "Google Sheets")

* YouTube Channels for Speedy-Py functionality: 

  * [Alina Chudnova](https://www.youtube.com/watch?v=7lGRTeBlDvQ "YouTube")
  * [Make Everyday EZ Day](https://www.youtube.com/watch?v=ykOlbRaNBYU "YouTube")
  * [Web Dev Simplified](https://www.youtube.com/watch?v=R-7eQIHRszQ "YouTube")
  * [Coding Lifestyle 4u](https://www.youtube.com/watch?v=1R8KCdRcoUw "YouTube")
 

* Visual content:

  - [Coolors](https://coolors.co/ "Coolors")
 
* Images:
  
  - [Gencraft](https://gencraft.com/ "Gencraft")

## Disclaimer
-   SpeedyPy app was created for educational purpose only. 
[Back to top](#contents)