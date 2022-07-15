files:
1- CSV data file                                          adta_file.csv
2- HTM file (mail formatting)                             html_file.html
3- mail bot code                                          main.py
4- data caller from the CSV file + finally send emails    call_data.py


To use this bot successfully,
you must follow the instructions below carefully and proficiently:

First: HTML mail preparation:

1- write your HTML script, and to but variables in your text and name them with a 
unique name.
in this project, I have two variables (name_replace) and (dep_replace).

2- If you want to attach pictures you will Define the image in the desired 
location and make it defined like this:  <img src='cid:myimageid' width="700">

3-  Save your file.

###################################################################
Secondly: Prepare the data set:

1- create a CSV file or excel file.

2- But your data. in my case, I just need the send-to mail and my two variables
  (to_mail , name , department).

###################################################################
Third: the bot: 

The code is attached to the comments for explanation.
You are careful
you are required to change the data in the main code and HTML file as you need

###################################################################
fourth: data calling:

in data calling, you will find in line 5 the log_in function
you must write a valid Gmail email and the correct password
NOTE: make sure that you have activated Less secure app access
	if not you can activate it from here:
	https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Npxle17jXki9-f7JXKPp-5X6dlmpD_PWIlH7QXo1Q0g0oht30mYySsW316nL_9AncC_oyJdlHLG0ynbH0nCf_SQMyRwQ

you can contact me on mail: asedky@gmail.com
				    s-abdulrhman.elfeky@zewailcity.edu.eg

