import os
import time
import requests
import json
import subprocess



print(""" 

                                                                                                     
      -_____                               -_____                 
        ' | -,                               ' | -,    _          
       /| |  |`  /'\\  /'\\ \\/\\/\\  _-_,  /| |  |`  < \, '\\/\\ 
       || |==|| || || || || || || || ||_.   || |==||  /-||  || ;' 
      ~|| |  |, || || || || || || ||  ~ || ~|| |  |, (( ||  ||/   
       ~-____,  \\,/  \\,/  \\ \\ \\ ,-_-   ~-____,   \/\\  |/    
      (                                    (               (      
                                                      -_-   
                                                            
                                /\\,/\\,                          
                               /| || ||   '                       
                               || || ||  \\ \\/\\  _-_  ,._-_     
                               ||=|= ||  || || || || \\  ||       
                              ~|| || ||  || || || ||/    ||       
                               |, \\,\\, \\ \\ \\ \\,/   \\,      
                              _-
                              
                 Donate BTC 3KtPkJ5cBkuVeVfWCZNuZTUH632MsuvHoP                                  
                                                            
""")
time.sleep(3)


while True:
    diff = requests.get('https://api.blockchain.info/stats').json()['difficulty']

    if diff > 2437180461434:
        print("             Bitcoin difficulty", diff, "Damnn! still stable..")
    time.sleep(20)
    if diff < 2437180461434:
        print("Difficulty has dropped starting miner.")
        process = subprocess.Popen('/home/<user>/Desktop/doomsday-miner/doomsday-miner.sh', shell=True)
        	 																
										
								 
