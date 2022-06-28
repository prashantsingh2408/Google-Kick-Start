=begin
2
7 3
1 2 3 4 5 6 7
5 10
7 7 7 7 7

Output 
Case #1: 1
Case #2: 5
=end

T = gets.to_i

T.times do |t|
  candy, bag = gets.split.map(&:to_i)
  candy_arr = gets.split.map(&:to_i)
  bag_arr = gets.split.map(&:to_i)
end
#sum
puts candy_arr.inject(:+)

  


