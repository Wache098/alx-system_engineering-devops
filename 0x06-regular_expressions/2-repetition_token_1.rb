#!/usr/bin/env ruby

# This script accepts one argument and passes it to a regular expression matching method
# The regular expression matches "hbtn" followed by one or more occurrences of "t"

# Extract the argument provided
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /hbt+n/

# Check if the input string matches the pattern
if input_string.match?(pattern)
  puts input_string
else
  puts "No match"
end
