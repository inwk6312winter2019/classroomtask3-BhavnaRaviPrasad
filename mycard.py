"""rank=[1,2,3,4,5,6,7,8,9,10,11,12,13]
suite=["h","s","d","c"]

cards=list(zip(rank,suite))
#populate the card list
card=[]
for ranks in rank:
  cards=cards+[(ranks,suite[0]),(ranks,suite[1]),(ranks.suite[2])]


print(cards)
"""

class card():
suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

 def __init__(self,rank=0,suite=2):
    self.rank=rank
    self.suite=suite


 def __str__(self):
return f"the rankis {card.rank_names[self.rank]} and the suite is {card.suite_name[self.suite]}"

ace_of_spades=cards(1,3)

print(ace_of_spades)

