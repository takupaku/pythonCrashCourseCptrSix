cities={
    'dhaka':{
        'country':'bangladesh',
        'population':'20.628 Million',
        'fact':'eighth most populated country',
    },
    'tokyo':{
        'country':'japan',
        'population':'13.9 million',
        'fact':'technologically improved',

    },
    'macca':{
        'country':'kingdom of saudi arabia',
        'population':'1.535 million',
        'fact':'prophet muhammad(pbuh) birth place',

    },
}
for k,v in cities.items():
    print('\ncity: '+k)
    print("country:"+v['country'].title())
    print("population:" + v['population'])
    print("fact:" + v['fact'])

