# PersonalizedGroupMail
Send batch emails with personalized greetings.

##About
A lot of time at university residence halls, information is distributed through batch emails. However they run the risk of being ignored by recipients. As a Resident Advisor especially, it is important that maximum resident engagement be achieved. This package is one solution.

'PersonalizedGroupMail` sends emails that are modified by adding customized greetings and a personal message. That way each recipient gets an email that was addressed directly to them and that contains a personal message that reinforces that point.

##Getting Started
To install this module, a [Python 2.7](https://www.python.org/download/releases/2.7/) installation is needed. First, clone (download) this repository. Then open the [command prompt](http://www.7tutorials.com/command-prompt-how-use-basic-commands) / [terminal](http://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html) and navigate to where this file is saved. Then run this command:

```python
python setup.py install
```

And you are done!

##Sending the First Emails
First we need to import this package:  
```python
import PersonalizedGroupMail as PGM
```

Then we need to instantiate a class that will do our work:  
```python
batchEmail = PGM.PersonalizedGroupMail('Subject', 'Your email address')
```

Now we need the message to send. That can be done through:  
```python
batchEmail.msg = my_message                 # passing a string variable, or,
batchEmail.get_message_from_text(filepath)  # passing a text file path, or,
batchEmail.get_message_from_html(filepath)  # passing a html file path
```
The next step is to get the recipients' names, email addresses, personal messages, and salutations (Hi, hey etc). There are two ways of doing this (using the example of salutations):
```python
batchEmail.salutations = list_of_salutations            # passing a list variable, or,
batchEmail.get_salutations_from_csv(filepath, column)   # loading them from a csv file with column specified
```
Specifying the column allows names, salutations, email addresses, and PMs to be stored in the same file (see `testData.csv`). Otherwise the first column is read.

In case there are fewer salutations or PMs than there are recipients, they can be assigned some randomly from the available data. Use this command:
```python
batchEmail.randomize_salutations()
batchEmail.randomize_personalized_messages()
```
Or if you need a default salutation and personal message for recipients that do not have any, you can use:
```python
batchEmail.set_default_salutation('Howdy!')
batchEmail.set_default_personalized_message("How've you been?")
```

All that is left is to connect to your email server and send the emails:  
```python
batchEmail.set_connection('host', 'port')         # connect to the server
batchEmail.authenticate('username', 'password')   # provide credentials
```
Finally, enter the magic command and the messages will be on their way:  
```python
batchEmail.send(sendmeacopy=True)                 # default value of sendmeacopy=False
```
##HTML Support
This package can send HTML files (and their plaintext alternatives). Currently there is no support for HTML attachments (like images etc.). Gmail does not have support for `<style></style>` tags in the email. So you can use [premailer](https://pypi.python.org/pypi/premailer) to convert `<style>` tags into inline style attributes.
