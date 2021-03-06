## What is  globalCovid-19Updates

[![Build Status](https://travis-ci.org/KabakiAntony/globalCovid-19Updates.svg?branch=develop)](https://travis-ci.org/KabakiAntony/globalCovid-19Updates) [![Coverage Status](https://coveralls.io/repos/github/KabakiAntony/globalCovid-19Updates/badge.svg?branch=develop)](https://coveralls.io/github/KabakiAntony/globalCovid-19Updates?branch=develop)

It is a REST API that gives daily updates for consumption by people who 
are looking to make apps that give users the daily numbers as we 
track the corona virus figures aroung the world.

This api is made based on flask framework, it will be hosted on heroku and a postgres db
will be used for persistence.

## Where am I getting data from ?

At this point I am getting data and filtering it for use from 
the repository that is being maintained by the [John Hopkins University](https://github.com/CSSEGISandData/COVID-19)


## Setup and installation

1. First things first set up virtualenv
      ```bash
           virtualenv venv
      ```      
2. Activate virtualenv on linux and windows  as below
      ```bash
         LINUX/MAC

         source venv\bin\activate

         WINDOWS

         venv\Scripts\activate
         
      ```
3. Install dependencies for the project
      ```bash
         pip install -r requirements.txt
      ```
4. Running tests
      ```bash
         python -m pytest --cov=app/api

         For those that may have a challenge running pytest as I noticed there is a bug getting pytest to 
         run on some windows machines then run the tests with  the below command. 

         python -m nose2 -v 

         The difference is that nose2 will not run coverage you will have to invoke coverage on your own,
         or if you decide to host the project on github and run travis-ci in the background then it will run 
         the coverage on your behalf and I do recommend adding a travis-ci webhook to this project.
      ```
5. Start the server
      ```bash
         flask run or python wsgi.py 
      ```
<details>
      <summary>globalCovid-19Updates endpoints</summary>

      | Method   | Endpoint                              | Description                                                 |
      | -------- | ------------------------------------- | ------------------------------------------------------------|
      | `GET`    | `/global`                             | get the latest update of the global numbers                 |
      | `GET`    | `/global/summary`                     | get the latest global sum and a per country breakdown       |
      | `GET`    | `/country/<str:name>`                 | get the numbers of the country whose name has been supplied |
      | `GET`    | `/historical/country/<str:name>`      | get the historical details of the country                   |
      | `GET`    | `/names`                              | gets all the names of the countries                         |

</details>

Incase of a bug or anything else use any on the below channels to reach me on

[Find me on twitter](https://twitter.com/kabakikiarie) OR  drop me an email at kabaki.antony@gmail.com
