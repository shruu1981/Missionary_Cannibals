# Missionary_Cannibals
# Using basic python
boat_side='Right'
missionaries_on_right=3
cannibals_on_right=3
missionaries_on_left=0
cannibals_on_left=0
print("M =",missionaries_on_left,"C =",cannibals_on_left,"|-----B|","M =",missionaries_on_right,"C =",cannibals_on_right)
while True:
  missionaries=int(input("Enter the no. of missionaries on boat: "))
  cannibals=int(input("Enter no. of cannibals on boat: "))
  total_traveller=missionaries+cannibals
  if total_traveller<1 or total_traveller>2:
    print("Invalid move1")
    continue
  if boat_side=='Right':
    if missionaries+cannibals > missionaries_on_right+cannibals_on_right:
      print("Invalid move 2")
      continue
    missionaries_on_right=missionaries_on_right-missionaries
    cannibals_on_right=cannibals_on_right-cannibals
    missionaries_on_left=missionaries_on_left+missionaries
    cannibals_on_left=cannibals_on_left+cannibals
    boat_side='left'
    print("M =",missionaries_on_left,"C =",cannibals_on_left,"|B-----|","M =",missionaries_on_right,"C =",cannibals_on_right)
  elif boat_side=='left':
    print("B-----")
    if missionaries_on_left<missionaries or cannibals_on_left<cannibals:
      print("Invalid move 2")
      continue
    missionaries_on_right=missionaries_on_right+missionaries
    cannibals_on_right=cannibals_on_right+cannibals
    missionaries_on_left=missionaries_on_left-missionaries
    cannibals_on_left=cannibals_on_left-cannibals
    boat_side='Right'
    print("M =",missionaries_on_left,"C =",cannibals_on_left,"|-----B|","M =",missionaries_on_right,"C =",cannibals_on_right)
  if cannibals_on_right>missionaries_on_right and missionaries_on_right>0:
    print("you lose")
    break
  if cannibals_on_left>missionaries_on_left and missionaries_on_left>0:
    print("you lose")
    break
  if missionaries_on_left==3 and cannibals_on_left==3:
    print("you win")
    break
