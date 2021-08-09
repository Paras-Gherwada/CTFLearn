#CTFlearn{xor_is_your_friend}
c1="Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo="
c2="xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
c3="h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

c1=c1.decode("base64")
c2=c2.decode("base64")
c3=c3.decode("base64")


print c1," ",len(c1)
print c2," ",len(c2)
print c3," ",len(c3)

val=""
for i in range(30):
    val+=chr(ord(c2[i])^ord(c3[i]))

print val
