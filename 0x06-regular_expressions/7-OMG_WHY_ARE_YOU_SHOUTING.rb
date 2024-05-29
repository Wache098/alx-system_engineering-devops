#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression matching method
# The regular expression matches and extracts only capital letters

puts ARGV[0].scan(/[A-Z]/).join
