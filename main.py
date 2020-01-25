import pandas as pd

import re


ff= open("result.txt","w+")
data = pd.read_csv("sample_email.csv",squeeze = True)
first_name = data.iloc[:, 0]
last_name = data.iloc[:, 1]
mail_to = data.iloc[:, 10]
subject = data.iloc[:, 11]
body = data.iloc[:, 12]
phone = data.iloc[:, 8]


full_name=[]

for i in range(len(first_name)):
    full_name.append(first_name[i]+" " +last_name[i])



sender_name = '''
Thanks,
Rob Willison.
'''



dat = []
email_list=[]
phone_list=[]
x = 0
while x < len(data):
    z = """
Email_to : {mail_to}
Subject Line: {subject}
Hi {full_name}
{body}
Thanks,
Rob Willison.
    
    """.format(mail_to=mail_to[x], subject=subject[x], full_name=full_name[x], body=body[x])

    dd = z
    ff.write(dd)
    dat.append(dd)
    print(dd)
    match = re.search(r'[\w\.-]+@[\w\.-]+', dd)
    email_list.append(match.group(0))
    try:
        ph1 = re.search(r'[\w\.-]+-[\w\.-]+-[\w\.-]+', dd)
        try:
            for item in ph1.group(0):
                if int(item):
                    # print(ph1.group(0))
                    phone_list.append(ph1.group(0))
                    break
        except:
            pass        
        # phone_list.append(ph1.group(0))

        

        # print(ph1.group(0))
    except:
        pass    

    
    

    x += 1


    

# mail_list=[]
# for j in range(len(mail_to)):
#     if mail_to[j]!=" ":
#         mail_list.append((mail_to[j]))


# +1 (123) 456-7890

# phone_list=[]
# for k in range(len(phone)):
#     if phone[k]!=" ":
#         phone_list.append((phone[k]))


df_number = pd.DataFrame(phone_list, columns=["Number"])

df_number.to_csv('number.csv', index=False)


df = pd.DataFrame(email_list, columns=["Mail Address"])

df.to_csv('mail.csv', index=False)


