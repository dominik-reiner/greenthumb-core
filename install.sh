#!/bin/bash

# Get the directory of the install script
script_dir=$(dirname "$0")

# Register the alias
echo "alias greenthumb='python $script_dir/cli.py'" >> ~/.bashrc

# Reload the shell configuration
source ~/.bashrc

echo "Alias 'greenthumb' registered successfully!"