# When a button is clicked in any form, the data related to that form is received,
## and the form data is converted to the required format for the API. 
### It is then sent to the specific function for each task, and after receiving the relevant information from the API, 
#### it is sent to the "fail" or "result" page.


from flask import Flask, render_template, request, jsonify
from function import *


app = Flask(__name__)

# connect to main page
@app.route('/')
def index():
    return render_template('index.html')

# with click submit button, get forms data that value number is checked
@app.route('/submit', methods=['POST'])
def submit():
    form_number = request.form.get('form_number')
    
    # iban_inquiry
    if form_number == '1':
        n = request.form.get('iban').strip()
        if check_IR(n):
            iban = {'IBAN': n}
            answer = iban_inquiry(iban)
            if type(answer) is dict:
                if answer['istransferable'] and answer['bankname'] != 'null':
                    return render_template('result.html', iban_asnwer = f'این شماره شبا به نام "{answer['''name''']}" در بانک "{answer['''bankname''']}" میباشد.')
                else:
                    return render_template('result.html', iban_asnwer = f'این شماره شبا به نام "{answer['''name''']}" میباشد.')
            else:
                return render_template('fail.html', iban_asnwer = answer)
        else:
            return render_template('fail.html', iban_asnwer = "شماره شبا باید با IR شروع شده و بدون خط تیره و فاصله باشد.")

    # national_identity_inquiry
    elif form_number == '2':
        n2 = request.form.get('nationalcode').strip()
        d = request.form.get('birthdate').strip()
        if check_ircart(n2) and check_date(d):
            nationalidentityinquiry = {"nationalCode": n2, "birthDate": d}
            answer2 = national_identity_inquiry(nationalidentityinquiry)
            if type(answer2) is dict:
                if answer2['''alive''']:
                    return render_template('result.html', national_identity_inquiry_asnwer = f'اطلاعات هویتی وارد شده متعلق به "{answer2['''name''']}" و نام پدر "{answer2['''fathername''']}" میباشد و ایشان در حال حاضر در قید حیات هستند.')
                else:
                    return render_template('result.html', national_identity_inquiry_asnwer = f'اطلاعات هویتی وارد شده متعلق به "{answer2['''name''']}" و نام پدر "{answer2['''fathername''']}" میباشد و ایشان در حال حاضر در قید حیات نیستند.')
            else:
                return render_template('fail.html', national_identity_inquiry_asnwer = answer2)
        elif not check_ircart(n2):
            return render_template('fail.html', national_identity_inquiry_asnwer = "شماره کارت ملی به درستی وارد نشده است. باید ۱۰ رقم و بدون فاصله و خط تیره باشد.")
        else:
            return render_template('fail.html', national_identity_inquiry_asnwer = "تاریخ تولد باید به فرم 1377/09/15 باشد")

    # card_inquiry        
    elif form_number == '3':
        n3 = request.form.get('cardnumber').strip()
        if check_bankcart(n3):
            cardnumber = {"cardNumber": n3}
            answer3 = card_inquiry(cardnumber)
            if type(answer3) is dict:
                return render_template('result.html', card_inquiry_asnwer = f'این شماره کارت به نام "{answer3['''name''']}" میباشد.')
            else:
                return render_template('fail.html', card_inquiry_asnwer = answer3)
        else:
            return render_template('fail.html', card_inquiry_asnwer = "شماره کارت باید بدون فاصله و حرف باشد و ۱۶ رقمی باشد.")

    # postal_code_inquiry
    elif form_number == '4':
        n4 = request.form.get('postalcode').strip()
        if check_post(n4):
            postalcode = {"postalCode": n4}
            answer4 = postal_code_inquiry(postalcode)
            b = answer4['a']['data']['address']
            if type(b) is dict:
                return render_template('result.html', postal_code_inquiry_asnwer = b)
            else:
                return render_template('fail.html', postal_code_inquiry_asnwer = answer4)
        else:
            return render_template('fail.html', postal_code_inquiry_asnwer = "کد پستی بدون خط تیره و فاصله باید باشد و شامل ۱۰ رقم باشد.")

    # company_inquiry
    elif form_number == '5':
        n5 = request.form.get('nationalid').strip()
        if check_cnum(n5):
            nationalid = {"nationalId": n5}
            answer5 = company_inquiry(nationalid)
            m = {}
            for i in answer5:
                if i != 'companyRelatedPeople':
                    x = answer5[i]['data']
                    m[i] = x
                else:
                    for item in len(answer5['a']['data']['companyRelatedPeople']):
                        m[item] = answer5['a']['data']['companyRelatedPeople'][item]
            if len(m) != 0:
                return render_template('result.html', company_inquiry_asnwer = m)
            else:
                return render_template('fail.html', company_inquiry_asnwer = answer5)
        else:
            return render_template('fail.html', company_inquiry_asnwer = "شناسه ملی باید شامل ۱۰ رقم بدون فاصله و خط تیره باشد")

    # card_to_iban
    elif form_number == '6':
        n6 = request.form.get('cardnumber').strip()
        if check_bankcart(n6):
            cardnumber = {"cardNumber": n6}
            answer6 = card_to_iban(cardnumber)
            if type(answer6) is dict:
                if answer6['bankname'] == 'null':
                    return render_template('result.html', card_to_iban_asnwer = f'این شماره کارت به نام "{answer6['''name''']}" با شماره شبا "{answer6['''iban''']}" میباشد.')
                else:
                    return render_template('result.html', card_to_iban_asnwer = f'این شماره کارت به نام "{answer6['''name''']}" با شماره شبا "{answer6['''iban''']}" در بانک "{answer6['''bankname''']}" میباشد.')
            else:
                return render_template('fail.html', card_to_iban_asnwer = answer6)
        else:
            return render_template('fail.html', card_inquiry_asnwer = "شماره کارت باید بدون فاصله و حرف باشد و ۱۶ رقمی باشد.")

    # card_to_account
    elif form_number == '7':
        n7 = request.form.get('cardnumber').strip()
        if check_bankcart(n7):
            cardnumber = {"cardNumber": n7}
            answer7 = card_to_iban(cardnumber)
            if type(answer7) is dict:
                return render_template('result.html', card_to_account_asnwer = f'این شماره کارت به نام "{answer7['''name''']}" میباشد.')
            else:
                return render_template('fail.html', card_to_account_asnwer = answer7)
        else:
            return render_template('fail.html', card_inquiry_asnwer = "شماره کارت باید بدون فاصله و حرف باشد و ۱۶ رقمی باشد.")

    # shahkar_inquiry
    elif form_number == '8':
        n8 = request.form.get('mobile').strip()
        c = request.form.get('nationalcode').strip()
        if check_phone(n8) and check_ircart(c):
            shahkarinquiry = {"mobile": n8, "nationalCode": c}
            answer8 = shahkar_inquiry(shahkarinquiry)
            if type(answer8) is dict:
                if answer8['match']:
                    return render_template('result.html', shahkar_inquiry_asnwer = 'کد ملی صاحب ای شماره موبایل با کد ملی وارد شده، تطابق دارد')
                else:
                    return render_template('result.html', shahkar_inquiry_asnwer = 'کد ملی صاحب شماره موبایل با کد ملی وارد شده تطابق ندارد.')
            else:
                return render_template('fail.html', shahkar_inquiry_asnwer = answer8)
        elif not check_phone(n8):
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره موبایل باید با 0 شروع شود و بدون فاصله و ۱۱ رقم داشته باشد")
        else:
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره کارت ملی به درستی وارد نشده است. باید ۱۰ رقم و بدون فاصله و خط تیره باشد.")

    # check_iban_with_name  
    elif form_number == '9':
        n9 = request.form.get('iban').strip()
        c1 = request.form.get('name').strip()
        if check_IR(n9) and check_name(c1):
            checkibanwithname = {"IBAN": n9, "name": c1}
            answer9 = check_iban_with_name(checkibanwithname)
            if type(answer9) is dict:
                if answer9['match']:
                    return render_template('result.html', check_iban_with_name_asnwer = 'صاحب شماره شبا و نام وارد شده تطابق دارند')
                else:
                    return render_template('result.html', check_iban_with_name_asnwer = 'صاحب شماره شبا و نام وارد شده تطابق ندارند')
            else:
                return render_template('fail.html', check_iban_with_name_asnwer = answer9)
        elif not check_IR(n9):
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره شبا باید با IR شروع شده و بدون خط تیره و فاصله باشد.")
        else:
            return render_template('fail.html', shahkar_inquiry_asnwer = "نام و نام خانوادگی فقط باید شامل حروف فارسی و فاصله باشد")
    
    # check_card_with_name  
    elif form_number == '10':
        n10 = request.form.get('cardnumber').strip()
        c2 = request.form.get('name').strip()
        if check_bankcart(n10) and check_name(c2):
            checkcardwithname = {"cardNumber": n10, "name": c2}
            answer10 = check_card_with_name(checkcardwithname)
            if type(answer10) is dict:
                if answer10['match']:
                    return render_template('result.html', check_card_with_name_asnwer = 'نام شماره کارت و نام وارد شده تطابق دارند')
                else:
                    return render_template('result.html', check_card_with_name_asnwer = 'نام شماره کارت و نام وارد شده تطابق ندارند')
            else:
                return render_template('fail.html', check_card_with_name_asnwer = answer10)
        elif not check_bankcart(n10):
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره کارت باید بدون فاصله و حرف باشد و ۱۶ رقمی باشد.")
        else:
            return render_template('fail.html', shahkar_inquiry_asnwer = "نام و نام خانوادگی فقط باید شامل حروف فارسی و فاصله باشد")

    # check_card_with_national_code  
    elif form_number == '11':
        n11 = request.form.get('nationalcode').strip()
        c3 = request.form.get('birthdate').strip()
        e = request.form.get('cardnumber').strip()
        if check_ircart(n11) and check_date(c3) and check_bankcart(e):
            checkcardwithnationalcode = {"nationalCode": n11, "birthDate": c3, "cardNumber": e}
            answer11 = check_card_with_national_code(checkcardwithnationalcode)
            if type(answer11) is dict:
                if answer11['match']:
                    return render_template('result.html', check_card_with_national_code_asnwer = 'اطلاعات کد ملی و صاحب شماره کارت تطابق دارند')
                else:
                    return render_template('result.html', check_card_with_national_code_asnwer = 'اطلاعات کد ملی و صاحب شماره کارت تطابق ندارند')
            else:
                return render_template('fail.html', check_card_with_national_code_asnwer = answer11)
        elif not check_bankcart(n10):
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره کارت باید بدون فاصله و حرف باشد و ۱۶ رقمی باشد.")
        elif not check_date(c3):
            return render_template('fail.html', shahkar_inquiry_asnwer = "تاریخ تولد باید به فرم 1377/09/15 باشد")
        else:
            return render_template('fail.html', shahkar_inquiry_asnwer = "کد ملی باید ۱۰ رقم و بدون فاصله و حروف باشد")

    # check_iban_with_national_code  
    elif form_number == '12':
        n12 = request.form.get('nationalcode').strip()
        c4 = request.form.get('birthdate').strip()
        e1 = request.form.get('iban').strip()
        if check_ircart(n12) and check_date(c4) and check_IR(e1):
            checkibanwithnationalcode = {"nationalCode": n12, "birthDate": c4, "IBAN": e1}
            answer12 = check_iban_with_national_code(checkibanwithnationalcode)
            if type(answer12) is dict:
                if answer12['match']:
                    return render_template('result.html', check_iban_with_national_code_asnwer = 'اطلاعات شماره شبا و صاحب شماره کارت تطابق دارند')
                else:
                    return render_template('result.html', check_iban_with_national_code_asnwer = 'اطلاعات شماره شبا و صاحب شماره کارت تطابق ندارند')
            else:
                return render_template('fail.html', check_iban_with_national_code_asnwer = answer12)
        elif not check_bankcart(n10):
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره کارت باید بدون فاصله و حرف باشد و ۱۶ رقمی باشد.")
        elif not check_date(c3):
            return render_template('fail.html', shahkar_inquiry_asnwer = "تاریخ تولد باید به فرم 1377/09/15 باشد")
        else:
            return render_template('fail.html', shahkar_inquiry_asnwer = "شماره شبا باید شامل IR باشد و بدون فاصله و خط تیره و ۲۴ رقم باشد")

    # persian_to_finglish  
    elif form_number == '14':
        n14 = request.form.get('persiantext').strip()
        if check_name(n14):
            finglishtext = {"persianText": n14}
            answer14 = persian_to_finglish(finglishtext)
            if type(answer14) is dict:
                return render_template('result.html', persian_to_finglish_asnwer = f'{answer14['''finglishtext''']}')
            else:
                return render_template('result.html', persian_to_finglish_asnwer = answer14)
        else:
            return render_template('result.html', persian_to_finglish_asnwer = "نام و نام خانوادگی فقط شامل حروف فارسیو فاصله باید باشد")

    else:
        return render_template('fail.html', error_answer = 'ridi azizam')
    
if __name__ == "__main__":
    app.run(debug=True)