def infoSYS ():
    import platform
    print("Your system info \n"+
          "System Operation: "+ platform.platform()+"\n"
          "Processor: " + platform.processor() +"\n"
          "Machine: " + platform.processor()+'\n'
          "Node: " + platform.node()+ '\n'
          'System: ' + platform.system() +'\n'
          
            )



infoSYS()

