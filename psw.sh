#!/bin/bash

# Generate a random password with 16 characters
password=$(openssl rand -base64 16)

echo "Your random password: $password"
