# doomsday-miner
# This is my code bitch do not copy unless you give me credit or donate.

My python program that monitors BTC difficulty and starts miner if there is sudden drop in diff. Basically this would work if there were some kind of disaster scenario where most or all Bitcoin mining operations were destroyed or shut down. In theory this could work as for the Bitcoin difficulty would decrease significantly which will activate the miner.

Works with AMD gpu/wildrig or cpu miner option.

To use type 
* $ cd doomsday-miner
* $ source tool/bin/activate
* $ python3 doomsday.py

Make sure to change any necessary info
Change line 46 in doomsday.py to your user and preferance GPU (gpu-doomsday-miner.sh) or CPU (miner-cpu-btc.sh). 

And if you get any block rewards from this please donate some! 3KtPkJ5cBkuVeVfWCZNuZTUH632MsuvHoP

Would like to thank and credit these Developers for the mining applications that made this possible. 
Andrew Kuhn for wildrig miner
Rplant for his cpuminer
