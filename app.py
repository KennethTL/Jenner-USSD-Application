from flask import Flask, request
import africastalking
import os
app = Flask(__name__)
username = "sandbox"
api_key = "2dcafb313d4f5f4565fc2d9da5a87e40ad522456f8f906d6f38e001714b7a270"  # Exposed for the purpose of demonstrating the application
africastalking.initialize(username, api_key)
sms = africastalking.SMS

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")
  sms_phone_number = []
  sms_phone_number.append(phone_number)

  if text == '':
    response  = "CON Preferred language/Lugha inayopendekezwa \n"
    response += "1. English \n"
    response += "2. Kiswahili \n"
    
  elif text == '1':
    response = "CON Jenner Health Services \n"
    response += "1. Virtual Consultation \n"
    response += "2. Hospital / Health Centre Appointment \n"
    response += "3. Emergency Service Request \n"
    response += "4. Previous Diagnosis Report \n"
    response += "5. List of Hospitals / Health Centres \n"
    response += "6. List of Health Specialists"
    
  elif text == '1*1':
   try:
      #sending the sms
      sms_response = sms.send("Your virtual appointment has been scheduled for dd/mm/yyyy. Please carry your ID.", sms_phone_number)
      print(sms_response)
      response = "END You will receive an SMS with appointment details shortly."
   except Exception as e:
      #show us what went wrong
      print(f"Houston, we have a problem: {e}")

  elif text == '1*2':
    try:
      #sending the sms
      sms_response = sms.send("Your Health Centre appointment has been scheduled for dd/mm/yyyy. Please carry your ID.", sms_phone_number)
      print(sms_response)
      response = "END You will receive an SMS with appointment details shortly."
    except Exception as e:
      #show us what went wrong
      print(f"Houston, we have a problem: {e}")

  elif text == '1*3':
    try:
      #sending the sms
      sms_response = sms.send("A phone operator will call you shortly. Kindly provide as much information as you can for use by our Emergency Response Team.", sms_phone_number)
      print(sms_response)
      response = "END A phone operator will call you shortly."
    except Exception as e:
      #show us what went wrong
      print(f"Houston, we have a problem: {e}")

  elif text == '1*4':
    response = "CON Enter your ID Number \n"
    if text != '':
      try:
        #sending the sms
        sms_response = sms.send("DIAGNOSIS REPORT: Please reply to this SMS with your ID", sms_phone_number)
        print(sms_response)
        response = "END You will receive an SMS with further instructions."
      except Exception as e:
        #show us what went wrong
        print(f"Houston, we have a problem: {e}")

  elif text == '1*5':
    response = "CON Choose a specialist \n"
    response += "1. Radiologist \n"
    response += "2. Optician \n"
    response += "3. Cardiologist \n"
    response += "4. Neurologist \n"
    response += "5. Pediatrician \n"
    response += "6. Orthopedic"
  
  elif text == '1*5*1':
    response = "CON Choose your preferred county \n"
    response += "1. Nairobi \n"
    response += "2. Kiambu \n"
    response += "3. Garissa \n"
    response += "4. Mombasa \n"
    response += "5. Kisumu \n"
    response += "6. Machakos"

  elif text == '1*5*1*1':
    response = "END Specialised Hospital for County chosen \n"
    response += "1. MP Shah \n"
    response += "2. Kenyatta National Hospital \n"
    response += "3. Moi Teaching and Referral Hospital \n"
    response += "4. Nairobi Hospital \n"
    response += "5. Avenue Health Care \n"
    response += "6. Manugu Hospital"

  elif text == '1*6':
    response = "END Health Specialists \n"
    response += "1. Pediatrician \n"
    response += "2. Optician \n"
    response += "3. Cardiologist \n"
    response += "4. Neurologist \n"
    response += "5. Radiologist \n"
    response += "6. Orthopedic Surgeon"

  elif text == '2':
    response = "CON Huduma za Afya za Jenner. \n"
    response += "1. Ushauri wa Mtandao \n"
    response += "2. Miadi ya Kituo cha Afya \n"
    response += "3. Ombi la Huduma ya Dharura \n"
    response += "4. Ripoti ya Uchunguzi ya awali \n"
    response += "5. Hospitali / Vituo vya Afya \n"
    response += "6. Wataalam wa Afya"

  elif text == '2*1':
   try:
      #sending the sms
      sms_response = sms.send("Miadi yako ya mtandaoni imeratibiwa dd/mm/yyyy. Tafadhali beba kitambulisho chako.", sms_phone_number)
      print(sms_response)
      response = "END Utapokea SMS yenye maelezo ya miadi hivi karibuni."
   except Exception as e:
      #show us what went wrong
      print(f"Houston, we have a problem: {e}")

  elif text == '2*2':
    try:
      #sending the sms
      sms_response = sms.send("Miadi yako katika Kituo cha Afya imeratibiwa dd/mm/yyyy. Tafadhali beba kitambulisho chako.", sms_phone_number)
      print(sms_response)
      response = "END Utapokea SMS yenye maelezo ya miadi hivi karibuni."
    except Exception as e:
      #show us what went wrong
      print(f"Houston, we have a problem: {e}")

  elif text == '2*3':
    try:
      #sending the sms
      sms_response = sms.send("Opereta wa simu atakupigia simu baada ya muda mfupi. Tafadhali toa maelezo mengi uwezavyo ili yatumiwe na wahudumu wetu wa dharura.", sms_phone_number)
      print(sms_response)
      response = "END Opereta wa simu atakupigia simu baada ya muda mfupi."
    except Exception as e:
      #show us what went wrong
      print(f"Houston, we have a problem: {e}")

  elif text == '2*4':
    response = "CON Weka Nambari yako ya Kitambulisho \n"
    if text != '':
      try:
        #sending the sms
        sms_response = sms.send("RIPOTI UA UCHUNGUZI: Tafadhali jibu SMS hii kwa kitambulisho chako", sms_phone_number)
        print(sms_response)
        response = "END Utapokea SMS yenye maelekezo zaidi."
      except Exception as e:
        #show us what went wrong
        print(f"Houston, we have a problem: {e}")

  elif text == '2*5':
    response = "CON Chagua mtaalamu: \n"
    response += "1. Mtaalamu wa radiolojia \n"
    response += "2. Daktari wa macho \n"
    response += "3. Daktari wa moyo \n"
    response += "4. Daktari wa neva \n"
    response += "5. Daktari wa watoto\n"
    response += "6. Daktari wa upasuaji wa mifupa"
  
  elif text == '2*5*1':
    response = "CON Chagua kaunti unayopendelea: \n"
    response += "1. Nairobi \n"
    response += "2. Kiambu \n"
    response += "3. Garissa \n"
    response += "4. Mombasa \n"
    response += "5. Kisumu \n"
    response += "6. Machakos"

  elif text == '2*5*1*1':
    response = "END Mtaalamu aliyechaguliwa katika kaunti unayopendelea: \n"
    response += "1. MP Shah \n"
    response += "2. Kenyatta National Hospital \n"
    response += "3. Moi Teaching and Referral Hospital \n"
    response += "4. Nairobi Hospital \n"
    response += "5. Avenue Health Care \n"
    response += "6. Manugu Hospital"

  elif text == '2*6':
    response = "END Wataalam wa Afya \n"
    response += "1. Daktari wa watoto \n"
    response += "2. Daktari wa macho \n"
    response += "3. Daktari wa moyo \n"
    response += "4. Daktari wa neva \n"
    response += "5. Mtaalamu wa radiolojia \n"
    response += "6. Daktari wa upasuaji wa mifupa"

  return response 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))