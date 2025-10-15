#!/bin/bash
ip link show ens3 | head -n 2 | tail -n 1 | tr -s ' ' | cut -d ' ' -f3

