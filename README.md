# Speedy-Py

Speedy-Py typing test is a tool designed to evaluate typing speed and accuracy. It provides users with a platform to assess their typing skills in terms of words per minute (WPM) and accuracy rate. The test typically presents users with a passage or a series of random words that they need to type accurately and swiftly within a specified time frame.

By practicing regularly with Speedy-Py, users can enhance their typing skills and become more efficient at keyboard-based tasks.


[Speedy-Py Live](https://speedy-py-5327a914ba84.herokuapp.com/)


![Speedy-Py](docs/typing-test-display.png)


# Contents 
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
  * Have the ability to delete specific data entries if needed.


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


##  Colour Scheme

High contrast colors are used to show terminal outputs on a black background to improve readability and accessibility. Warnings are red, standard prompts are yellow, and general information is blue. 
Summary of color scheme used in the terminal:
Here's a brief summary of the color scheme used in the program:

* MAGENTA: Used for some headings.
* RED: Indicates errors or prompts for confirmation before quitting or deleting.
* GREEN: Indicates success messages or prompts for confirmation before quitting.
* YELLOW: Indicates warnings or prompts for user input.
* BLUE: Used for displaying instructions and tips.
* RESET_COLOR: Used to reset the text color to default.

[Back to top](#contents)

# Logic

## Python Logic

A flow diagram of the logic behind the application was developed using [Lucid Chart](https://www.lucidchart.com/).

As the flow chart was created at the outset of the project, it does not fully reflect all elements of the application.

![Flow Chart](docs/flowchart.jpeg)

For PDF version [click here](docs/flowchart-pdf.pdf)

## Aplication Code Structure

Python code is organized following the best modularization practices. This increases efficiency and readability of the code. It also assists in refactoring of the code for future improvements. However, [curses](https://docs.python.org/3/library/curses.html) module was used for the typing game so all the test related curses functions are contained in one file to avoid the application performance issues. Curses library facilitates the creation of text-based user interfaces within the terminal, handling keyboard input, displaying text with color and formatting. Curses functions are contained in a wrapper. It simplifies the initialization and cleanup of the curses application by handling the initialization and termination of curses mode automatically.

## Database structure

Google Sheets service is used to store project's database in the spreadsheet.

![Speadsheet sample](docs/spreadsheet.png)

Summary of the data structure in the google spreadsheet:

| Name            | Type       | Other Details            |
|-----------------|------------|--------------------------|
| ID              | String     | Unique identifier        |
| Username        | String     | Name of the user         |
| Completion Date | DateTime   | Date and time of completion |
| Accuracy        | Integer    | Accuracy percentage      |
| WPM             | Integer    | Words per minute         |


[Back to top](#contents)

# Features

## Existing Features

### Introduction Section

The program is run, terminal window displays the main menu of the typing speed test application. It prints the game logo followed by a numbered list of options using [Colorama]("https://pypi.org/project/colorama/").

![Terminal Intro](docs/terminal-intro.png)


### Options menu

The menu continously displays options list using the loop. To continue using the application, the user is prompted to choose one of the options from 1 to 6. Following the user's selection, the function verifies the input to make sure it is within the permitted range of possibilities. An error message asking the user to select the correct option is presented if the input is invalid. The related action linked to the selected choice is carried out if the input is valid. This functionality ensures seamless navigation through the application's features and facilitates user interaction.

<details><summary><b>Options Menu Functionality</b></summary>

![Options Menu Functionality](docs/options-menu.png)

</details><br


### View Instructions

 It presents users with a set of guidelines to follow while taking the typing test. The instructions are printed in the terminal with colorized text to enhance readability and user experience. After displaying the instructions, the function prompts users to return to the main menu, facilitating seamless navigation within the application.

<details><summary><b>View Instructions Display</b></summary>

![View Instructions Display](docs/view-instructions-display.png)

</details><br/>

### Test


 It begins by requesting user for their name. Name must be at least two characters. Then it generates a random paragraph for the user to type, which is displayed in the terminal with colorized text. The user is then prompted to begin typing, and their input is recorded. Once the user has finished typing, the function calculates and displays the results of the typing test, including accuracy and speed. It measures time taken in the background for calculations. This function serves as the core component of the typing speed test game, allowing users to assess and improve their typing skills within the terminal environment.Users are also given an option to either save test results or to return to the main menu.

 <details><summary><b>Test Functionalities</b></summary>

 Name Validation:

 ![Name Validation](docs/name-validation.png)

 Name Entry:

 ![Name Entry](docs/name-entry.png)

  Start Test:

![Start Test](docs/start-test.png)

Show Results:

![Show Results](docs/show-results.png)

Save test:

![Save Test](docs/save-test.png)


</details><br/>

### Typing Advice 

 It displays a list of 12 tips and tricks in the terminal, each designed to improve typing proficiency. It starts by presenting a list of 12 quick fixes in the terminal, all aimed at enhancing typing speed. To make the experience more interactive, users are required to press Enter in order to reveal each advice. Important methods including touch typing, good posture, finger positioning, and consistent practice are covered in the suggestions. The functionality also suggests that users take pauses, practice typing using games, and track their advancement over time. Users can improve their accuracy and speed while strengthening their typing skills by implementing these tips. At the end of the the function takes users back to the main menu so they can continue using the typing speed test application after applying these instructions.

<details><summary><b>Tips and Tricks Display</b></summary>

![Tips and Tricks Display](docs/tips-tricks-display.png)

</details><br/>

### Practice Accuracy

The user is prompted to practice accurately typing a paragraph that is created at random by the Practice Accuracy function as accuracy is imperative for speed typing skills. The function determines the accuracy of the user's input in relation to the original text once they have completed typing. The user sees a green text message congratulating them on reaching 100% accuracy. If not, the user is shown with a red letter that indicates their accuracy percentage. After that, the function asks the user if they want to attempt inputting the paragraph again. The user can start the practice again or return to main menu.

<details><summary><b>Practice Accuracy Display</b></summary>

![Practice Accuracy display](docs/practice-accuracy-display.png)

</details><br/>


### View Leaderboard

This functionality retrieves data from a spreadsheet and organizes it to display the top 10 results in a clear table format. Users are then given the option to remove an entry from the leaderboard. If they choose to do so, users are prompted to input the ID of the entry they wish to delete. The function searches for the corresponding entry, removes it if found, updates the leaderboard, and displays the revised version. If the entry ID is not found, the function alerts the user and allows them to try again. This process ensures accurate leaderboard data and user control over its contents. If they decline, they are returned to the main menu.
<details><summary><b>View Leaderboard</b></summary>

![View Leaderboard](docs/view-leaderboard.png)


![Edit Leaderboard](docs/leaderboard-edit.png)

</details><br/>

### Exit Application

Provides users with a confirmation prompt to confirm whether they want to exit the application. It operates within a loop to continuously prompt the user until a valid response is received. The prompt asks users to confirm whether they are sure they want to quit the application, giving them the option to respond with "Y" for yes or "N" for no.
Once a valid response is received, the function checks if the user confirmed they want to quit by entering "Y". If the confirmation is affirmative, the function clears the terminal screen, prints a thank-you message to acknowledge the user's usage of the application, and terminates the program.
If the user chooses not to exit the application by entering "N" or an invalid response, the function clears the terminal screen and returns the user to the main menu.


<details><summary><b>Exit Application</b></summary>

Confirm exit:

![Confirm Exit](docs/confirm-exit.png)

Exit Message:

![Exit View](docs/exit-message.png)

</details><br/>

## Future Enhancements

* Continuously update and improve the application based on user feedback and technological advancements.
* Database to save test results for multiple users
* Share results on Social Media
* Allow users to choose the content theme for the test i.e. legal, fiction, medical etc. 
* Allow users to select time and paragraph length for the test.


[Back to top](#contents)


# Testing

## Accessibility

[WAVE](https://wave.webaim.org/) online tool was used to check terminal colour contrast. ! alert was returned relating to the CI template layout. 

While building the application, the general principles of accessibility where adhered to: 

- Using clear instructions
- Asking for user input before continuing
- Validating inputs before moving on to the next step
- Testing the game to make sure it does not crash from user input
- Using ARIA labels in the README

![WAVE](docs/summary.png)

## Bugs 

| Bug                                 | Status   | Description                                                                                       | Steps To Resolve                                                            |
| ----------------------------------- | -------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Leaderboard refresh                 | Resolved | When results saved, they are no displayed in the leaderboard although recorded in the spreadsheet | Refresh added to view_leaderboard function so it refreshes prior to display |
| Menu loop                           | Resolved | If enter pressed when option selected, error showed                                               | Removed time.sleep functionality                                            |
| Screen flickering                   | Resolved | While typing deployed screen kept flickering.                                                     | Changed function from screen clear to erase                                 |
| Test stopped when backspace pressed | Resolved | During the test, when backspace pressed test terminated                                           | Updated key types in the function                                           |
| Live results                        | Resolved | When live test results functionality enabled, the deployed terminal kept freezing                 | Functionality removed due to performance limitations                        |

[Back to top](#contents)

## Code Validation

### PEP8 Testing

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details><summary><b>PEP8 Test Results</b></summary>

run.py:

![run.py](docs/pep8-run-py-result.png)

utils.py:

![utils.py](docs/pep8-utils-py-result.png)

game.py:

![game.py](docs/pep8-game-py-result.png)

constants.py:

![constants.py](docs/pep8-constants-py-result.png)

functions.py:

![functions.py](docs/pep8-functions-py-result.png)

menu.py:

![menu.py](docs/pep8-menu-py-result.png)

spreadsheet.py: 

![spreadsheet.py](docs/pep8-spreadsheet-py-result.png)

</details><br/>


### Error Handling



## User Story Testing

| User Story                                                                    | Result                                      | Pass | Screenshot                              |
| ----------------------------------------------------------------------------- | ------------------------------------------- | ---- | --------------------------------------- |
| Clearly understand the purpose of the application from the first interaction. | Name, intro and options reflect the purpose | Pass |  [ View](docs/users-story1.png " View")  |
| Use the program in real-life scenarios to enhance my typing skills.           | Practice accuracy option                    | Pass |  [ View](docs/users-story2.png " View")  |
| Receive clear feedback for the actions I take within the application.         | Feedback based on wpm result                | Pass |  [ View](docs/users-story3.png " View")  |
| Be challenged by having to input actual words rather than random letters.     | Sentences displayed from library            | Pass |  [ View](docs/users-story4.png " View")  |
| Compare my score to others on the leaderboard.                                | View leaderboard option                     | Pass |  [ View](docs/users-story5.png " View")  |
| Easily and intuitively navigate through the typing test.                      | Test displays step by step                  | Pass |  [ View](docs/users-story6.png " View")  |
| Learn how I can improve my typing speed and accuracy based on my score.       | Tips and tricks option                      | Pass |  [ View](docs/users-story7.png " View")  |
| Have the option to save my results for future reference.                      | Option to save top 10 results               | Pass |  [ View](docs/users-story8.png " View")  |
| Access my previous test results to track my progress.                         | View Leaderboard option                     | Pass |  [ View](docs/users-story9.png " View")  |
| Have the ability to delete specific data entries if needed.                   | Option to delete a score                    | Pass |  [ View](docs/users-story10.png " View") |

[Back to top](#contents)

## Manual testing




[Back to top](#contents)


## Lighthouse Testing

Speedy-Py was tested in the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and [Microsoft Edge Dev Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/open/?tabs=cmd-Windows) using Lighthouse Testing tool which inspects and scores the website for the following criteria:

* Performance - how quickly a website loads and how quickly users can access it.
* Accessibility - test analyses how well people who use assistive technologies can use your website.
* Best Practices - checks whether the page is built on the modern standards of web development.
* SEO - checks if the website is optimised for search engine result rankings.

<details><summary><b>Lighthouse Test Results</b></summary>

Tests for Desktop on Lighthouse Chrome:
![Lighthouse-Desktop-Chrome](docs/lighthouse-desktop-chrome-index.png "Lighthouse-Desktop-Chrome")

Tests for Mobile on Lighthouse Chrome:
![Lighthouse-Mobile-Chrome](docs/lighthouse-mobile-chrome-index.png "Lighthouse-Mobile-Chrome")

Tests for Desktop Lighthouse Edge:
![Lighthouse-Desktop-Edge](docs/lighthouse-desktop-edge-index.png "Lighthouse-Desktop-Edge")

Tests for Mobile on Lighthouse Edge:
![Lighthouse-Mobile-Edge](docs/lighthouse-mobile-edge-index.png "Lighthouse-Mobile-Edge")

</details><br/>

[Back to top](#contents)


# Deployment

## To deploy the project

This site was developed using [**GitPod**](https://www.gitpod.io/), stored on [**GitHub**](https://github.com/) and deployed with [**Heroku**](https://dashboard.heroku.com/apps).

Deploying on Heroku:

* From the homescreen, click **New** and select **Create new app**

* Choose app name, select region and click **Create**

* Go to "****Settings**" and add `PORT : 8000` to the Config Vars (``CREDS ``: {*contents of creds.json file*} also added but excluded from GitHub for security reasons)

* Add ``heroku/python`` and ``heroku/nodejs buildpacks`` (in that order)

* Go to **Deploy** and connect **Github** repository

* Select ``Enable Automatic Deploy`` and click **Deploy Branch**

* The link to deployed application: https://speedy-py.herokuapp.com/


[Back to top](#contents)

## To fork the project

  

Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.


- Log in to **GitHub**.

- Locate the repository.

- Click to open it.

- The fork button is located on the right side of the repository menu.

- To copy the repository to your **GitHub** account, click the button.

  
## To clone the project

  
- Log in to **GitHub**.

- Navigate to the main page of the repository and click **Code**.

- Copy the **URL** for the repository.

- Open your local **IDE**.

- Change the current working directory to the location where you want the cloned directory.

- Type git clone, and then paste the **URL** you copied earlier.

- Press **Enter** to create your local clone.
  

_Any changes required to the website, they can be made, committed and pushed to GitHub._

[Back to top](#contents)

# Technology

##  Languages used

-   [Python](https://www.python.org/) - high-level, general-purpose programming language.
-   [Markdown](https://en.wikipedia.org/wiki/Markdown) - markdown language used to write README and TESTING documents.


## Python Libraries:

- [colorama](https://pypi.org/project/colorama/) - for adding colour to terminal text.
- [datetime](https://pypi.org/project/DateTime/): used to get today's date for the leaderboard entry.
- [gspread](https://pypi.org/project/gspread/): to allow communication with Google Sheets. 
- [requests](https://pypi.org/project/requests): enables data retrieval from APIs.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html):  used to validate credentials and grant access to google service accounts.
- [PrettyTable](https://pypi.org/project/prettytable/) - Python library for easily displaying tabular data in a visually appealing ASCII table format.
- [Curses](https://docs.python.org/3/library/curses.html#module-curses) - terminal handling for character-cell displays.
- [UUID](https://docs.python.org/3/library/uuid.html) - generates a unique ID
- [Wonderwords](https://libraries.io/pypi/wonderwords) - A python package for random words and sentences in English language.


## Tools

* [GitHub](https://github.com/ "GitHub")
* [GitPod](https://www.gitpod.io/#get-started "GitPod")
* [Heroku](https://dashboard.heroku.com/apps "Heroku")
* [Lucidchart](https://lucid.app/documents#/dashboard "Lucidchart")
* [PEP8 Validation](http://pep8online.com/ "PEP8 Validation")
* [TOC Generator](https://ecotrust-canada.github.io/markdown-toc/ "TOC Generator")
* [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive")
* [WAVE](https://webaim.org/resources/contrastchecker/ "Web Aim")
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
  * [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python "Google Sheets")
  * [IIIT Kalyani](https://github.com/GDSC-IIIT-Kalyani/Typing-Speed-Test/blob/main/Speed%20typing.py "GitHub")


* YouTube Channels for Speedy-Py functionality: 

  * [Alina Chudnova](https://www.youtube.com/watch?v=7lGRTeBlDvQ "YouTube")
  * [Make Everyday EZ Day](https://www.youtube.com/watch?v=ykOlbRaNBYU "YouTube")
  * [Web Dev Simplified](https://www.youtube.com/watch?v=R-7eQIHRszQ "YouTube")
  * [Coding Lifestyle 4u](https://www.youtube.com/watch?v=1R8KCdRcoUw "YouTube")
  * [Tech with Tim](https://www.youtube.com/watch?v=NQ5i1kJAA6Y "YouTube")
 

## Disclaimer
-   SpeedyPy app was created for educational purpose only. 

[Back to top](#contents)