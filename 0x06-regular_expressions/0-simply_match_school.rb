#!/usr/bin/env ruby

# This script accepts one argument and passes it to a regular expression matching method
# The regular expression must match "School"

# Extract the argument provided
input_string = ARGV[0]

# Define the regular expression pattern to match "School"
pattern = /School/

# Check if the input string matches the pattern
if input_string.match?(pattern)
  puts input_string
else
  puts "No match"
end
