#python mailbot 
'''Author == Shubham Panchal'''
# external dependencies == pandas

import smtplib
import pandas as pd
import time
import random
import time
import random
import csv
import winsound


frequency = 3500  # Set Frequency To 2500 Hertz
duration = 1000 
printtime = time.strftime("%H:%M:%S:%D")
print(printtime) 


#read the required files in the folder
try:
    filenames = ['maillist.csv', 'senderlist.csv']
 
    # Create the list for the three DataFrames you want to create:
    dataframes = []
    for filename in filenames:
        dataframes.append(pd.read_csv(filename))
     df1 = dataframes[0]
    senderlist = dataframes[1]
    
except:
    print('all the files are not found or corrupted'  )

    

#print reciever list
try:
    toreciever = df1['email']
    print(toreciever.values.T.tolist())
    toreciever = toreciever.values.T.tolist()
    
except:
    print('file name = maillist.csv not found or corrupted'  )


#print senders list
try:
    gmail_sender = senderlist['id']
    gmail_passwd  = senderlist['password']
    print(gmail_sender)
    print(gmail_passwd) # print("**********")
    
except:
    print('file name = senderlist.csv not found or corrupted'  )


#open text message
try:
    f = open('message.txt','r+')
    TEXT = f.read()
    print(TEXT)

except:
    print('file name = message.txt not found or corrupted'  )


# create log file
try:        
    logs = open('logs.txt','w')
    logs.write('happy')
    logs.write('\ninferno')
    logs.close()

except:
    print('file name = logs.txt not found or corrupted'  )


# message file data
SUBJECT = "Message_you_need_to_send"
gmail_sender, gmail_passwd = senderlistfunc()
        
BODY = '\r\n'.join(['To: %s',
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])



#generate random for the mail timing, makin it look like a as human
h = []
x = len(senderlist) -1
print(x)
for l in range(len(toreciever)):
    print (random.randint(1,5))
    h.append(random.randint(1,5))
print("random value :",h[3]) #test random variable
print('total recievers of emails  :',len(toreciever))
print('sender id list: :',len(senderlist),'id:',gmail_sender)
print('the message body as per message.txt')
print(BODY)
print (time.strftime("%H:%M:%S:%D:%M:%Y"))


# email Sign In
for r in range(len(df2)):
    try:
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(gmail_sender[r], gmail_passwd[r])
        print('login successful for ',gmail_sender[r])
        time.sleep(1)
    except:
        print("login failed for ",gmail_sender[r])


# start sending bulk mails
for i in range(len(toreciever)):  

    try:                           
        s.sendmail(gmail_sender[0], toreciever[i], TEXT)
        print ('email sent to: ',toreciever[i] , i+1,'left:',len(toreciever) - (i +1) )
        time.sleep(h[i]) 
        
    except:
        print ('error sending mail 1 time')
        winsound.Beep(frequency, duration)
        break
            
print("all mails sent")
      

s.quit()


