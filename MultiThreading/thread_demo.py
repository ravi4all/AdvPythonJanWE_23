import threading

# thread - lightweight program

def job():
    print(f"Job Started by {threading.current_thread().name}...")
    for i in range(1,6):
        print("I is :",i)
    print(f"Job Done by {threading.current_thread().name}...")


worker_1 = threading.Thread(target=job, name="John")
worker_2 = threading.Thread(target=job, name="Sam")
worker_3 = threading.Thread(target=job, name="Max")

worker_1.start()
worker_2.start()
worker_3.start()