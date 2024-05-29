#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression matching method
# The regular expression matches specific patterns involving repetition tokens

puts ARGV[0].scan(/h(b?t)n/).join
