This is MailMag a library which provice bulk mailing at ease, all the functions are made and you just have to call them!

There are several functions for two classes  the functions are:

    Mailman class:

        Pass the email id and password while making object;
        mail_id parameter can take list or a single email id

        Functions are as follow:

            simpleemail(mail_id, subject, body)
            htmlmail(mail_id, subject, html_msg)
            mailwithimage(mail_id, subject, body, file_name)
            mailwithpdf(mail_id, subject, body, file_name)

    Gspread Class:

        This requires your token and .json credential file given by google
        Sheet should be shared by you manually to your service account given in credential file
        while making object specify the filname or path, sheet name(spreadsheet name), the column no. in which emails are present
            (columns starts with 0)

        Functions in Gspread are:
            authorizers-> This only make a connection with your google spreadsheet and return that in a variable
            selectandsave-> This function authorize and returns a list of the items in the row of choosen column.

#How to use:
Put Mailmag.py in your working directory and use
       from Mailmag import Mailman, Gspread
