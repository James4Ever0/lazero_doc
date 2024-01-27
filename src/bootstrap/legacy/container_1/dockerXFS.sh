#!/bin/bash
# not even a tty! better run away from this.
#echo parrot | sudo -S docker run --rm --kernel-memory="8m" --memory-swap="16m" --cpus="0.05" --memory="16m" --memory-reservation="8m" -it alpine sh
docker run --rm --read-only --kernel-memory="8m" --cpus="0.05" --memory="16m" --memory-reservation="8m" -it alpine sh
# better check the rootlesskit.
# this one is for service. # --storage-opt overlay2.size=0.008G
# --read-only
# if it is XFS it is way better than now.
