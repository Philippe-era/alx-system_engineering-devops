#!/usr/bin/env ruby
SEND = ARGV[0].scan(/from:\+*\w*/).join[5..-1]
RESPONSE = ARGV[0].scan(/to:\+*\w*/).join[3..-1]
PATTERN = ARGV[0].scan(/flags:(.*?)\]/).join

text_reply = SEND + "," + RESPONSE + "," + PATTERN
puts text_reply
