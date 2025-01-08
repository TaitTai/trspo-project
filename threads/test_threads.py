import threading
from joke.services import print_random_joke
from random_tasks import run_random_task


thread1 = threading.Thread(target=print_random_joke)
thread2 = threading.Thread(target=run_random_task)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
