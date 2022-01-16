#!/bin/sh
#
# Choose nearest stratum:
#       stratum-ru.rplant.xyz   /Moscow/
#       stratum-eu.rplant.xyz   /London/
#       stratum-asia.rplant.xyz /Singapore/
#       stratum-na.rplant.xyz   /Toronto/
#
while [ 1 ]; do
./cpuminer-sse2 -a sha256d -o stratum+tcp://stratum.solomining.io:7777 -u 35NU7PRg3YzyFHBBUM6RQNTyvXY8PADfk6 -t 3 -p x
sleep 5
done
