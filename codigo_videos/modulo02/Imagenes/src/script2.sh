#!/bin/bash

# Script to print all arguments

echo "Number of arguments: $#"
echo "All arguments:"
echo "$@"

# Alternative way to print each argument on a separate line
echo -e "\nArguments one per line:"
for arg in "$@"; do
  echo "$arg"
done

# Another alternative showing argument positions
echo -e "\nArguments with positions:"
count=1
for arg in "$@"; do
  echo "Argument $count: $arg"
  ((count++))
done