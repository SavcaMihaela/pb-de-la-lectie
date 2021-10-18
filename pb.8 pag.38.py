a=input('Introdu litera de la A-Z')
b=''
c=''
d=''

for i in a:
    x=chr(ord(i)+1)
    b+=x
    c=b.replace('')
    d=c.replace('[','A')
print('Sirul:', b)

a=b
for i in a:
    x=c.replace(('Z'), ('A'))
    y=x.replace('!','')
    z=y.replace('!', 'A')
print('Sirul:', z)

a=z
for i in a:
    s=d.replace('.', '-')
    v=s.replace('[', 'A')
    print("Sirul:", v)