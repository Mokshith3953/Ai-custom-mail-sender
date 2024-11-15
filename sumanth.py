import pandas
import send_mail
import genai
import time
data=pandas.read_csv(r"D:\PYHTON\bunny\file.csv")
print(data.head())
n_mail=0
c=0
le=data.shape[0]
perday=50
per_hor=50
f=0
l=[]
st=time.time()
for i in data.email:
    end=time.time()
    if c==perday or (end-st>60 and n_mail==per_hor):
        break
    if input(f'{i} if you need to schedule this Type: s')=='s':
        l.append([data.iloc[c]['Company_name'] ,i, 'Scheduled','NA','NA'])
        continue
    a=input(f"Enter the prompt {i}:")+data.iloc[c]['Company_name']+data.iloc[c]['products']+"you need to write a mail according to this products"
    mess=genai.text(a)
    print("email is sent to the user")
    res=send_mail.mail(i,mess)
    s=["send","deleivered","yes"]
    if res==-1:
        f+=1
        n_mail-=1
        s=["Failed","bounced","no"]
    l.append([data.iloc[c]['Company_name'] ,i, s[0],s[1],s[2]])
    n_mail+=1
    c+=1
    if input("if break : Type : exit")=='exit':
        break
    
    
    
print(f"Total mail send: {n_mail}\n Email pending :{le-n_mail} \n Email failed:{f}\n\n\n ")
    
for i in l:
    print(*i)
