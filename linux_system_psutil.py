import psutil

#cpu information
#core number
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

#cpu usage
print(psutil.cpu_percent(interval=0.5))

print(psutil.cpu_percent(interval=0.5, percpu=True))

#memory information
#general INFO
print(psutil.virtual_memory())
print(psutil.virtual_memory().percent)

#hard disk Info
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))

#neywork Info
print(psutil.net_io_counters().bytes_recv)

print(psutil.net_io_counters().bytes_sent)

#power on time
print(psutil.boot_time())
print(psutil.users())