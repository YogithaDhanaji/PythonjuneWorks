email_id=[
    "sam@gamail.com",
    "yogi@gamail.com",
    "alex@gamail.com",
    "ashin@gamail.com",
    "nam@gamail.com",
    "alf@gamail.com",

]

f=open("C:\\Users\\LENOVO\\Desktop\\PythonJuneWorks\\FILEPRGMS\\emails.txt","w")

for email in email_id:

    f.write(email+"\n")
