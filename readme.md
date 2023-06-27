
# MiniMail

## What is it?

A simple docker REST api microservice to send emails using pre-defined jinja templates. Supports all popular email providers - SMTP, Sendgrid, Mailgun and AWS SES.

## How do I send an email?

Simple. Just send a POST request to the `/send_email` endpoint with the json body containing the following - 
|Body Parameter| Type | Notes|
|--|--|--|
|recipient  |  str| must be a valid email ID
| subject | str | subject of the email
| template_name| str| name of the html template
| template_options| json| optional. JSON which is passed to the template
| api_key | str | optional. Based on configuration

Example JSON request - 
```json
{
	"api_key": "123456789",
	"recipient": "person@example.com",
	"subject": "Welcome to Minimail!",
	"template_name": "invite",
	"template_options": {
		"option1" : "value1"
	}
}
```

## How do I make a new template?

Also simple! All templates are written using the jinja templating language. You can add options in the template using double curly brackets (`{{`). As always, check the Jinja documentation or [this blog post](https://realpython.com/primer-on-jinja-templating/) for more details. There are two ways you can go about making a template -

1. Make a template using the existing base template

There's a file called `base.py` in the existing `email_templates` directory. That file acts like a style guide, and takes in jinja "blocks" as arguments to build on top of it. Refer to the comment in the `base.html` file or the `invite.html` file to see an example. The name of the html file is what you should use for the `template_name` field.

2. Create a new template from scratch

Just make an html file and refer to the jinja docs. Use the name of the html file for the `template_name` field.

## What was wrong with Nodemailer etc?

Not much, its just that every microservice tends to have its own email setup, which is inefficient and makes it difficult to have a standard design language across emails.