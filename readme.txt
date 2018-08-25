Author:
	Tanner Woody
Date:
	20180824

REQUIREMENTS:
	Gmail account -- Recommend making a new one to avoid conflict with personal account

Attempting to Support:
	Craigslist

Craigslist Auto Jobs:
	1. Copy the search url for your city and desired job.
	2. Enter your gmail credentials
	3. Overwrite path to coverletter template
	4. Overwrite path to resume.pdf
	5. Run bot and send doctored and personal cover letters to each company on craigslist query result

Future support:
	Get a list of companies hiring via twitter and hashtags
	Get a list of companies that are hiring via indeed, glassdoor, etc.

TODO:
	With `findemails` list, send resume email to each person on that list
	Send emails to webmaster@domain.com
	Provide more items to `generics` for links to avoid looking up
	Consolidate code and make everything more managable
	Google query the links in `foundlinks`
		query should be something like `company.com human resources contact`
	Store items in an sql DB in regards to date email was sent, who it was sent to, ....
