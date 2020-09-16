favourite_places={
    'maki':['tokyo','akihabra'],
    'taku':['uttara','saint martin'],
    'echizen':['yokohama','nagoya','hiroshima'],
}
for k,v in favourite_places.items():
    print(k+"'s fav places are: ")
    for places in v:
        print("\t"+places.title())