import pandas as pd
from main import log_in,mail_creation,end

data = pd.read_csv('data_file.csv')
my_address = log_in('SenderMail@gmail.com', 'sendrpassword')  #login

for i in range(0, len(data)-1):
    to_mail = data.iloc[i]['mail']
    name = data.iloc[i]['name']
    dep = data.iloc[i]['department']
    mail_creation(to_mail,my_address, name , dep )     #Mail sending

end()

