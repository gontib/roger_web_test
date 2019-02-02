#!/usr/bin/env bash

# Create (if needed) and activate the virtual environment
if [ ! -d "env" ]; then
    echo "Creating the virtual environment"
    virtualenv -q env
    cp bin/chromedriver env/bin/
else
    EXISTS="true"
fi

echo "Activating the virtual environment"
source env/bin/activate

# Use pip to install the requirements
{
    if [ "$EXISTS" != "true" ]; then
        echo "Installing required packages"
        pip2 install -r requirements.txt
    fi
} || { # This code with run if the previous fails
    pip install -r requirements.txt
}

echo "Running the test"
nosetests tests/cart_tests.py:Cart.test_verify_cart_contents

echo "Deactivating the environment"
deactivate