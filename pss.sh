#!/bin/bash

# Define the length of the password
LENGTH=16

# Generate a random alphanumeric password
PASSWORD=$(head /dev/urandom | tr -dc 'A-Za-z0-9' | head -c "$LENGTH")

echo "Your random password: $PASSWORD"
