#used psutil libary

def systemLIVE ():
    import psutil
    print(psutil.swap_memory())
    print(psutil.cpu_count(logical=False))
systemLIVE()

