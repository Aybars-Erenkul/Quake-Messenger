from time import sleep
from whatsapp_api import WhatsApp
import quake_scope
from threading import Thread

# Message functions

def quake_announce():
  with open("latest_quake.txt", encoding='utf-8') as f:
    last_message = f.readline()
    last_message = last_message.split()
    #last_message = []
    #for i in range(len(last_message)):
    #  last_messagee.append(last_messagee[i])
    if len(last_message) == 9:
      last_message = last_message[0]+last_message[1] + ' ' + last_message[2]+' '+last_message[3] + ' ' + last_message[4]+' '+last_message[5] + ' ' + last_message[6]+' '+last_message[7] + ' ' + last_message[8]
    else:
      last_message = last_message[0]+last_message[1] + ' ' + last_message[2]+' '+last_message[3] + ' ' + last_message[4]+' '+last_message[5] + ' ' + last_message[6]+' '+last_message[7] + ' ' + last_message[8]+' '+last_message[9]

    print(last_message)
    f.seek(0)
    f.close()
    return last_message



# Initialize
wp = WhatsApp()


# Wait for enter to be pressed
input("Press enter after QR Code")


# List of names or phone numbers to be searched
# IMPORTANT: The name must be unambiguous as it will return the first result




while(True):
  ask = input('1)Person 2)Group : ')
  if ask == '1':
    namess = input("Enter person name: ")
  elif ask == '2':
    namess = input("Enter group name: ")
    names = namess.split()
  elif ask == 0:
    break
  else:
    break





  #wp.search_contact(namess)
  #sleep(2)
  #message = input("Enter message: ")
  #msg_reversed = message[::-1]

  #number_of_tims = input('How many times to send: ')
  #i = 0
  #while (i < int(number_of_tims)):
  #  wp.send_message(message)
  #  i = i + 1
  temp = 'message'
  last_message = "test" 
  #last_message = wp.get_last_message()
  #wp.send_message(message)

  activated = False

  last_message = quake_announce()


  while(True):
    for name in names:
      wp.search_contact(name)
      sleep(2)
      temp = last_message
      
      last_message = wp.get_last_message()

      if(last_message == "!quit"):
        wp.send_message("*_Artik bu chate bakmiyorum_*")
        names.remove(name)
      elif(last_message == "!deprem"):
        deprem = quake_announce()
        wp.send_message(deprem)
        sleep(1)
        activated = True
      elif(last_message == "! deprem"):
        deprem = quake_announce()
        wp.send_message(deprem)
        sleep(1)
        activated = True
      
      elif(last_message == "! Deprem"):
        deprem = quake_announce()
        wp.send_message(deprem)
        sleep(1)
        activated = True


      else:
        pass 
      if activated == False:
        continue

      if last_message != temp:
        temp = last_message
        
        last_message = wp.get_last_message()
        print(last_message)
      else:
        continue


  # Wait 10 seconds and close
  sleep(10)
wp.driver.close()
