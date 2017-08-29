def systemLIVE ():
    import psutil
    print(psutil.swap_memory())
    print(psutil.cpu_count(logical=False))
#     for i in psutil.virtual_memory():
#      print(i)
systemLIVE()

