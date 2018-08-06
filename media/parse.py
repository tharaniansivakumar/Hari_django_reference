import xmltodict
import json

f=open("details.json","w");
x=xmltodict.parse('''

     <root>

       <persons city="hyderabad">

         <person name="abc">

           <name age="50" mobile="789" />

         </person>

       </persons>

       <persons city="vizag">

            <username></username>

         <person name="xyz">

           <name age="70" mobile="123" />

         </person>

       </persons>

     </root>

     ''')
#f.write(json.dumps(x,indent=4))
json.dump(x,f,indent=4)
f.close()
f=open("details.json","r")
a=json.load(f)
print(type(a))
print(xmltodict.unparse(a, pretty=True))
