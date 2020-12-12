import schedule
import webbrowser
import datetime


def open_mail():
    url = "https://mail.google.com"
    webbrowser.open(url)


def read_time():
    return datetime.datetime.now().time()	


if __name__=="__main__":
    open_mail() # just for testing   
