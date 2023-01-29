Scholasrship collab

A website where people can tell their history/dreams and ask support to pay their educational costs. The idea is to help people to change their life's through study. The users will be people in need of financial support to start/complete their educational development. 

## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

  - [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
  - [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [x] Update
  - [x] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [x] Update
  - [ ] Destroy - Deleting a pledge will not be allowed
- User
  - [X] Create
  - [X] Retrieve
  - [x] Update
  - [x] Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [x] Limit who can create
  - [x] Limit who can retrieve
  - [x] Limit who can update
  - [x] Limit who can delete
- Pledge
  - [x] Limit who can create
  - [x] Limit who can retrieve
  - [x] Limit who can update
  - [ ] Limit who can delete - Not allowed to be done
- User
  - [ ] Limit who can retrieve - No restriction is necessary
  - [ ] Limit who can update - No restriction is necessary
  - [ ] Limit who can delete - No restriction is necessary

### Implement relevant status codes

- [x] Get returns 200
- [x] Create returns 201
- [x] Not found returns 404

### Handle failed requests gracefully 

- [x] 404 response returns JSON rather than text

### Use token authentication

- [X] impliment /api-token-auth/

## Additional features

- [x] {Filter}

You can filter according to your preferences: 'owner', 'date_created' and 'is_open'

- [x] {Password Change}

{{ description of feature 2 }}

- [x] {Favourite project}

{{ description of feature 3 }}

### External libraries used

- [x] django-filter


## Part A Submission

- [x] A link to the deployed project. https://shy-rain-4768.fly.dev/
- [x] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [x] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [x] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema.

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```

2. Sign in User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```

3. Create Project

```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
```