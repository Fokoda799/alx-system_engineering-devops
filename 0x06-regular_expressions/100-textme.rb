#!/usr/bin/env ruby

pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
data = ARGV[0].match(pattern)
result = "#{data[1]},#{data[2]},#{data[3]}"
puts result
