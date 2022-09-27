import Random_Responses
from datetime import datetime

def sample_responses(input_text):
    user_message =  str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "hey", "what's up", "yo", "wassup", "wassup bro", "wassup dude", "wassup"):
            return "Heyy! How are you?"

    if user_message in("how are you", "how are you doing", "how are you doing today", "how are you doing today?"):
        return "I'm doing great!"        
            
    if user_message in ("see you", "goodbye", "bye", 'cya', 'ttyl', 'talk to you later', 'see you later', 'see ya', 'see ya later', 'see you soon', 'see ya soon', 'talk to you soon', 'talk to you later'):
            return "See you later!"

    if user_message in ("i'm fine", "fine", "i'm fine", "i am fine", "i'm good", "good", "i'm good", "i am good", "i'm doing good", "i am doing good", "i'm doing fine", "i am doing fine"):
            return "Ahh that's great! Any way I can help you?"

    if user_message in ("who are you", "who are you?", "who created you", "who created you?", "who made you", "who made you?", "who is your creator", "who is your creator?", "who is your maker", "who is your maker?"):
            return "I am a bot created by Farhaan"

    if user_message in ("time", "time?", "what time is it", "what time is it?", "what's the time", "what's the time?"):
            now = datetime.now()
            date_time = now.strftime("%d/%m/%y, %H:%M:%S")

            return str(date_time)

    return Random_Responses.random_string()