from datetime import datetime
import time
for _ in range(10):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
