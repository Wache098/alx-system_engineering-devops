#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression matching method
# The regular expression matches specific patterns involving repeated characters

puts ARGV[0].scan(/hbt{2,5}n/).join
