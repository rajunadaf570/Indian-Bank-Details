# About:
Indian Bank details.\
Using the Bank name, Bank branch, and Bank ifsc code, to get details of the Bank.


# Tech:
. Django==2.0\
. Python==3.7\
. Postgresql


#           ............To Search the bank details..........

## STEP 1:
First and foremost have to create or set username and password using,\
createsuperuser command.

Using username and password you can get access token, to get access token call below api.\

#### Input: username, password.
[http://127.0.0.1:8000/api/token/token\]

#### Output: access token and refresh.

If access token expired call below api to get new access token.

#### Input: refresh token.
[http://127.0.0.1:8000/api/token/refresh/]

#### Output: access token.

## STEP 2:
#		To call the below api, token as mandatory Header.

[http://127.0.0.1:8000/api/v1/banks/getbranchdetails/]
Using above api you can get bank details.

### Example: 
#### 1. Input: 
  {'bank':'STATE BANK OF INDIA'} 
#### Output:
list of State Bank details.

#### 2. Input:
  {'branch':'Sambra'}
#### Output:
list of Bank which is present in Sambra.
Or else use combination of input to get perticular Bank detials.\
example :\
input:{\
'bank':'STATE BANK OF INDIA',\
'city':'Belgaum'\
}\
\
and also use limit and offset.\
Use requirement.txt file and install all the packages.







