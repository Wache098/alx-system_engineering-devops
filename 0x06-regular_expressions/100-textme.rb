#!/usr/bin/env ruby

# This script accepts one argument and passes it to a regular expression matching method
# The script should output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

# Extract sender, receiver, and flags using regular expressions
sender = ARGV[0].scan(/(?<=\[from:)([^\[\]]+)(?=\])/).join
receiver = ARGV[0].scan(/(?<=\[to:)([^\[\]]+)(?=\])/).join
flags = ARGV[0].scan(/(?<=\[flags:)([^\[\]]+)(?=\])/).join

# Output the extracted sender, receiver, and flags
puts "#{sender},#{receiver},#{flags}"
