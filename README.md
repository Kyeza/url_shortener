[![Build Status](https://travis-ci.com/Kyeza/url_shortener.svg?branch=master)](https://travis-ci.com/Kyeza/url_shortener)

# URL Shortener

The goal of this Project is to create a URL shortener web application in the same 
vein as bitly, TinyURL, or the now defunct Google URL Shortener. 
 
## UX

- As a user, I want to enter a long url in the url-shortener, so that it can return me a short one.

## Technologies Used
- [Python](#)
- [Django](#)
- [HTML,CSS and JavaScript]
- [Bootstrap4](#)
- [JQuery](#)
- [Docker](#)
- [Travis](#)
- [Postgres](#)
   
## Testing
- `$ make test`

## Deployment
- create a .env file inside project directory add the following:
- set value for SECRET_KEY=secret 
- set value for DEBUG=False

then run the commands below to deploy: 

- `$ make deploy`
- `$ make docker-migrations`

to run the project go to your browser and enter url as  http://0.0.0.0:8000/

## Assumptions
- Database of choice: I would have prefered to use a NoSQL data like Mongo because it would scale batter but for purposes of quick development I have gone with a RDBMS(Postgres)
