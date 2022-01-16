#!/bin/bash

while true
do
./wildrig-multi --algo sha256d --opencl-threads auto --opencl-launch auto --url stratum.solomining.io:7777 --user 35NU7PRg3YzyFHBBUM6RQNTyvXY8PADfk6 --pass x --opencl-devices=0,1 --opencl-threads=3
sleep 5
done
