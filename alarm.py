from datetime import datetime
import time
import pytz
from playsound import playsound

def get_CT():
    current_time = datetime.now(pytz.timezone('Asia/Jakarta'))
    return current_time

print(get_CT())