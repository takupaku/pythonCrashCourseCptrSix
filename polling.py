polling={
    'jen':'python',
    'sarah':'C',
    'edword':'ruby',
    'phill':'python',

}

name=['jen','sarah','edword','phill','taku','maki']
for n in name:
    print("dear,"+n+" please take the poll.")
    
print("\n")

for k,v in polling.items():
    print(k+"'s "+"fav language is "+v+".")
    print("thank you for taking the poll.\n")
for n in name:
    if n not in polling.keys():
        print(n+" please take the poll.")


