
import streamlit_authenticator as stauth
import streamlit as st

import psycopg2 as ps
import pandas as pd
mydb=ps.connect(database="d8f945g4dudcl0", user="jexkbfaxxohsyp",
password="8cae305dcedc724344fab60b1534eceae9147e59642b698b1fc8b9d6e0d5e5d5",
host="ec2-3-225-213-67.compute-1.amazonaws.com", port="5432")


cur= mydb.cursor(buffered=True)
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def addData(a,b,c,d):
    
    cur.execute("""CREATE TABLE if not exists MyComfort_dataset (date_time  datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Location VARCHAR(50),Seat_Number int, Thermal_Sensation VARCHAR(50));""")
    cur.execute("INSERT INTO MyComfort_dataset VALUES(%s,%s,%s,%s);",( a,b,c,d))
    mydb.commit()
    mydb.close()
    st.success('Submission Success! ')






def form():  
    st.header('HVAC Request Interface')
    st.write('Raise Your Request Here')
  
    with st.form(key='Info form'):
        
        Location=st.selectbox('Office Location', ['Phase 1', 'Phase 2','Central block'])
        
        Thermal_Sensation=st.selectbox('Your Current thermal Sensation ?', ['Too Cool', 'Cool','Slightly cool',
        'Just fine','Slightly warm','Hot','Too Hot'])
        Seat_Number=st.number_input(label='Seat Number',min_value=1,max_value=50)        
        
        submission=st.form_submit_button(label='Submit')
        Date_time=timestamp
        
        if submission==True:
            addData(Date_time,Location,Seat_Number,Thermal_Sensation)
            


names = ['Leo', 'Luffy']
usernames = ['Leo120', 'Luffy']
passwords = ['123', '456']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    form()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

