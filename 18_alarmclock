from datetime import datetime
import time
alarm = input("Set alarm HH:MM (24h format): ")
print(f"Alarm set for {alarm}")
while True:
    now = datetime.now().strftime("%H:%M")
    if now==alarm:
        print("WAKE UP! ALARM!")
        break
    time.sleep(20)
