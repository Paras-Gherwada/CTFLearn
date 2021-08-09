card_init="543210"
card_mid=""
card_end="1234"

def validate(card):
    card_int=[int(i) for i in card]
    for i in range(0,len(card_int),2):
        temp=card_int[i]*2
        if temp>9:
            val=[int(x) for x in str(temp)]
            card_int[i]=sum(val)
        else:
            card_int[i]=temp
    if sum(card_int)%10==0 and int(card)%123457==0:
        return card

for i in range(0,1000000):
    if i<10:
        card_mid="0"*5
    elif i<100:
        card_mid="0"*4
    elif i<1000:
        card_mid="0"*3
    elif i<10000:
        card_mid="0"*2
    elif i<100000:
        card_mid="0"
    else:
        card_mid=""
    card_mid=card_mid+str(i)
    card=validate(card_init+card_mid+card_end)
    if card!=None:
        print card
