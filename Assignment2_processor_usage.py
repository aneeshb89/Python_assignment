import psutil

a = 0
x = psutil.cpu_count()
print(f"No of cores of the cpus is {x}")

while True:
 y = psutil.cpu_percent(interval=3, percpu=None)
 print(f"Cpu usage is {y:.2f}%")
 if y > 15:
  print(f"CPU usage is {y:.2f}% and it exceeds threshold of 15%")
  
 


