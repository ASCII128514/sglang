#! /bin/bash


# launch majority workloads
for i in {0..3}
do
    python client.py --pos $((i*3000)) --max_new_tokens 1 --n 20 --interval 0.3 > shell_$i.log &
done


# launch minority workloads
for i in {4..20}
do
    python client.py --pos $((15000-1000+i*200)) --max_new_tokens 128 --n 20 --interval 5 > shell_$i.log &
done
