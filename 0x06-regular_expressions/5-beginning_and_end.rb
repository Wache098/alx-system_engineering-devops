#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression matching method
# The regular expression matches strings starting with 'h', ending with 'n', and having exactly one character in between

puts ARGV[0].scan(/^h.n$/).join
