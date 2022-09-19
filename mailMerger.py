with open("names.txt", 'r', encoding='utf-8') as names_file:   # open names.txt for reading

    
    with open("body.txt", 'r', encoding='utf-8') as body_file:  # open body.txt for reading

        body = body_file.read()        # read entire content of the body

       for name in names_file:          # iterate over names
            mail = "Hello " + name.strip() + "\n" + body

            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:   # write the mails to individual files
                mail_file.write(mail)
