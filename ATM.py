pin = int(input('PLEASE ENTER YOUR PIN: '))
def Atm() :
    import os
    os.system('cls')
    print('----------TRANSACTION TYPE---------- \n')
    print('''
        1.CURRENT
        2.SAVINGS
        ''')
    choice_transactionType = int(input('TRANSACTION TYPE: '))
    if choice_transactionType == 1:
        import os
        os.system('cls')
        print('----------MAIN MENU---------- \n')
        print('''
            1.WITHDRAW                   2.PIN CHANGE           
            ''')
        choice_mainMenu = int(input('WHAT OPTION ARE YOU HERE FOR: '))
        if choice_mainMenu == 1:
            import os
            os.system('cls')
            print('----------SELECT TRANSACTION AMOUNT---------- \n')
            print('''
                    1. 10,000
                    2. 20,000
                    3  other amount            
                        ''')
            choice_transactionAmount = int(input('TRANSACTION AMOUNT: '))
            if choice_transactionAmount == 1:
                print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                import pyttsx3
                engine = pyttsx3.init()
                engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                engine.runAndWait()
                speaker = pyttsx3.init()
                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 100)
                # volume
                volume = engine.getProperty('volume')
                engine.setProperty('volume',1.0)
                # voice
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                import time
                time.sleep(6)
                print('Your money (#10000) has been processed to you. Please take your card') 
            elif choice_transactionAmount == 2:
                print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                import pyttsx3
                engine = pyttsx3.init()
                engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                engine.runAndWait()
                speaker = pyttsx3.init()
                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 100)
                # volume
                volume = engine.getProperty('volume')
                engine.setProperty('volume',1.0)
                # voice
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                import time
                time.sleep(6)
                print('Your money (#10000) has been processed to you. Please take your card') 
            elif choice_transactionAmount == 3:
                print('ENTER THE MULTIPLE OF #500 OR #1000')
                amt = int(input('>> ')) 
                print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                import pyttsx3
                engine = pyttsx3.init()
                engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                engine.runAndWait()
                speaker = pyttsx3.init()
                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 100)
                # volume
                volume = engine.getProperty('volume')
                engine.setProperty('volume',1.0)
                # voice
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                import time
                time.sleep(6)
                print(f'Your money #{amt} has been processed to you. Please take your card') 
        elif choice_mainMenu == 2 :
            new_pin = int(input('ENTER YOUR NEW PIN')) 
            import os
            os.system('cls') 
            confirm_newPin = int(input('CONFIRM YOUR NEW PIN'))
            import os
            os.system('cls')
            print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
            import pyttsx3
            engine = pyttsx3.init()
            engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
            engine.runAndWait()
            speaker = pyttsx3.init()
            rate = speaker.getProperty('rate')   
            speaker.setProperty('rate', 100)
            # volume
            volume = engine.getProperty('volume')
            engine.setProperty('volume',1.0)
            # voice
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice', voices[1].id)
            import time
            time.sleep(6)  
            import os
            os.system('cls')  
            print('''
                            CHANGE PIN 
                    YOUR PIN HAS BEEN CHANGED
                  THANK YOU FOR BANKING WITH US
        ''')
            exit()
    elif choice_transactionType == 2:
        import os
        os.system('cls')
        print('----------MAIN MENU---------- \n')
        print('''
            1.WITHDRAW                   2.PIN CHANGE           
            ''')
        choice_mainMenu = int(input('WHAT OPTION ARE YOU HERE FOR: '))
        if choice_mainMenu == 1:
            import os
            os.system('cls')
            print('----------SELECT TRANSACTION AMOUNT---------- \n')
            print('''
                    1. 10,000
                    2. 20,000
                    3  other amount            
                        ''')
            choice_transactionAmount = int(input('TRANSACTION AMOUNT: '))
            if choice_transactionAmount == 1:
                print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                import pyttsx3
                engine = pyttsx3.init()
                engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                engine.runAndWait()
                speaker = pyttsx3.init()
                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 100)
                # volume
                volume = engine.getProperty('volume')
                engine.setProperty('volume',1.0)
                # voice
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                import time
                time.sleep(6)
                print('Your money (#10000) has been processed to you. Please take your card') 
            elif choice_transactionAmount == 2:
                print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                import pyttsx3
                engine = pyttsx3.init()
                engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                engine.runAndWait()
                speaker = pyttsx3.init()
                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 100)
                # volume
                volume = engine.getProperty('volume')
                engine.setProperty('volume',1.0)
                # voice
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                import time
                time.sleep(6)
                print('Your money (#10000) has been processed to you. Please take your card') 
            elif choice_transactionAmount == 3:
                print('ENTER THE MULTIPLE OF #500 OR #1000')
                amt = int(input('>> ')) 
                print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                import pyttsx3
                engine = pyttsx3.init()
                engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
                engine.runAndWait()
                speaker = pyttsx3.init()
                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 100)
                # volume
                volume = engine.getProperty('volume')
                engine.setProperty('volume',1.0)
                # voice
                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                import time
                time.sleep(6)
                print(f'Your money #{amt} has been processed to you. Please take your card') 
        elif choice_mainMenu == 2 :
            new_pin = int(input('ENTER YOUR NEW PIN')) 
            import os
            os.system('cls') 
            confirm_newPin = int(input('CONFIRM YOUR NEW PIN'))
            import os
            os.system('cls')
            print('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
            import pyttsx3
            engine = pyttsx3.init()
            engine.say('PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED')
            engine.runAndWait()
            speaker = pyttsx3.init()
            rate = speaker.getProperty('rate')   
            speaker.setProperty('rate', 100)
            # volume
            volume = engine.getProperty('volume')
            engine.setProperty('volume',1.0)
            # voice   
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice', voices[1].id)
            import time
            time.sleep(6)  
            import os
            os.system('cls')  
            print('''
                            CHANGE PIN 
                    YOUR PIN HAS BEEN CHANGED
                  THANK YOU FOR BANKING WITH US
        ''')
            exit()
    
if pin == 2345:
    Atm()
else :
    count = 0
    count_limit = 3
    print('Try again')
    while count < count_limit :
        retry_pin = int(input('ENTER YOUR PIN AGAIN: '))
        if retry_pin == 2345 :
            Atm()
            exit()    
        else :
         print('Wrong password!') 
        count += 1 
    print("You've been logged out.😔 ")
    print('You have to wait for three minutes and try again')
    
         
     
     