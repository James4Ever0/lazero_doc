#!/bin/bash
docker run --read-only --rm --kernel-memory="8m" --memory-swap="16m" --cpus="0.05" --memory="16m" --memory-reservation="8m" -it alpine sh
# --read-only
# if it is XFS it is way better than now.
