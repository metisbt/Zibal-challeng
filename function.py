
# The functions in this file each have the task of receiving information and connecting to the respective API on the server. 
## They perform the task of fetching data and return the results.

import requests
import re


# get data of iban inquiry from api
def iban_inquiry(data):
    site = "https://api.zibal.ir/v1/facility/ibanInquiry"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            name = datas['data']['name']
            bankname = datas['data']['bankName']
            istransferable = datas['data']['isTransferable']
            return {"name": name, "bankname": bankname, "istransferable": istransferable}
        else:
            return f"خطا: {datas['message']}"

# get data of national identity inquiry from api
def national_identity_inquiry(data):
    site = "https://api.zibal.ir/v1/facility/nationalIdentityInquiry"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            name = str(datas['data']['firstName']) + " " + str(datas['data']['lastName'])
            fathername = datas['data']['fatherName']
            alive = datas['data']['alive']
            return {"name": name, "fathername": fathername, "alive": alive}

        else:
            return f"خطا: {datas['message']}"

# get data of card to iban from api
def card_to_iban(data):
    site = "https://api.zibal.ir/v1/facility/cardToIban"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            name = datas['data']['name']
            iban = datas['data']['IBAN']
            bankname = datas['data']['bankName']
            return {"name": name, "iban": iban, "bankname": bankname}
        else:
            return f"خطا: {datas['message']}"

# get data of card inquiry from api
def card_inquiry(data): 
    site = "https://api.zibal.ir/v1/facility/cardInquiry"
    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            name = datas['data']['name']
            return {'name': name}
        else:
            return f"خطا: {datas['message']}"

# get data of postal code inquiry from api
def postal_code_inquiry(data):
    site = "https://api.zibal.ir/v1/facility/postalCodeInquiry"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            return {'a': datas}
        else:
            return f"خطا: {datas['message']}"

# get data of shahkar inquiry from api
def shahkar_inquiry(data):
    site = "https://api.zibal.ir/v1/facility/shahkarInquiry"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            match = datas['data']['matched']
            return {"match": match}
        else:
            return f"خطا: {datas['message']}"

# get data of check iban with name from api
def check_iban_with_name(data):
    site = "https://api.zibal.ir/v1/facility/checkIBANWithName"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            match = datas['data']['matched']
            return {"match": match}
        else:
            return f"خطا: {datas['message']}"

# get data of check card with name from api
def check_card_with_name(data):
    site = "https://api.zibal.ir/v1/facility/checkCardWithName"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            match = datas['data']['matched']
            return {'match': match}
        else:
            return f"خطا: {datas['message']}"

# get data of card to account from api
def card_to_account(data):
    site = "https://api.zibal.ir/v1/facility/cardToAccount"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            name = datas['data']['name']
            bankaccount = datas['data']['bankAccount']
            bankname = datas['data']['bankName']
            return {"name": name, "bankaccount": bankaccount, "bankname": bankname}
        else:
            return f"خطا: {datas['message']}"

# get data of check card with national code from api
def check_card_with_national_code(data):
    site = "https://api.zibal.ir/v1/facility/checkCardWithNationalCode"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            match = datas['data']['matched']
            return {'match': match}
        else:
            return f"خطا: {datas['message']}"

# get data of check iban with national code from api
def check_iban_with_national_code(data):
    site = "https://api.zibal.ir/v1/facility/checkIbanWithNationalCode"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            match = datas['data']['matched']
            return {'match': match}
        else:
            return f"خطا: {datas['message']}"

# get data of company inquiry from api
def company_inquiry(data):
    site = "https://api.zibal.ir/v1/facility/companyInquiry"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            return datas
        else:
            return f"خطا: {datas['message']}"

# get data of persian to finglish from api
def persian_to_finglish(data):
    site = "https://api.zibal.ir/v1/facility/persianToFinglish"

    result = requests.post(site ,json=data ,headers={"Authorization":"Bearer 309f719fcf264e5fa47734227982dae9"})
    if result.status_code not in [200, 400]:
        return f"Error: {result.status_code}"
    else:
        datas = result.json()
        if datas["result"] == 1:
            finglishtext = datas['data']['finglishText']
            return {"finglishtext": finglishtext}
        else:
            return f"خطا: {datas['message']}"

# check account number is true or not
def check_ircart(cartnumber):
    if re.search(r"^\d{10}$", cartnumber):
        return True
    else:
        return False

# check phone number is true or not
def check_phone(phone):
    if re.search(r"^\d{11}$", phone):
        return True
    else:
        return False

# check iban number is true or not
def check_IR(ir):
    if re.search(r"^IR\d{24}$", ir):
        return True
    else:
        return False

# check date is true or not
def check_date(da):
    if re.search(r"^[1][1-4]\d{2}/[0-1][0-9]/[0-3][0-9]$", da):
        return True
    else:
        return False

# check name is true or not
def check_name(name):
    if re.search(r"[\s+\D+]", name):
        return True
    else:
        return False

# check cart number is true or not
def check_bankcart(bcart):
    if re.search(r"^\d{16}$", bcart):
        return True
    else:
        return False

# check postal number is true or not
def check_post(pnum):
    if re.search(r"^\d{10}$", pnum):
        return True
    else:
        return False
    
# check company number is true or not
def check_cnum(cnum):
    if re.search(r"^\d{11}$", cnum):
        return True
    else:
        return False
