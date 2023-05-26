import datetime


def main():
    time = datetime.datetime.now() #gets the current datetime

    fDate = list(time.strftime("%x")) #format it to xx/xx/xx
    #replace / with _ for filename
    for i in range(0, len(fDate)):
        if (fDate[i] == '/'):
            fDate[i] = '_'

    fDate = "".join(fDate) #put back into string
    print(fDate)
    filename = "{fDate}_headlines.html".format(**locals()) #make the filename
    print(filename)
    return(filename)
#    file = open(filename, "w").close # create the file

main()
