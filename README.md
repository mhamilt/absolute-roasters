# ![Absolute Roasters](img/logo.png)

**A data set of UK Coffee Roasters**

## Usage

For JSON format, query the following URL

```
https://raw.githubusercontent.com/mhamilt/absolute-roasters/main/absolute_roasters.json
```

Data set is an array of coffee roaster objects, which at a minimum should contain

```json
{
  "name": "Roaster Name",
  "url": "https://roaster.url",
  "location": "business address"
}
```

### Optional keys

entries may include extra keys

```json
{
  "coord": [54.665, -2.228],
  "facebook": "facebook_handle",
  "instagram": "instagram_handle",
  "twitter": "@twitterHandle",
  "profile_image_url": "url",
  "description": "business description"
}
```

```geojson
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "properties": {
      "location": "Heston House, Meadow Lane, Nottingham, NG2 3HE",
      "name": "200 Degrees Coffee",
      "updated_at": "2020-06-15 09:32:27 UTC",
      "url": "https://200degs.com/",
      "twitter": "@200Degs",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1361, 52.942]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "3FE Coffee",
      "url": "http://3fe.com",
      "location": "32/34 Lower Grand Canal St, Dublin, Ireland",
      "profile_image_url": "static.squarespace.com/static/541188fee4b09a04d20e1ad3/t/54521507e4b008c5dd78c382/1418467422164/?format=1500w",
      "updated_at": "06-May-2015 15:49",
      "twitter": "@3FE",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.242, 53.3399]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "11 Victoria Avenue, Heanor, Derbyshire, DE75 7SA",
      "name": "47 degrees coffee",
      "updated_at": "2020-06-16 04:35:25 UTC",
      "url": "https://47degreescoffee.com/",
      "twitter": "@47degreescoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3673, 53.0137]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "80 Stone Coffee Roasters",
      "url": "https://80stonecoffeeroasters.co.uk/",
      "location": "512 Fulham road, London, SW6 5NJ",
      "profile_image_url": "https://pbs.twimg.com/profile_images/1092128400796516352/mrGuM1j1_400x400.jpg",
      "updated_at": "02-May-2019 20:30",
      "twitter": "@80stonecoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1991, 51.4797]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "10 Old Market Centre, Gillingham, Dorset, SP8 4QQ",
      "name": "918 Coffee",
      "updated_at": "2020-06-10 10:04:17 UTC",
      "url": "https://www.918coffee.com/",
      "twitter": "@918_Coffee_Co",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2712, 51.035]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "92degreescoffee",
      "url": "https://facebook.com/92DegreesCoffee",
      "location": "24 Hardman Street, Liverpool, Merseyside, L1 9AX",
      "profile_image_url": "pbs.twimg.com/profile_images/525291991282626561/18y3PYue_400x400.png",
      "updated_at": "10-Nov-2015 09:02",
      "twitter": "@92degreescoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.9713, 53.4015]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "48 Appin Road, Argyle Industrial Estate, Birkenhead, Merseyside, CH41 9HH",
      "name": "Adams & Russell",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/adams-and-russell-logo.png?1028",
      "updated_at": "2019-07-30 08:56:30 UTC",
      "url": "https://www.adamsandrussell.co.uk/",
      "twitter": "@adamsandrussell",
      "facebook": "adamsandrussell",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.021, 53.3854]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Alchemy Coffee",
      "url": "https://alchemycoffee.co.uk/",
      "location": "Unit 14-16, Riverside Business Park, Lyon Road, London, SW19 2RL",
      "profile_image_url": "www.alchemycoffee.co.uk/skin/frontend/alchemy/default/images/logo.png",
      "updated_at": "06-May-2015 15:31",
      "twitter": "@alchemy_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1851, 51.4132]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Allegro Coffee UK",
      "description": "Allegro Coffee was founded in Boulder, Colorado, USA in 1977, with the simple goal to bring you the best coffees in the world. In the decades since, we have merged with Whole Foods Market, moved our offices to a larger facility in the outskirts of nearby Denver, and expanded our product line to include fine tea, wellness tea, and drinking chocolate\u2014all with an emphasis on organic and sustainably grown ingredients. Through all this growth and change, our initial goal has remained the same: from coffee beans to tea leaves, herbs, botanicals, and chocolate\u2014 we passionately and continually source the best ingredients the world has to offer.",
      "location": "63 - 97 Kensington High Street, London, W8 5SE",
      "handle": "allegro-coffee-uk",
      "url": "https://www.allegrocoffee.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1908, 51.5016]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Allpress Espresso UK",
      "url": "https://uk.allpressespresso.com:443/",
      "location": "58, Redchurch Street,  London, E2 7DP",
      "profile_image_url": "https://instagram.fmxp1-1.fna.fbcdn.net/vp/405d0787503fcee1b639a1c3e386deac/5D559F3A/t51.2885-19/s150x150/21689356_500380583627978_847256743804141568_n.jpg?_nc_ht=instagram.fmxp1-1.fna.fbcdn.net",
      "updated_at": "02-May-2019 20:36",
      "twitter": "@AllpressE2",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0745, 51.5244]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "59 Silver Street, Lyme Regis, Devon, DT7 3TZ",
      "name": "Amid Giants & Idols",
      "profile_image_url": "https://daks2k3a4ib2z.cloudfront.net/5884eaca0ceec0701f3a4b86/589a45dee0f4d2b73b1f0eba_Logo%20Dark-p-500x500.png",
      "updated_at": "2019-11-17 18:10:44 UTC",
      "url": "http://www.amidgiantsandidols.co.uk",
      "twitter": "@AndAnnex",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.9374, 50.7256]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 1, Crown Ind Est, Poland street, Ancoats, Manchester, M4 6BN",
      "name": "Ancoats Coffee Co.",
      "profile_image_url": "http://www.ancoats-coffee.co.uk/wp-content/themes/AncoatsCoffee/images/ancoats-coffee-logo.jpg",
      "updated_at": "2019-07-04 16:57:42 UTC",
      "url": "https://www.ancoats-coffee.co.uk/",
      "twitter": "@ancoatscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2254, 53.4872]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "472 Long Lane, East Finchley, London, N2 8JL",
      "name": "Angelucci Coffee",
      "updated_at": "2020-06-11 04:19:44 UTC",
      "url": "https://angeluccicoffee.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1724, 51.5932]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Basingstoke, Hampshire",
      "name": "Anvil Coffee",
      "updated_at": "2020-06-10 09:56:52 UTC",
      "url": "https://www.anvilcoffee.co.uk",
      "twitter": "@AnvilCoffee",
      "facebook": "ANVILCoffee",
      "instagram": "anvilcoffeeuk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.0924, 51.2665]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Ariosa coffee",
      "url": "https://ariosacoffee.com/",
      "location": "Borranstown, Ashbourne, Co. Meath, Ireland",
      "profile_image_url": "pbs.twimg.com/profile_images/478137195921162240/2pyQakhc_400x400.jpeg",
      "updated_at": "06-May-2015 15:35",
      "twitter": "@Ariosacoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.4066, 53.5178]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "4 Hotspur Park, Knights Way, Battlefield Enterprise Park, Shrewsbury, Shropshire , SY1 3FB",
      "name": "Aroma Tea & Coffee",
      "updated_at": "2019-12-19 17:56:48 UTC",
      "url": "http://www.aroma-coffee.co.uk",
      "twitter": "@AromaTeaCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7378, 52.7467]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "57 Broughton Street, Edinburgh, Scotland, EH1 3RJ",
      "name": "Artisan Roast",
      "updated_at": "2020-08-24 04:54:56 UTC",
      "url": "https://www.artisanroast.co.uk",
      "twitter": "@artisanroast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.189, 55.9581]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Astrora Coffee",
      "description": "a speciality coffee micro roastery & retailer",
      "location": "31 Broad Street, Teddington, Middlesex, TW11 8QZ",
      "twitter": "@astroracoffee",
      "handle": "astrora-coffee",
      "url": "http://astrora.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.3375, 51.426]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Badger & Dodo",
      "url": "https://badgeranddodo.ie/",
      "location": "Each Saturday, Douglas Farmers Market, Douglas, Cork, Ireland",
      "profile_image_url": "pbs.twimg.com/profile_images/1947185010/Twitterblk_400x400.jpg",
      "updated_at": "06-May-2015 15:38",
      "twitter": "@BadgerAndDodo",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-8.4336, 51.875]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "27 Stockman\u2019s Way, Belfast, Northern Ireland, BT9 7ET",
      "name": "Bailies Coffee",
      "updated_at": "2020-06-28 02:42:28 UTC",
      "url": "https://www.bailiescoffee.com/",
      "twitter": "@bailiescoffeeco",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.8965, 54.6288]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Balance Coffee",
      "updated_at": "2020-05-21 04:02:28 UTC",
      "url": "https://balancecoffee.co.uk",
      "location": "London, EC1V 2NX",
      "twitter": "@BalanceCoffeeUK",
      "instagram": "@BalanceCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0893, 51.5274]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "92 English Row, Celbridge, Co Kildare, Ireland",
      "name": "Baobab Coffee Roasters",
      "updated_at": "2020-06-28 04:12:32 UTC",
      "url": "http://baobab.ie",
      "twitter": "@BaobabRoasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.5405, 53.3378]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bean & Ground",
      "description": "Discover freshly roasted coffee, delivered. Two different varieties from around the world with each delivery, straight through your door.",
      "location": "London, UK",
      "twitter": "@beanandground",
      "handle": "bean-and-ground",
      "url": "http://beanandground.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Fairfield Mills, Queen Street South, Huddersfield, West Yorkshire, HD1 3DX",
      "name": "Bean Brothers",
      "updated_at": "2020-06-28 02:03:00 UTC",
      "url": "https://www.beanbrothers.co.uk/",
      "twitter": "@beanbrothersLtd",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.785, 53.6458]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bean enCounter",
      "url": "https://www.facebook.com/beanencounterltd",
      "location": "Salter Street, Stafford, Staffordshire, ST16 2JU",
      "profile_image_url": "www.beanencounter.co.uk/wp-content/uploads/2014/01/beanlogoonly-copy-277x300.jpg",
      "updated_at": "06-May-2015 15:56",
      "twitter": "@BeanEnCounter",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1164, 52.8078]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "bean miles",
      "url": "https://www.beanmiles.co.uk/",
      "location": "Wetheral, Carlisle, Cumbria",
      "profile_image_url": "pbs.twimg.com/profile_images/457830333572849664/_usmbAsC_400x400.jpeg",
      "updated_at": "06-May-2015 16:02",
      "twitter": "@BeanMiles",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8334, 54.8818]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, Old Mill Business Park, Station Road, Brunton, Somerset, BA10 0EH",
      "name": "Bean Shot Coffee",
      "updated_at": "2019-12-21 16:37:52 UTC",
      "url": "https://www.beanshot.co.uk/",
      "twitter": "@BeanShotCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.4488, 51.1119]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bean Smitten",
      "url": "https://www.beansmitten.co.uk/",
      "location": "Cedar Gables, Hastings Road, Flimwell, East Sussex, TN5 7QA",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/bean-smitten.jpg",
      "updated_at": "06-May-2015 15:47",
      "twitter": "@BeanSmitten",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.4187, 51.0765]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "13a Boundary Business Centre, Boundary Way, Woking, Surrey, GU21 5DH",
      "name": "Beanberry Coffee Company",
      "updated_at": "2020-06-28 02:31:07 UTC",
      "url": "https://www.beanberrycoffee.com/",
      "twitter": "@beanberrycoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5445, 51.3263]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Beanheroes",
      "url": "http://www.beanheroes.co.uk",
      "location": "Sterling House Cheadle Court, 5 \u2013 7 Turves Road, Cheadle Hulme, Cheshire, SK8 6AW",
      "profile_image_url": "pbs.twimg.com/profile_images/560114616890425344/dMP6o7IH_400x400.jpeg",
      "updated_at": "06-May-2015 15:57",
      "twitter": "@Beanheroes",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2067, 53.3734]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Beans and Leaves",
      "url": "http://www.beansandleaveswolves.co.uk",
      "location": "Wolverhampton, West Midlands",
      "profile_image_url": "pbs.twimg.com/profile_images/480672745563246592/2D-13b0W_400x400.jpeg",
      "updated_at": "06-May-2015 15:36",
      "twitter": "@beansleaves",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1288, 52.587]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Beanworks",
      "url": "http://thebeanworks.co.uk/",
      "location": "The Roastery, 5 Viking Business Centre, High Street, Woodville, Derbyshire, DE11 7EH",
      "profile_image_url": "http://media.designersfriend.co.uk/beanworks/img/logo.png",
      "updated_at": "11-Jun-2017 18:16",
      "twitter": "@beanworks",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5335, 52.7689]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "39 Grove Rd, Eastbourne, East Sussex, BN21 4TX",
      "name": "Beanzz Coffee",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/collections/beanzz-logo_medium.JPG",
      "updated_at": "2019-11-17 18:01:57 UTC",
      "url": "http:///collections/beanzz-coffee-eastbourne",
      "twitter": "@BeanzzCoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.2791, 50.7678]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Mullingar, Co Westmeath, Ireland",
      "name": "Bell Lane Coffee",
      "updated_at": "2020-06-28 01:49:06 UTC",
      "url": "https://www.belllane.ie",
      "twitter": "@BellLaneCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-7.3381, 53.5259]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bella Barista",
      "url": "https://www.bellabarista.co.uk/",
      "location": "Northamptonshire, NN8 1LD",
      "profile_image_url": "pbs.twimg.com/profile_images/351001101/logo_400x400.jpg",
      "updated_at": "06-May-2015 15:48",
      "twitter": "@bellabarista",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.6761, 52.2963]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bewley's Ireland",
      "url": "http://bewleys.com/",
      "location": "78/79 Grafton Street, Dublin, Ireland",
      "profile_image_url": "bewleys.com/wp-content/themes/bewleys/images/layout/header_logo.png",
      "updated_at": "06-May-2015 15:48",
      "twitter": "@BewleysIreland",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2604, 53.3417]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Big Nose Coffee Company",
      "description": "Freshly Roasted Arabica Coffee Beans, Home Grinders and Aeropress.",
      "location": "Unit A & B Station Yard Norbiton Station, Coombe Road, Kingston Upon Thames, Surrey, KT2 7AZ",
      "twitter": "@BigNoseCoffee",
      "handle": "big-nose-coffee-company",
      "url": "http://bignosecoffeecompany.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2833, 51.4127]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Arena Business Centre, 9 Nimrod Way, Ferndown, Dorset, BH21 7UH",
      "name": "Bird & Wild",
      "updated_at": "2019-12-19 17:55:51 UTC",
      "url": "https://birdandwild.co.uk/",
      "twitter": "@BirdandWild",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.9224, 50.8077]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Black Chapel",
      "description": "Preferred coffee of transpontines. Located in Chapel Yard SW18",
      "location": "SW18",
      "twitter": "@BlackChapelYard",
      "handle": "black-chapel",
      "url": "http://blackchapel.london/index.php/black-chapel",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1935, 51.4466]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Black Circle Coffee\u2122",
      "url": "https://blackcirclecoffee.com/",
      "location": "22 Ivy Gardens, Congleton, Cheshire, CW12 4GA",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/1081/9972/t/11/assets/logo.png",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@blackcirclenews",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2218, 53.162]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Black Craft Coffee",
      "description": "Heavy Metal, Light Roast. Black Craft Coffee Established was in 2013 by Anto, a travelling Barista who settled in London in 2003. To his surprise he discovered that the Brits drank something called Tea, and just weren\u2019t doing Coffee proper",
      "location": "Belvedere Rd, London, SE19 2HP",
      "twitter": "@BlackCraftCoffe",
      "handle": "black-craft-coffee",
      "url": "http://blackcraftcoffee.com/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0775, 51.416]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Black Sheep Coffee",
      "url": "https://leavetheherdbehind.com/",
      "location": "Caf\u00e9 in Camden, 26 Camden High Street, London, NW1 0JH",
      "profile_image_url": "https://www.leavetheherdbehind.com/wp-content/themes/blacksheep/assets/images/header/logo.webp",
      "updated_at": "02-May-2019 20:50",
      "twitter": "@leavetheherd",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1391, 51.5354]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Black Star Coffee",
      "url": "http://www.BlackStarCoffee.co.uk",
      "location": "West Bridgford, Nottinghamshire",
      "profile_image_url": "https://pbs.twimg.com/profile_images/2796470223/00b1ac4b3db71cad9fad418ada57a2f6_400x400.png",
      "updated_at": "16-Jul-2018 09:42",
      "twitter": "@BlkStarCoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.134, 52.9357]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Blenders",
      "url": "https://gaggia.ecwid.com/",
      "location": "75 St Giles' St, Northampton, NN1 1JF",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/blenders.png",
      "updated_at": "06-May-2015 15:51",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.8907, 52.2378]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Kingsmill Granary  Mill House  Mill Hill, Kingsnorth, Kent, TN23 3EW",
      "name": "Bloss Coffee Company",
      "updated_at": "2020-05-21 08:58:41 UTC",
      "url": "https://www.andbloss.com",
      "twitter": "@andBloss",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.8552, 51.1125]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Roughmoor Farm, Silkmills Road, Taunton, Somerset, TA1 5AA",
      "name": "Brazier Roasters",
      "updated_at": "2020-06-28 04:17:09 UTC",
      "url": "https://www.braziercoffeeroasters.co.uk/",
      "twitter": "@brazierroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.1306, 51.0218]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Brew Coffee Plus",
      "updated_at": "2020-05-21 08:59:04 UTC",
      "url": "https://www.brewcoffeeplus.com",
      "location": "Streatham, London",
      "facebook": "brewcoffeeplus",
      "instagram": "brewcoffeeplus",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1317, 51.4283]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bridge Coffee Roasters",
      "updated_at": "2020-05-21 08:58:53 UTC",
      "url": "https://www.bridgecoffeeroasters.co.uk",
      "location": "1 Alder Avenue, Dyffryn Business Park, Ystrad Mynach, Cardiff, Wales, CF82 7RJ",
      "linked_in_handle": "bridgecoffeeroasters",
      "twitter": "@BridgeValleyBev",
      "instagram": "bridge_coffee_roasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.2328, 51.6291]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Brown Bear",
      "url": "https://www.brownbear.co/",
      "location": "UK",
      "profile_image_url": "pbs.twimg.com/profile_images/488001772221251584/wYcl2AoF_400x400.png",
      "updated_at": "06-May-2015 15:31",
      "twitter": "@BrownBearCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.436, 55.3781]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 4a, The Foundry London Road, Kingsworthy, SO23 7QN",
      "name": "Brown Bottle Coffee",
      "updated_at": "2020-06-11 04:02:34 UTC",
      "url": "http://brownbottlecoffee.com",
      "twitter": "@BrownBottleCo",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2998, 51.0872]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bruce & Lukes Coffee",
      "url": "https://www.bruceandlukes.com/",
      "location": "Carlisle, Cumbria",
      "profile_image_url": "www.bruceandlukes.com/wp-content/uploads/2014/10/brucelukes_logo.jpg",
      "updated_at": "03-Jun-2015 13:48",
      "twitter": "@BruceandLukes",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.9329, 54.8925]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Buckshot Coffee Co.",
      "url": "http://buckshotcoffeeroasters.com",
      "location": "Sheffield, South Yorkshire",
      "profile_image_url": "pbs.twimg.com/profile_images/664827949691047936/pZgOGIM9.jpg",
      "updated_at": "01-Aug-2016 12:25",
      "twitter": "@BuckshotCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4701, 53.3811]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Bullet Coffee",
      "url": "http://www.bullet-coffee.com",
      "location": "789 Wandsworth Rd, London, SW8 3JQ",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/bullet-coffee-logo.jpg",
      "updated_at": "06-May-2015 15:51",
      "twitter": "@bulletcoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1476, 51.4668]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "1D Boldero Road, Moreton Hall, Bury St Edmunds, Suffolk, IP32 7BS",
      "name": "Butterworth & Son",
      "updated_at": "2019-12-22 11:02:56 UTC",
      "url": "https://butterworthandson.co.uk/",
      "twitter": "@ButterworthsUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.7489, 52.24]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Cafe Boutique",
      "url": "http://www.cafeboutique.co.uk",
      "location": "25 Dale Road, Stanton by Dale, Derbyshire, DE7 4QF",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/cafe-boutique-logo.jpg",
      "updated_at": "06-May-2015 15:38",
      "twitter": "@CafeBoutique",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3125, 52.9371]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Cafe Hormozi",
      "url": "https://hormozi.co.uk/",
      "location": "Kent",
      "profile_image_url": "thecoffeeroasters.x10.mx/images/cafe-hormozi-logo.jpg",
      "updated_at": "04-Feb-2016 14:58",
      "twitter": "@CafeHormozi",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.5217, 51.2787]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Caffe Biscardi 1903",
      "description": "For the Biscardi family, coffee is an art mastered over four generations in a journey started in New York in 1903. The Biscardi blends are crafted in Naples following old recipes prepared by Nonno Ferdinando utilising only the best beans roasted on fire fed by hand chopped oak wood",
      "location": "9 Dalecroft, London N4 2SJ",
      "twitter": "@Biscardi1903",
      "handle": "caffe-biscardi-1903",
      "url": "http://www.caffebiscardi1903.com",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0928, 51.5608]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "16 Front Street,  Prudhoe, Northumberland, NE42 5HN",
      "name": "Caffe Ginevra UK",
      "updated_at": "2020-06-28 02:35:47 UTC",
      "url": "https://www.caffeginevra.co.uk/",
      "twitter": "@CaffeGinevraUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8479, 54.9614]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Tornado House, Moxon Way, Sherburn In Elmet, Leeds, West Yorkshire, LS25 6FB",
      "name": "Caffe Society",
      "updated_at": "2020-06-28 01:21:27 UTC",
      "url": "https://caffesociety.co.uk/coffee/speciality-coffee",
      "twitter": "@CaffeSociety",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2317, 53.7942]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Cambridge Coffee Co",
      "description": "Inspired by one of the world's most beautiful cities we've created a range of ground and whole bean coffees for every part of your week. Our beans come from some of Africa's very best coffee farms via a century and a half old family import firm. We roast in small batches in a wonderfully restored vintage coffee roaster and... then we deliver them, fast and fresh, right to your door.",
      "location": "Cambridge, UK",
      "twitter": "@CambCoffeeCo",
      "handle": "cambridge-coffee-co",
      "url": "http://thecambridgecoffeecompany.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.1218, 52.2053]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "5 Saxon Business Centre, Windsor Avenue, London, SW19 2RR",
      "name": "Capital Coffee",
      "updated_at": "2020-04-08 01:10:12 UTC",
      "url": "https://capitalcoffee.co.uk/",
      "twitter": "@WeKnowCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1853, 51.4109]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Caravan Coffee Roaster",
      "url": "http://caravanonexmouth.co.uk/roastery/about",
      "location": "Granary Building, 1 Granary Square (off Goods Way), London, N1C 4AA",
      "profile_image_url": "https://pbs.twimg.com/profile_images/378800000850084911/00527c790fc98ed2c47e92ca89f619e6_400x400.jpeg",
      "updated_at": "16-Jul-2018 07:59",
      "twitter": "@CaravanRoastery",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1246, 51.5347]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Carrara Collection",
      "url": "https://www.carraracoffeeroasters.com/",
      "location": "Unit M1, Harrison Road,  Airfield Business Park, Market Harborough, Leicestershire, LE16 7QB",
      "profile_image_url": "pbs.twimg.com/profile_images/695293499793629185/ypgJwIzS.jpg",
      "updated_at": "01-Aug-2016 12:22",
      "twitter": "@CaffeCarrara",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.9424, 52.4979]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Carringtons Coffee Co",
      "updated_at": "2020-06-15 07:59:42 UTC",
      "url": "https://carringtonscoffee.co",
      "location": "The Roastery at Kenyon Hall Farm, Winwick Lane, Croft,, Warrington, Cheshire, WA3 7ED",
      "twitter": "@CarringtonsCo",
      "instagram": "carringtonscoffeeco",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.597, 53.39]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Carvetii Coffee",
      "url": "https://www.carvetiicoffee.co.uk/",
      "location": "The Roastery, Embleton, Cockermouth, Cumbria, CA13 9YA",
      "profile_image_url": "pbs.twimg.com/profile_images/458909059278577664/W3jM-lG9_400x400.jpeg",
      "updated_at": "06-May-2015 15:32",
      "twitter": "@CarvetiiCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.2776, 54.6638]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "U5 Briar Rhydding House, Otley Road, Shipley, West Yorkshire, BD17 7JW",
      "name": "Casa Espresso",
      "updated_at": "2020-09-02 05:38:42 UTC",
      "url": "https://casaespresso.co.uk",
      "twitter": "@Casa_Espresso",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.7533, 53.8447]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 1, Quell Farm Ind. Units, Greatham, Pulborough, West Sussex, RH20 2ES",
      "name": "Cast Iron Coffee Roasters",
      "updated_at": "2020-05-06 05:34:05 UTC",
      "url": "https://castironroasters.com",
      "twitter": "@castironroaster",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5227, 50.9335]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "512 Fulham road, London, SW6 5NJ",
      "name": "Chairs and Coffee",
      "updated_at": "2020-06-28 04:08:00 UTC",
      "url": "http://chairsandcoffee.co.uk",
      "twitter": "@chairsandcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.199, 51.4796]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "London, W2 4UA",
      "name": "Chapter Coffee",
      "updated_at": "2020-06-16 04:27:46 UTC",
      "url": "https://www.chaptercoffee.com/",
      "twitter": "@ChapterCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1897, 51.5155]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Charlestown Coffee",
      "url": "https://twitter.com/bradford_coffee",
      "location": "Yorkshire",
      "profile_image_url": "pbs.twimg.com/profile_images/532931991016988672/ma45bdjr.jpeg",
      "updated_at": "06-May-2015 15:55",
      "twitter": "@bradford_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1526, 53.6204]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Charlie Mills Coffee",
      "description": "We are a family run, independent moorland micro roastery. Sourcing and roasting the highest quality, 100% Arabica, green beans which are fully traceable and sustainable",
      "location": "Eaglesham, Glasgow, G76 0BB",
      "twitter": "@cmcoffeeroaster",
      "handle": "charlie-mills-coffee",
      "url": "http://www.charliemillscoffee.com",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2819, 55.738]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Cherry Picked Coffee",
      "url": "http://cherrypickedcoffee.co.uk",
      "location": "Worthing, West Sussex , BN11 2QU",
      "profile_image_url": "cherrypickedcoffee.co.uk/skin/frontend/ultimo/default/images/cpc-brand/CherryPickedCoffee-website-logo.png",
      "updated_at": "06-May-2015 15:53",
      "twitter": "@CoffeeClubUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.3518, 50.8144]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit C2, Island Trade Park, Bristow Broadway, Avonmouth, Bristol, BS11 9FB",
      "name": "Clifton Coffee Roasters",
      "updated_at": "2021-02-09 19:02:34 UTC",
      "url": "https://cliftoncoffee.co.uk",
      "twitter": "@cliftoncoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.6908, 51.5004]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Arch Roastery, Arch 374, Helmsley Place, London, E8 3SB",
      "name": "Climpson & Sons",
      "updated_at": "2019-12-21 16:34:46 UTC",
      "url": "https://climpsonandsons.com/",
      "twitter": "@climpsonandsons",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0588, 51.5397]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Cloggs Coffee",
      "description": "Cloggs Coffee Company is a Yorkshire based premium quality coffee bean supplier. We have a range of coffees that include single origin numbers and espresso blends. We ethically source the highest grade coffee beans available and hand roast them to order in the Calder Valley, West Yorkshire. Cloggs started life 13 years ago as a small coffee shop in an old converted clog factory in West Yorkshire, hence the name! We supply roasted coffee beans, tea and luxurious hot chocolate to cafes, restaurants, hotels and bars all over the UK.",
      "location": "3 Park Row, Leeds, West Yorkshire, LS26 0JA",
      "twitter": "@cloggscoffee",
      "handle": "cloggs-coffee",
      "url": "http://cloggscoffee.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4779, 53.75]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Science Gallery Caf\u00e9, Pearse St, Dublin, Ireland",
      "name": "Cloud Picker Coffee",
      "updated_at": "2020-06-28 01:50:29 UTC",
      "url": "https://cloudpickercoffee.ie",
      "twitter": "@CloudPickercoff",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2482, 53.3439]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "D10 Fieldhouse Industrial Estate, Fieldhouse Road, Rochdale, Lancashire, OL12 0AA",
      "name": "Clumsy Goat Coffee",
      "updated_at": "2020-04-25 03:40:37 UTC",
      "url": "https://clumsygoat.co.uk/",
      "twitter": "@clumsy_goat",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1553, 53.6286]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, Glynhir Rd, Llandybie, Ammanford, SA18 2TB",
      "name": "Coaltown Coffee Roasters",
      "updated_at": "2020-06-28 01:46:36 UTC",
      "url": "https://www.coaltowncoffee.co.uk",
      "twitter": "@CoaltownCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.7837, 52.1307]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coastal Roaster",
      "description": "At Coastal Roaster we believe in quality and sustainability, whilst still being able to enjoy the finer things in life. Our coffee is ethically sourced and most come with some form of certification. Our coffee is roasted by hand, and monitored by eye, ensuring we get the best out of each batch",
      "location": "Redcar, North Yorkshire",
      "twitter": "@Coastal_Roaster",
      "handle": "coastal-roaster",
      "url": "http://coastalroaster.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.078, 54.5975]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coburg Coffee Co.",
      "url": "http://www.coburgcoffeecompany.co.uk/",
      "location": "3 Harrington Way, Warspite Road, London, SE18 5NU",
      "profile_image_url": "pbs.twimg.com/profile_images/562275513683566593/wdQhEkws.jpeg",
      "updated_at": "07-Mar-2016 19:33",
      "twitter": "@CoburgCoffeeCo",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.0448, 51.4944]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Cavern - Eric Moore",
      "description": "Owner of coffee tasting club, online shop and mad dog.",
      "location": "Stony Stratford Market & Riseley, Bedford MK44 1EE",
      "twitter": "@CoffeeCavern",
      "handle": "eric-moore",
      "url": "http://brystreduksjon.net",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.4822, 52.2503]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 1 Pentrich Road, Giltbrook Ind. Estate, Nottingham, NG16 2UZ",
      "name": "Coffee Central",
      "updated_at": "2020-06-28 00:47:08 UTC",
      "url": "https://coffeecentral.co.uk/",
      "twitter": "@CoffeeCentralUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2811, 53.0045]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Compass",
      "url": "https://www.coffeecompass.co.uk/",
      "location": "Fort Road, Wick, Littlehampton, West Sussex, BN17 7QZ",
      "profile_image_url": "pbs.twimg.com/profile_images/444056311294992384/zqO3joyz_400x400.jpeg",
      "updated_at": "06-May-2015 15:41",
      "twitter": "@CoffeeCompass",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.552, 50.8146]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Mallens Brae, Torphichen, Bathgate, West Lothian, EH48 4NY",
      "name": "Coffee Direct",
      "updated_at": "2020-06-28 04:15:15 UTC",
      "url": "https://www.coffeedirect.co.uk/",
      "twitter": "@coffeedirect88",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.6478, 55.9307]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Factory",
      "url": "https://thecoffeefactory.co.uk/",
      "location": "Samuria Buildings,  Seaton Junction, Axminster, Devon, EX13 7PW",
      "profile_image_url": "pbs.twimg.com/profile_images/456719936040497152/7HWMFBIF_400x400.jpeg",
      "updated_at": "31-May-2015 13:30",
      "twitter": "@Coffee_Factory",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0655, 50.7635]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Magic",
      "url": "http://coffeemagic.co.uk",
      "location": "Griffin Lane, Attleborough, Norfolk, NR17 2AD",
      "profile_image_url": "https://pbs.twimg.com/profile_images/443060482732085248/cLTocldF_400x400.jpeg",
      "updated_at": "17-Jul-2018 13:57",
      "twitter": "@CoffeeMagic2",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.0163, 52.5172]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Mojo",
      "url": "https://www.coffeemojo.ie/",
      "location": "Unit W6, Wicklow Enterprise Centre, The Murrough, Wicklow Town, Co. Wicklow, Ireland",
      "profile_image_url": "https://pbs.twimg.com/profile_images/461196807221956608/BkBgCNmh_400x400.jpeg",
      "updated_at": "17-Jul-2018 13:56",
      "twitter": "@MojoRoastery",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.0458, 52.9863]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Plant",
      "url": "https://coffee.uk.com/",
      "location": "180 Portobello Road, London, W11 2EB",
      "profile_image_url": "https://coffee.uk.com/wp-content/uploads/2017/11/logo_60.jpg",
      "updated_at": "02-May-2019 20:33",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2047, 51.5158]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Real Ltd",
      "url": "http://coffeereal.co.uk",
      "location": "The Elephant House, Graylands Est., Langhurst Wood Road, Horsham, West Sussex, RH12 4QD",
      "profile_image_url": "pbs.twimg.com/profile_images/385986937/Coffee_Real_logo_50__400x400.jpg",
      "updated_at": "06-May-2015 15:41",
      "twitter": "@BrownBean",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.3246, 51.0983]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee Spot Roasters",
      "url": "http://1066Coffee.co.uk",
      "location": "East Sussex, TN38 8DW",
      "profile_image_url": "pbs.twimg.com/profile_images/534484690376208385/H_eg-105_400x400.png",
      "updated_at": "06-May-2015 15:59",
      "twitter": "@RoastersSpot",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.5296, 50.858]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee World",
      "url": "http://www.coffeeworld.co.uk/",
      "location": "Unit 9 Minton Enterprise Park, Oaks Drive, Newmarket, Suffolk, CB8 7YY",
      "profile_image_url": "pbs.twimg.com/profile_images/715863436/coffeeworldlowres_400x400.jpg",
      "updated_at": "06-May-2015 15:38",
      "twitter": "@CoffeeWorldUk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.3948, 52.2601]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Coffee, Chocolate & Tea",
      "url": "http://coffeechocolateandtea.com",
      "location": "944 Argyle Street, Glasgow, Scotland, G3 8YJ",
      "profile_image_url": "pbs.twimg.com/profile_images/2451603988/ju3g8f1x76mx96cx90ve.jpeg",
      "updated_at": "09-Mar-2016 16:07",
      "twitter": "@RoasteryGlasgow",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2847, 55.8649]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Croft House, Sandy Down, Boldre, Lymington, Hampshire, SO41 8PL",
      "name": "Coffee-Direct.co.uk",
      "updated_at": "2020-06-16 03:43:24 UTC",
      "url": "https://www.coffee-direct.co.uk",
      "twitter": "@coffeedirectuk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5576, 50.7942]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 20, Connect 10 Business Park, Foster Road, , Ashford, Kent, TN24 0FE",
      "name": "CoffeeBeanShop",
      "updated_at": "2020-06-28 04:20:30 UTC",
      "url": "https://www.coffeebeanshop.co.uk/",
      "twitter": "@CoffeeBeanShop",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.9018, 51.1311]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "31 Knightsdale Road, Ipswich, Suffolk, IP1 4JJ",
      "name": "Coffeelink",
      "updated_at": "2020-06-27 04:40:39 UTC",
      "url": "https://coffeelink.com/",
      "twitter": "@Coffeelink",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.1392, 52.0741]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 5, Dockley Estate, Dockley Road, London",
      "name": "Coleman Coffee Roasters",
      "updated_at": "2020-06-11 04:05:18 UTC",
      "url": "https://colemancoffee.com/",
      "twitter": "@ColemanCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0693, 51.4957]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "ColourCoffeeRoastery",
      "description": "Coffee roastery based just outside Newcastle Upon Tyne.",
      "location": "1 Pink Lane, Newcastle upon Tyne, NE1 5DW",
      "twitter": "@Colourcoffee",
      "handle": "colour-coffee-roastery",
      "url": "https://www.pinklanecoffee.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.6185, 54.9695]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Cork Coffee Roasters",
      "url": "http://corkcoffee.com",
      "location": "2 Bridge St, Cork, Ireland",
      "profile_image_url": "www.corkcoffee.com/gallery/1.jpg",
      "updated_at": "06-May-2015 15:49",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-8.4702, 51.9015]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Counter Roastery",
      "description": "Independent coffee roastery located in @countercafe on the canal in Hackney Wick.",
      "location": "Roach Rd, London, E3 2PA",
      "twitter": "@counterroastery",
      "handle": "counter-roastery",
      "url": "http://thecountercafe.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0214, 51.5402]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Devonbanks Cottage, Pitgober, Dollar, Clackmannanshire, Scotland, FK14 7PQ",
      "name": "CounterRoast",
      "updated_at": "2020-06-28 04:09:36 UTC",
      "url": "http://counterroast.co.uk",
      "twitter": "@CounterRoast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.6524, 56.1676]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 6A,  Blacklands Farm,  Wheatsheaf Rd, Henfiled,  West Sussex, BN5 9AT",
      "name": "Craft House Coffee",
      "updated_at": "2020-06-28 04:00:18 UTC",
      "url": "https://www.crafthousecoffee.co.uk/",
      "twitter": "@craftingcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2486, 50.9508]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Crafted Coffee Co",
      "url": "http://www.craftedcoffee.co.uk",
      "location": "6C New Barn Farm, Funtington, Chichester, West Sussex, PO18 9DA",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/collections/craftedcoffee_logo_medium.jpg",
      "updated_at": "16-Jul-2018 07:57",
      "twitter": "@Crafted_Coffee",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.8534, 50.8682]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Craic Coffee",
      "url": "https://twitter.com/craic_coffee",
      "location": "The Heath, Co Laois, Ireland",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/craic-coffee-logo.jpg",
      "updated_at": "06-May-2015 16:01",
      "twitter": "@craic_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-7.2245, 53.056]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Great Matridge, Longdown, Exeter, Devon, EX6 7BE",
      "name": "Crankhouse Coffee",
      "updated_at": "2020-06-28 01:46:26 UTC",
      "url": "https://www.crankhousecoffee.co.uk",
      "twitter": "@crankhouseroast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.6381, 50.6974]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Crediton Coffee",
      "url": "https://www.creditoncoffee.co.uk/",
      "location": "1 Market Square House, Market Street, Crediton, Devon, EX17 2BN",
      "profile_image_url": "https://pbs.twimg.com/profile_images/2555507673/CreditonCoffeeCompany_400x400.jpg",
      "updated_at": "16-Jul-2018 08:05",
      "twitter": "@CreditonCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.6581, 50.791]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Crosby Coffee",
      "url": "https://www.crosbycoffee.co.uk/",
      "location": "Unit 14, Bridge Road Industrial Estate, Litherland, Liverpool, Merseyside, L21 2QG",
      "profile_image_url": "pbs.twimg.com/profile_images/524576204888616960/74hzP_tr_400x400.jpeg",
      "updated_at": "06-May-2015 15:50",
      "twitter": "@CoffeeCrosby",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0018, 53.4682]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "172 Northdown Rd, Margate, Kent, CT9 2QN",
      "name": "Curve Roasters",
      "updated_at": "2020-06-27 06:50:10 UTC",
      "url": "https://www.curveroasters.co.uk",
      "twitter": "@curveroasters",
      "instagram": "curveroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.3951, 51.3883]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "DamnFineCoffeeCo",
      "url": "https://damnfinecoffeeco.bigcartel.com/",
      "location": "Nottingham",
      "profile_image_url": "pbs.twimg.com/profile_images/629548075057573888/QKCRnHYa.jpg",
      "updated_at": "01-Aug-2016 12:28",
      "twitter": "@DamnFineCoffeeC",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1581, 52.9548]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Danielle's Coffee",
      "url": "https://www.daniellescoffee.co.uk/",
      "location": "1 Burwarton, Bridgnorth, Shropshire, WV16 6QG",
      "profile_image_url": "pbs.twimg.com/profile_images/1106278318/DC_Red_Circle_small_normal.jpg",
      "updated_at": "01-Aug-2016 12:12",
      "twitter": "@DaniellesCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5604, 52.4631]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Dark Arts Coffee",
      "url": "https://www.darkartscoffee.co.uk/",
      "location": "Homerton, London, E9",
      "profile_image_url": "pbs.twimg.com/profile_images/665250179176660993/2YUjHGTB_400x400.jpg",
      "updated_at": "15-Apr-2016 14:29",
      "twitter": "@DarkArtsCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0383, 51.549]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Dark Fluid Coffee",
      "url": "http://darkfluid.co.uk",
      "location": "Brockley Market, London, SE4 1UT",
      "profile_image_url": "pbs.twimg.com/profile_images/1818250371/DF_Logo_under_over_twitter_400x400.png",
      "updated_at": "06-May-2015 15:34",
      "twitter": "@DarkFluidCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0259, 51.4682]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Holme Mills, West Slaithwaite Road, Marsden, HD7 6LS",
      "name": "Dark Woods Coffee",
      "updated_at": "2020-06-28 04:25:23 UTC",
      "url": "https://darkwoodscoffee.co.uk/",
      "twitter": "@DarkWoodsCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.9062, 53.6134]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "5 Airds Lane (Bridgegate), Glasgow, Scotland, G1 5HU",
      "name": "Dear Green Coffee",
      "updated_at": "2019-12-21 17:45:07 UTC",
      "url": "https://www.deargreencoffee.com",
      "twitter": "@CoffeeGlasgow",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2499, 55.855]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Fort Road, Wick, Littlehampton, BN17 7QZ",
      "name": "Decadent Decaf Coffee Company",
      "updated_at": "2020-06-27 06:53:20 UTC",
      "url": "https://www.decadentdecaf.com/",
      "twitter": "@DecadentDecaf",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5523, 50.8142]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "DEEPmills Suffolk",
      "description": "We slow Hand Roast Gourmet Arabica Coffees in small batches each week.We produce fine Chocolate products, Importers of Fine Ceylon Teas",
      "location": "45 Orchard Close, Woodbridge, Suffolk, IP12 1LD",
      "twitter": "@DeepmillsUK",
      "handle": "deepmills-suffolk",
      "url": "https://www.deepmills.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.3147, 52.1049]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "DJ Miles",
      "url": "http://milesteaandcoffee.com/",
      "location": "Porlock House, Stephenson Road,  Minehead, Somerset, TA24 5EB",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/dj-miles.logo.png",
      "updated_at": "06-May-2015 15:45",
      "twitter": "@MilesTeaCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.4635, 51.2011]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "24 Kenilworth Road, Ainsdale, Southport, PR8 3PE",
      "name": "Django Coffee Co.",
      "updated_at": "2020-06-28 02:31:12 UTC",
      "url": "https://www.djangocoffeeco.com",
      "twitter": "@DjangoCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0399, 53.5978]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "90 Hanbury Street, London, E1 5JL",
      "name": "doppiocoffee",
      "updated_at": "2020-06-28 04:28:28 UTC",
      "url": "https://doppiocoffee.co.uk",
      "twitter": "@doppiocoffeeltd",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.071, 51.5203]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Drip Coffee",
      "updated_at": "2020-05-21 08:58:59 UTC",
      "url": "https://www.coffeedrip.co.uk",
      "location": "Hampshire",
      "facebook": "dripcoffeebeans",
      "instagram": "dripcoffeebeans",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3081, 51.0577]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "19a Anne Street South, Dublin, Ireland, 2",
      "name": "DublinBaristaSchool",
      "updated_at": "2020-06-28 01:29:02 UTC",
      "url": "https://dublinbaristaschool.ie",
      "twitter": "@dubbaristasch",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2588, 53.3409]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Marsh Farm Roastery, Hilperton, Wiltshire, BA14 7PJ",
      "name": "Dusty Ape Coffee",
      "updated_at": "2020-06-28 01:48:25 UTC",
      "url": "https://dustyape.com",
      "twitter": "@DustyApe",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1901, 51.3404]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Wicks House, Ford Lane, Arundel, West Sussex, BN18 0DF",
      "name": "Edgcumbes",
      "updated_at": "2020-03-25 05:50:01 UTC",
      "url": "https://edgcumbes.co.uk/",
      "twitter": "@Edgcumbes",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5769, 50.8376]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "eightpointnine",
      "description": "Personalised fresh coffee blends for discerning individuals. Convert to us today and get your first box half price with code: 8PT9HALF",
      "location": "London | Cotswolds | Norway",
      "twitter": "@eightpointnine",
      "handle": "eight-point-nine",
      "url": "https://eightpointnine.com/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "40 Haven Green, London, W5 2NX",
      "name": "ELECTRIC COFFEE CO.",
      "updated_at": "2020-06-28 04:10:49 UTC",
      "url": "https://www.electriccoffee.co.uk/",
      "twitter": "@eleccoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.302, 51.5155]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Ethical Addictions",
      "url": "https://eacoffee.co.uk/",
      "location": "Rear Warehouse, 69A Alvin Street, Gloucester, GL1 3EH",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/ethical-addictions-logo.jpg",
      "updated_at": "17-Jul-2018 13:57",
      "twitter": "@EA_Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2414, 51.8693]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Craven, Calderdale, Clitheroe, Lancashire",
      "name": "Exchange Coffee Co.",
      "updated_at": "2020-06-28 02:35:40 UTC",
      "url": "http://exchangecoffee.co.uk",
      "twitter": "@Exchange_Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3931, 53.8711]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "EXE Coffee Roasters",
      "url": "https://execoffeeroasters.wordpress.com/",
      "location": "Exeter, Devon",
      "profile_image_url": "pbs.twimg.com/profile_images/625323275481161734/LKID8vqR_400x400.png",
      "updated_at": "21-Sep-2015 16:53",
      "twitter": "@execoffeeroast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.5339, 50.7184]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Exotic Coffee",
      "description": "Coffee hand roasted locally",
      "location": "Unit 30 Old London Road Oxford, OX33 1XW",
      "twitter": "@exoticroasters",
      "handle": "exotic-coffee",
      "url": "http://exoticcoffeeroasters.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.126, 51.7469]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Extract Coffee",
      "url": "https://extractcoffee.co.uk/",
      "location": "Unit 1, Gatton Road, Bristol, BS2 9SH",
      "profile_image_url": "https://extractcoffee.co.uk/manage/wp-content/themes/extract2015/images/logo_extract_modified.svg",
      "updated_at": "01-May-2019 08:14",
      "twitter": "@extractcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5733, 51.4675]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "8 Brunel Business Court, Eastern Way, Bury St Edmunds, Suffolk, IP32 7AJ",
      "name": "F & E Coffee",
      "updated_at": "2019-12-21 17:45:39 UTC",
      "url": "https://fandecoffee.co.uk/",
      "twitter": "@FandEcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.7243, 52.2497]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Farrers \u2122",
      "url": "https://farrerscoffee.co.uk/",
      "location": "Shap Road Industrial Estate, Fell View Trading Park, Kendal, Cumbria, LA9 6NZ",
      "profile_image_url": "pbs.twimg.com/profile_images/1899682619/image_400x400.jpg",
      "updated_at": "06-May-2015 15:30",
      "twitter": "@Farrers_Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7373, 54.3447]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 77-78, Brixton Village Market, London, SW9 8PS",
      "name": "Federation Coffee",
      "updated_at": "2020-06-28 02:42:19 UTC",
      "url": "https://federation.coffee",
      "twitter": "@FederationCoffe",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1131, 51.4622]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Ferns",
      "url": "http://coffeeisferns.co.uk",
      "location": "Fern House, 4 Onslow Close, Basingstoke Hampshire, RG24 8QL",
      "profile_image_url": "www.coffeeisferns.co.uk/img/g_ferns_coffee_logo.jpg",
      "updated_at": "18-May-2015 10:49",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.0639, 51.284]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "9A Hepworth Business Park, Coedcae Lane, Pontyclun, Wales, CF72 9FQ",
      "name": "Ferrari's Coffee",
      "profile_image_url": "https://pbs.twimg.com/profile_images/432886446320402434/zWMELoY0_400x400.jpeg",
      "updated_at": "2019-07-30 07:30:16 UTC",
      "url": "https://ferrariscoffee.co.uk/",
      "twitter": "@FerrarisCoffee",
      "facebook": "ferraris.coffee.1",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.4039, 51.5312]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "FINCA",
      "url": "https://fincacoffee.co.uk/",
      "location": "41 Great Western Road, Dorchester, Dorset, DT1 1UF",
      "profile_image_url": "pbs.twimg.com/profile_images/603599083043979264/OHNYdTbK_400x400.jpg",
      "updated_at": "03-Jun-2015 14:02",
      "twitter": "@scouting4coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.4386, 50.7116]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 39, Clayhill Light Industrial Park, Coalbrookdale Rd, Neston, Cheshire, CH64 3UG",
      "name": "Flaming Bean Coffee",
      "updated_at": "2020-06-28 03:36:39 UTC",
      "url": "http://www.flamingbean.co.uk",
      "twitter": "@flamingbean",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0582, 53.3012]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Footprint Coffee",
      "url": "https://footprintcoffee.co.uk/",
      "location": "Ednol Farm, Kinnerton, Presteigne, Powys, Wales, LD8 2PF",
      "profile_image_url": "pbs.twimg.com/profile_images/421357004263653376/bxx3fB3N_400x400.jpeg",
      "updated_at": "06-May-2015 15:51",
      "twitter": "@FootprintCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.1125, 52.2713]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Coach House, 9a Nether Edge Road, Sheffield, South Yorkshire, S7 1RU",
      "name": "Foundry Coffee Roasters",
      "updated_at": "2020-07-24 03:07:56 UTC",
      "url": "https://foundrycoffeeroasters.com",
      "twitter": "@FoundryCoffee1",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.488, 53.3593]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 39/40 Effingham Road, Attercliffe, Sheffield, South Yorkshire, S9 3QA",
      "name": "Frazer's Coffee Roasters",
      "updated_at": "2020-06-28 04:09:21 UTC",
      "url": "https://www.frazerscoffeeroasters.co.uk/",
      "twitter": "@FrazersCoffee",
      "facebook": "frazerscoffeeroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4396, 53.3902]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Freehand Coffee",
      "url": "http://www.freehandcoffee.com",
      "location": "Unit 4 Barncoose Ind. Est, Redruth, Cornwall, TR15 3RQ",
      "profile_image_url": "pbs.twimg.com/profile_images/588446427078139904/urXgfSvn_400x400.png",
      "updated_at": "19-May-2015 10:27",
      "twitter": "@freehandcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.2521, 50.2278]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Fresh bag of coffee",
      "description": "Roasting coffee to order in Nottingham. Blend and single origin beans. Use code NottsDelivery for free delivery",
      "location": "Nottingham, UK",
      "twitter": "@freshbagcoffee",
      "handle": "fresh-bag-of-coffee",
      "url": "http://afreshbagofcoffee.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1581, 52.9548]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Freshpac",
      "url": "https://freshpac.co.uk/",
      "location": "Unit B, Broadway Drive, Halesworth, Suffolk, IP19 8QR",
      "profile_image_url": "pbs.twimg.com/profile_images/2223580604/logo_400x400.png",
      "updated_at": "03-Jun-2015 13:29",
      "twitter": "@FreshpacSales",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.5089, 52.3536]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Full Circle Roasters",
      "url": "https://facebook.com/FCRoaster",
      "location": "Carrickmacross, Co. Monaghan, Ireland",
      "profile_image_url": "pbs.twimg.com/profile_images/635328763866279936/G8s1eAGR_400x400.jpg",
      "updated_at": "02-Jul-2016 11:58",
      "twitter": "@FCRoaster",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.7188, 53.978]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Southview, Maypole Lane, Hoath, Canterbury, Kent,  CT3 4LL",
      "name": "Garage Coffee",
      "url": "https://www.garageroasted.co.uk/",
      "updated_at": "2020-06-28 01:02:48 UTC",
      "twitter": "@GarageRoasted",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.1603, 51.3386]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 42 Bradley Court, Bradley Fold Trading Estate, Radcliffe Moor Road, Bolton, Lancashire, BL2 6RT",
      "name": "Garraways Coffee",
      "updated_at": "2020-06-28 02:44:25 UTC",
      "url": "https://www.garraways.co.uk/",
      "twitter": "@GarrawaysCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3634, 53.5734]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Geniuscoffea",
      "description": "Tisbury's first coffee roaster..Roasted in Tisbury and for you to enjoy in our unique coffee shop in the heart of Wiltshire",
      "location": "High street, Tisbury, Wiltshire, SP3 6JB",
      "handle": "geniuscoffea",
      "url": "https://www.facebook.com/geniuscoffea",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.0659, 51.0456]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Gillards of Bath",
      "url": "https://www.gillardsofbath.co.uk/",
      "location": "1 Roseberry Place, Lower Bristol Road, Bath, BA2 3DU",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/gillards_logo.jpg",
      "updated_at": "01-May-2019 08:25",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3819, 51.3821]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Lyon Lodge, Glenlyon, By Aberfeldy, Perthshire, Scotland, PH15 2PP",
      "name": "Glen Lyon Coffee",
      "updated_at": "2020-06-28 02:33:18 UTC",
      "url": "https://www.glenlyoncoffee.co.uk",
      "twitter": "@glenlyoncoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.3114, 56.5945]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Glenfinlas Coffee",
      "url": "http://glenfinlascoffee.com",
      "location": "1 St. Colme Street, Edinburgh, Scotland, EH3 6AA",
      "profile_image_url": "www.glenfinlas.com/_resource/_img/glenfinlas-logo.png",
      "updated_at": "06-May-2015 15:40",
      "twitter": "@glenfinlas_shop",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.208, 55.9534]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "9-11 Market Square, Sandbach, Cheshire , CW11 1AP",
      "name": "Godfrey C. Williams & Son Ltd",
      "updated_at": "2020-06-28 04:31:17 UTC",
      "url": "http://www.godfreycwilliams.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.362, 53.1436]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Newcastle upon Tyne",
      "name": "GoldBoxRoastery",
      "updated_at": "2020-06-28 02:50:05 UTC",
      "url": "https://www.goldboxroastery.com/uae",
      "twitter": "@GoldBoxRoastery",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.6178, 54.9783]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Gordon St Coffee",
      "url": "https://www.gordonstcoffee.co.uk/",
      "location": "Glasgow Central Station, 79 Gordon Street, Glasgow, Scotland, G1 3SQ",
      "profile_image_url": "pbs.twimg.com/profile_images/555774132861009922/IGnAh0Y4_400x400.jpeg",
      "updated_at": "06-May-2015 15:46",
      "twitter": "@gordonstcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2571, 55.86]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "66 The Park, Findhorn, IV36 3TZ",
      "name": "Green Bridge Organics",
      "updated_at": "2020-06-27 06:36:34 UTC",
      "url": "https://greenbridgeorganics.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.5976, 57.6154]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 1 Green Farm, Wendover Road, Rackheath Ind. Est., Norwich, Norfolk, NR13 6LQ",
      "name": "Green Farm Coffee",
      "updated_at": "2020-06-28 01:03:32 UTC",
      "url": "https://www.greenfarmcoffee.co.uk/",
      "twitter": "@greenfarmcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.3705, 52.6718]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Manor Farm Barns, Glandford, Norfolk, NR25 7JP",
      "name": "Grey Seal Coffee",
      "profile_image_url": "http://cdn.shopify.com/s/files/1/0181/3537/collections/grey-seal-logo_medium.jpg?v=1404853267",
      "updated_at": "2019-11-17 18:14:28 UTC",
      "url": "https://www.greysealcoffee.com/",
      "twitter": "@Greysealcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.0375, 52.9319]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Grind Coffee Bar",
      "url": "http://grindcoffeebar.co.uk",
      "location": "79 Lower Richmond Road, Putney, London, SW15 1ET",
      "profile_image_url": "static1.squarespace.com/static/53ce9752e4b09ce5b33ae23f/t/56c47fcd2b8dde24de9b08b8/1459031788588/?format=400w",
      "updated_at": "15-Apr-2016 14:28",
      "twitter": "@GrindCoffeeBar",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2194, 51.4672]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Grounded Coffee",
      "description": "Proud to stock one of the largest selections of single origin, flavoured, blends and gourmet coffee. Shop online or find us at Meadowhall and the Moor Market!",
      "location": "Sheffield, UK",
      "twitter": "@GroundedBoys",
      "handle": "grounded-coffee",
      "url": "http://ground-n-out.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4701, 53.3811]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, Meltham, Holmfirth, Yorkshire, HD9 4EP",
      "name": "Grumpy Mule Coffee",
      "updated_at": "2020-06-28 02:43:51 UTC",
      "url": "https://grumpymule.co.uk",
      "twitter": "@GrumpyMule",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8306, 53.5999]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "2 Cornwall Place, High Street, Buckingham, Buckinghamshire, MK18 1SB",
      "name": "Gyre & Gimble",
      "updated_at": "2020-06-28 01:51:04 UTC",
      "url": "http://gyre.coffeevagabond.co.uk",
      "twitter": "@mrgyre_mrgimble",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.9853, 52.0014]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "169 High Street, Winchester, Hampshire, SO23 9BQ",
      "name": "Hampshire Coffee Co.",
      "updated_at": "2020-06-16 22:39:51 UTC",
      "url": "https://hampshirecoffee.co/",
      "twitter": "@hantscoffeeco",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3081, 51.0611]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, 6F Bess Park Road, Wadebridge, Cornwall, PL27 6HB",
      "name": "Hands-On Coffee",
      "updated_at": "2020-06-28 04:32:53 UTC",
      "url": "https://hands-on-coffee.co.uk/",
      "twitter": "@hands_on_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.8224, 50.5201]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Happy Donkey Coffee",
      "url": "https://www.happydonkey.co.uk/",
      "location": "Units B,F and J, 50 Mount Pleasant, Silver Street, Reading, Berkshire, RG1 2TD",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/Happy_Donkey_Coffee_Logo.png",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@happydonkeyltd",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.9665, 51.4496]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Hasbean",
      "url": "https://www.hasbean.co.uk/",
      "location": "Unit 16, Ladford Covert, Ladfordfields Industrial Estate, Seighford, Stafford, ST18 9QL",
      "profile_image_url": "cdn.shopify.com/s/files/1/0023/1572/t/10/assets/logo.png",
      "updated_at": "06-May-2015 15:42",
      "twitter": "@hasbean",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2071, 52.8326]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "HATHI COFFEE",
      "description": "The Hathi Coffee Roastery is the vision of husband and wife, Johan and Wenona Du Toit. A true artisan approach to creating the finest coffee, hand roasted daily and delivered to your doorstep. From the start it was most important for us to build a direct relationship with our customers and be part of their journey as they discovered the world of Speciality Coffee. We only source 100% Arabica Speciality Grade green beans from responsible growers. This ensures the ethical traceability of our products and in doing so, helps further the industry as a whole.",
      "location": "Church Farm, Ardeley, Hertfordshire, SG2 7AH",
      "twitter": "@hathicoffee",
      "handle": "hathi-coffee",
      "url": "http://hathicoffee.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1203, 51.9222]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Hayling Island, Hampshire",
      "name": "Hayling Island Coffee Society",
      "updated_at": "2020-05-21 07:15:23 UTC",
      "url": "https://www.hics.biz/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.976, 50.7948]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "95 Greengate, Manchester, M3 7NG",
      "name": "Heart & Graft Coffee Roastery",
      "updated_at": "2019-12-21 17:46:03 UTC",
      "url": "https://www.heartandgraft.co.uk",
      "twitter": "@HeartandGraft",
      "instagram": "heartandgraft",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2503, 53.4879]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Highland Coffees",
      "description": "Welcome to Perthshire's premier coffee roasting house!",
      "location": "Drummond Street, Comrie, Perthshire, PH6 2DW",
      "twitter": "@HighlandCoffees",
      "handle": "highland-coffees",
      "url": "http://www.highlandcoffees.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.9855, 56.3753]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Lyleston West Lodge, Cardross, Argyll and Bute, Scotland, G82 5HF",
      "name": "Home Ground Coffee",
      "updated_at": "2020-06-28 02:59:22 UTC",
      "url": "https://www.homegroundcoffee.co.uk/",
      "twitter": "@The_coffee_guy",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.6767, 55.9795]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Fittleworth, Pulborough, West Sussex",
      "name": "Honeybee Coffee",
      "updated_at": "2020-06-16 04:29:18 UTC",
      "url": "https://thehoneybeecoffeeroastery.co.uk/",
      "twitter": "@HoneybeeCoffee1",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5599, 50.9641]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Hope & Glory Coffee",
      "description": "The new speciality coffee roasters on the block. Bringing Hope & Glory into your life, just one cup at a time. Tweets from Sean & Gina",
      "location": "North Lincolnshire, UK",
      "twitter": "@HopeandGloryUK",
      "handle": "hope-and-glory-coffee",
      "url": "http://www.hopeandglorycoffee.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5597, 53.6056]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Horsebox Coffee Co",
      "updated_at": "2020-05-21 06:55:30 UTC",
      "url": "https://horseboxcoffeeco.com",
      "location": "Unit 12 Highlands Farm, Wallingford, Oxfordshire, OX10 0QX",
      "twitter": "@Horseboxcoffee",
      "facebook": "horseboxcoffeeco",
      "instagram": "@horseboxcoffeeco",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1579, 51.6163]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Howard's Nursery, Handcross Road, Plummers Plain, Horsham, West Sussex, RH13 6NX",
      "name": "Horsham Coffee Roaster",
      "updated_at": "2020-06-15 09:31:33 UTC",
      "url": "https://www.horshamcoffeeroaster.co.uk",
      "twitter": "@horshamcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2605, 51.0419]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Gwydir St, Cambridge, CB1 2LJ",
      "name": "Hot Numbers Coffee",
      "updated_at": "2020-06-28 02:37:17 UTC",
      "url": "https://hotnumberscoffee.co.uk/",
      "twitter": "@hotnumbers",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.1388, 52.2007]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Duke Street, Mayfair, London, W1",
      "name": "HR Higgins Ltd",
      "updated_at": "2020-06-28 02:35:12 UTC",
      "url": "https://www.hrhiggins.co.uk/",
      "twitter": "@Higginscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.151, 51.5135]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Ludlow, Shropshire",
      "name": "Hundred House Coffee",
      "updated_at": "2020-05-07 00:49:16 UTC",
      "url": "https://hundredhousecoffee.com",
      "twitter": "@HundredHouseCo",
      "facebook": "hundredhousecoffee",
      "instagram": "hundredhousecoffee.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7139, 52.3677]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Imbibe Coffee",
      "url": "https://imbibe.ie/",
      "location": "Dublin, Ireland",
      "profile_image_url": "imbibe.ie/wp-content/uploads/2013/09/imbibe-coffee.png",
      "updated_at": "06-May-2015 15:57",
      "twitter": "@garyimbibe",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2603, 53.3498]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Inverness Coffee Roasting",
      "url": "https://invernesscoffeeroasting.co.uk/",
      "location": "15 Chapel Street, Inverness, Scotland, IV1 1NA",
      "profile_image_url": "invernesscoffeeroasting.co.uk/wp-content/uploads/Logo-150x150.gif",
      "updated_at": "06-May-2015 15:55",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.229, 57.481]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 9 Castle business Park, Shrewsbury, Shropshire, SY1 2EG",
      "name": "Iron & Fire Speciality Coffee Roasters",
      "updated_at": "2020-06-28 00:09:10 UTC",
      "url": "https://ironandfire.co.uk",
      "twitter": "@IronFireCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7498, 52.7136]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Isle of Skye roastery",
      "url": "https://facebook.com/skyeroastery",
      "location": "The Red Door, The Old Filling Station, Near the Roundabout by the Skye Bridge, Kyleakin side! , Isle of Skye, Scotland, IV41 8PQ",
      "profile_image_url": "https://pbs.twimg.com/profile_images/2316016043/facebook_roastery_profile_pic_400x400.jpg",
      "updated_at": "16-Jul-2018 09:42",
      "twitter": "@skyecoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.7435, 57.2721]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Ismail Coffee & Tea",
      "description": "Roasting IN-STORE daily selling some of the freshest coffee in the world.Family experience since 1925 .",
      "location": "95-97 Mount Pleasant Road, Tunbridge Wells, Kent, TN1 1QG",
      "twitter": "@IsmailCoffeeTea",
      "handle": "ismail-coffee-and-tea",
      "url": "http://ismail.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.2633, 51.1335]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "J. Atkinson and Co.",
      "url": "https://thecoffeehopper.com/",
      "location": "China Street, Lancaster, Lancashire, LA1 1EX",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/atkinsons-logo.jpg",
      "updated_at": "03-Jun-2015 14:18",
      "twitter": "@coffeehopper",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8032, 54.0491]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 7, Cropper Row, Haigh Ind. Est., Ross-on-Wye, Herefordshire, HR9 5LA",
      "name": "James Gourmet Coffee",
      "updated_at": "2020-06-10 10:38:28 UTC",
      "url": "https://jamesgourmetcoffee.com",
      "twitter": "@GourmetPJ",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5707, 51.9127]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Yarcroft, Yarbridge, Brading, Isle of Wight, PO36 0BP",
      "name": "Jasper's Coffee",
      "updated_at": "2020-06-28 04:34:19 UTC",
      "url": "http://www.jasperscoffee.co.uk/",
      "twitter": "@JaspersCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1445, 50.6798]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Jaunty Goat",
      "updated_at": "2020-04-26 04:57:34 UTC",
      "url": "https://www.jauntygoat.co.uk",
      "location": "Chester, UK",
      "twitter": "@jaunty_goat",
      "facebook": "jauntygoat",
      "instagram": "@jaunty_goat",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8931, 53.1934]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, 510 Mitchelstown Road, Northwest Business Park, Ballycoolin, Dublin, Ireland",
      "name": "Java Republic Roasting Company",
      "profile_image_url": "https://www.javarepublic.com/wp-content/uploads/2017/11/Unknown.png",
      "updated_at": "2019-11-17 14:34:13 UTC",
      "url": "https://www.javarepublic.com/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.3649, 53.4077]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "17d Hall Farm Business Park, Martham Road, Rollesby, Great Yarmouth, Norfolk, NR29 5DR",
      "name": "Javabean",
      "updated_at": "2020-06-12 04:49:32 UTC",
      "url": "https://www.javabean.co.uk/",
      "twitter": "@JavabeanLimited",
      "instagram": "javabeanlimited",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.6204, 52.6877]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "JerichoCoffeeTraders",
      "url": "https://www.jerichocoffeetraders.com/",
      "location": "3 King Edward Street, Oxford, Oxfordshire",
      "profile_image_url": "pbs.twimg.com/profile_images/583566655650828288/-6mPKmMG_400x400.jpg",
      "updated_at": "02-Aug-2015 20:45",
      "twitter": "@JeriCoffTraders",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2548, 51.752]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Jesters Coffee",
      "url": "http://jesterscoffee.co.uk",
      "location": "4 Hawthorn Way, St Ives, Cambridgeshire, PE27 3YP",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/jesters.gif",
      "updated_at": "06-May-2015 15:45",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0717, 52.3348]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Joe Black Coffee",
      "url": "https://www.joeblackcoffeeandtea.co.uk/",
      "location": "Millers Bridge Industrial Estate, Seymour Street, Liverpool, Merseyside, L20 1EE",
      "profile_image_url": "pbs.twimg.com/profile_images/3559403663/0f55bb5b776b12058851af5efd69f6e6_400x400.png",
      "updated_at": "06-May-2015 15:43",
      "twitter": "@JoeBlackCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0002, 53.4441]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "11 Bank St, Carlisle, Cumbria, CA3 8HG",
      "name": "John Watt And Sons",
      "updated_at": "2020-06-28 01:00:12 UTC",
      "url": "https://www.johnwatt.co.uk",
      "twitter": "@johnwatt_son",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.9346, 54.8939]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Jonestown Coffee",
      "description": "Small low brow coffee roaster coming soon to East London. Quality without the bullshit. Info at jonestowncoffee@gmail.com",
      "location": "East London",
      "twitter": "@jonestowncoffee",
      "handle": "jonestown-coffee",
      "url": "http://jonestowncoffee.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Julius Meinl UK",
      "url": "http://meinlcoffee.com/uk/uk/julius-meinl.html",
      "location": "Unit 3, Ground Floor, Lafone House, Leathermarket, 11 \u2013 13 Weston Street, London, SE1 3ER",
      "profile_image_url": "www.meinlcoffee.com/fileadmin/templates/meinl/img/logo-red.png",
      "updated_at": "06-May-2015 15:52",
      "twitter": "@MeinlCoffeeUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0849, 51.4999]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Just Bean Roasted",
      "url": "http://justbeanroasted.co.uk",
      "location": "Leeds, West Yorkshire",
      "profile_image_url": "https://pbs.twimg.com/profile_images/378800000674581263/a0a4591877c7ebad2b0f5f7f8ef2df32_400x400.png",
      "updated_at": "16-Jul-2018 09:42",
      "twitter": "@justbeanroasted",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5491, 53.8008]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Chiswick, London",
      "name": "Kimbo UK",
      "updated_at": "2020-06-28 02:36:56 UTC",
      "url": "https://kimbo.co.uk/",
      "twitter": "@KimbointheUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2633, 51.4925]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Flurry Bridge Business Park, Lower Foughill Rd, Jonesborough, Newry, Northern Ireland, BT35 8SQ",
      "name": "Koffy",
      "updated_at": "2020-11-09 06:23:18 UTC",
      "url": "https://koffy.ie",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.3715, 54.1058]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 6 Luddite Way Business Park Rawfolds Way, Rawfolds, Cleckheaton, BD19 5DQ",
      "name": "Limini Coffee",
      "updated_at": "2019-12-19 17:54:57 UTC",
      "url": "https://www.liminicoffee.co.uk",
      "twitter": "@liminicoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.7036, 53.7192]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Lincoln & York",
      "url": "https://www.lincolnandyork.com/",
      "location": "Kahawa House, Elsham Wold Industrial Estate, Nr. Brigg, North Lincolnshire, DN20 0SP",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/lincoln-york-logo.jpg",
      "updated_at": "18-May-2015 10:44",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.4224, 53.6062]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "North Hykeham, Lincoln",
      "name": "Lincoln Tea & Coffee",
      "updated_at": "2020-06-28 01:48:32 UTC",
      "url": "https://thelincolnteaandcoffeecompany.co.uk/",
      "twitter": "@LincolnTeaCoffe",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5871, 53.1826]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 50, Station Road Workshops, Station Road, Bristol, BS15 4PJ",
      "name": "Little and Long",
      "updated_at": "2020-06-28 01:50:08 UTC",
      "url": "http://littleandlong.com",
      "twitter": "@LittleandLongCC",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.4903, 51.474]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Littlestone Coffee",
      "url": "https://littlestonecoffee.co.uk/",
      "location": "17 Norman Court, Budlake Road, Exeter, EX2 8PY",
      "profile_image_url": "littlestonecoffee.co.uk/wp-content/themes/littlestone/assets/img/logo.png",
      "updated_at": "17-Sep-2017 16:46",
      "twitter": "@Lstonecoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.5272, 50.7004]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Londinium Espresso",
      "description": "LONDINIUM espresso is a dedicated espresso roaster committed to introducing everyone we can to the ultimate taste that only a lever espresso machines can bring to your cup LONDINIUM espresso has been providing single origin roasts to espresso lovers all over the globe since 2004 Our quest for the ultimate espresso led us to design and have built in England our own range of lever espresso machines, LONDINIUM I, II, & III, all designed to do one thing: make perfect espresso, again & again",
      "location": "426 Long Drive, London UB6 8UH",
      "twitter": "@lespresso",
      "handle": "londinium-espresso",
      "url": "https://londiniumespresso.com/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.3583, 51.5433]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Old Hall Farm, Grafton, Tilston, Cheshire, SY14 7JE",
      "name": "Lost Barn Coffee Roasters Ltd",
      "updated_at": "2020-06-10 10:39:58 UTC",
      "url": "https://lostbarncoffee.co.uk",
      "facebook": "lostbarncoffee",
      "instagram": "lostbarncoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8216, 53.0552]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 54-55, Milstrood Road, Whitstable, Kent, CT5 3PS",
      "name": "Lost Sheep Coffee",
      "updated_at": "2020-06-16 04:33:29 UTC",
      "url": "https://www.lostsheepcoffee.com",
      "twitter": "@SheepCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.034, 51.3513]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Luckie Beans",
      "url": "https://www.luckiebeans.co.uk/",
      "location": "Love Lane, Berwick Upon Tweed, Northumberland, TD15 1AR",
      "profile_image_url": "pbs.twimg.com/profile_images/593402567314538498/WEYpvzgA_400x400.jpg",
      "updated_at": "20-Aug-2015 18:24",
      "twitter": "@luckiebeans",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.0059, 55.7689]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Luckie Beans Coffee Roasters",
      "updated_at": "2020-06-16 04:00:35 UTC",
      "url": "https://www.luckiebeans.co.uk",
      "location": "Love Lane, Berwick Upon Tweed, TD15 1AR",
      "twitter": "@luckie_beans",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.0059, 55.7689]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Lulu Coffee Company",
      "description": "Hello, we\u2019re Lulu. We\u2019re small batch community coffee roasters and bakers and we do everything at our lovely old shop on the high street in Ware, Hertfordshire. We\u2019re committed to bringing all our customers fantastic coffee, good old fashioned service and some wonderful things to eat too. When you\u2019re next in town, pop by and say hello.",
      "location": "73 High Street, Ware, Herts, SG12 9AD",
      "twitter": "@lulucoffeeco",
      "handle": "lulu-coffee-company",
      "url": "http://lulucoffee.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0326, 51.8112]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "MacBeans Coffee",
      "url": "https://www.macbeans.com/",
      "location": "2 Little Bemont Street, Aberdeen, Scotland, AB10 1JG",
      "profile_image_url": "pbs.twimg.com/profile_images/674961154461073408/edeKnEbk.jpg",
      "updated_at": "09-Mar-2016 16:02",
      "twitter": "@macbeanscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1006, 57.1468]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Makushi Coffee Roasters",
      "description": "Makushi is a micro roaster on Steep Hill, Lincoln. They only roast sustainably sourced, traceable, high quality, single origin coffee. The green coffees they buy are typically priced a premium above the cost of production has been paid to the farmers, who are often in regions that need it most. They are part of a coffee chain that delivers the best possible coffee while sustainably supporting everyone in that chain, from the farmer, to exporter, roaster, barista and ultimately the consumer.",
      "location": "12 Steep Hill, Lincoln, Lincolnshire, LN2 1LT",
      "handle": "makushi-coffee-roasters",
      "url": "http://makushi.bigcartel.com",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5386, 53.233]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "ManCoCo",
      "url": "https://mancoco.co.uk/",
      "location": "84 Hewitt St, Manchester, M15 4GB",
      "profile_image_url": "https://pbs.twimg.com/profile_images/582474089350242304/bK9PO5gd_400x400.jpg",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@ManCoCoLtd",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2499, 53.4739]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Manx Tea And Coffee",
      "url": "http://www.manxteaandcoffee.com",
      "location": "Unit 4, Rear Wilson & Collins, Balthane Industrial Estate, Ballsalla, Isle of Man, IM9 2AJ",
      "profile_image_url": "manxteaandcoffee.com/image/data/logo.png",
      "updated_at": "06-May-2015 15:45",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.6023, 54.0927]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Mariners Coffee",
      "url": "http://www.marinerscoffeemerchants.co.uk",
      "location": "Unit 55, The Raylor Centre James Street, York, YO10 3DW",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/mariners-coffee-logo.png",
      "updated_at": "03-Jun-2015 13:59",
      "twitter": "@MarinersCoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.0656, 53.9568]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Markus Coffee",
      "url": "https://www.markuscoffee.com/",
      "location": "13 Connaught Street, London",
      "profile_image_url": "pbs.twimg.com/profile_images/1543220214/MarkusCC_800pixel_72dpi_RGB_400x400.jpg",
      "updated_at": "06-May-2015 15:32",
      "twitter": "@Markus__Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1652, 51.5145]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Masteroast Coffee Co Ltd",
      "url": "https://www.masteroast.co.uk/",
      "location": "Plantation House, Newark Road, Peterborough, Cambridgeshire, PE1 5UA",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/masteroast-logo.jpg",
      "updated_at": "18-May-2015 10:52",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2104, 52.576]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "16 Lawmoor Road, Glasgow, Scotland, G5 0UL",
      "name": "Matthew Algie",
      "updated_at": "2020-06-28 02:35:18 UTC",
      "url": "https://www.matthewalgie.com/",
      "twitter": "@Matthew_Algie",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2485, 55.84]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "83, 82 Railway St, Leeds, West Yorkshire, LS9 8HB",
      "name": "Maude Coffee",
      "updated_at": "2020-04-27 00:44:49 UTC",
      "url": "https://www.maudecoffee.co.uk/",
      "twitter": "@maudecoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5299, 53.7967]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Chester, Cheshire",
      "name": "Merchant and Miller Cheshire Coffee",
      "updated_at": "2020-05-21 07:27:46 UTC",
      "url": "https://www.merchantandmiller.co.uk/?utm_source=thecoffeeroasters&utm_medium=profilelink",
      "twitter": "@MerchantMiller_",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8931, 53.1934]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Method Roastery",
      "url": "https://methodroastery.com/",
      "location": "Unit 7, Hop Pocket Craft Centre, Bishops Frome, Herefordshire, WR6 5BT",
      "profile_image_url": "methodroastery.com/wp-content/uploads/2014/10/method-logo-black.png",
      "updated_at": "03-Jun-2015 13:50",
      "twitter": "@MethodRoastery",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.4942, 52.1221]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Microroastery",
      "url": "https://microroastery.co.uk/",
      "location": "4 St.Margarets Street, Canterbury, Kent, CT1 2TP",
      "profile_image_url": "pbs.twimg.com/profile_images/577412933040381952/xbNzeGPR_400x400.jpeg",
      "updated_at": "06-May-2015 15:30",
      "twitter": "@microroastery",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.0793, 51.2777]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Milly's Coffee Co",
      "description": "Millys Coffee Company is a small family run business, built from the dreams of the managing director to embody his passion and love for coffee. We are the only coffee company in the heart of the Scottish borders and the main distributor for Italian Aroma. We cover South East Scotland from Berwick upon tweed to the heart of Scotland's capital Edinburgh and back down to the Northumberland area.",
      "location": "Hawick, Scottish Borders, TD9 9NS",
      "twitter": "@MillysCoffeeCo",
      "handle": "milly's-coffee-co",
      "url": "http://millyscoffeecompany.com",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7794, 55.427]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "MissionCoffeeWorks",
      "url": "https://www.missioncoffeeworks.com/",
      "location": "4 Grosvenor Way, London, E5 9ND",
      "profile_image_url": "https://pbs.twimg.com/profile_images/668458259586662402/eT0rO2Jc.jpg",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@MissionCoffeeW",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0532, 51.5649]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 6 Capstan Centre, Tilbury, Essex, RM18 7HH",
      "name": "Modern Standard Coffee",
      "url": "https://modernstandardcoffee.co.uk/",
      "updated_at": "2020-06-28 04:08:10 UTC",
      "twitter": "@MSCroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.3426, 51.4696]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Mokarabia Coffee",
      "url": "http://www.mokarabia.co.uk",
      "location": "London",
      "profile_image_url": "https://pbs.twimg.com/profile_images/3503326027/99c7fa48c1891e70f4c629e27b4e8463_400x400.png",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@MokarabiaUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "2 Park St, London, SE1 9AB",
      "name": "Monmouth Coffee",
      "updated_at": "2020-06-28 03:04:15 UTC",
      "url": "https://www.monmouthcoffee.co.uk/",
      "twitter": "@monmouthcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0915, 51.5054]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, The Studio Alscot Park, Atherstone on Stour, Stratford upon Avon, Warwickshire, CV37 8BL",
      "name": "Monsoon Estates",
      "updated_at": "2020-06-29 05:36:36 UTC",
      "url": "https://monsoonestates.co.uk/",
      "twitter": "@MonsoonEstates",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.7099, 52.1907]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Brown Candover, Alresford, Hampshire, SO24 9TN",
      "name": "Moonroast Coffee",
      "updated_at": "2020-06-28 04:36:29 UTC",
      "url": "https://www.moonroast.co.uk",
      "twitter": "@MoonRoast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1773, 51.1493]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "mr_eion",
      "url": "https://facebook.com/mreionltd",
      "location": "9 DPS, Stockbridge, Edinburgh, Scotland",
      "profile_image_url": "pbs.twimg.com/profile_images/378800000766854701/ecb4e5eabd94c16bdcf7db7e982b05bc_400x400.jpeg",
      "updated_at": "06-May-2015 15:42",
      "twitter": "@mr_eion",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.2088, 55.9579]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "mug run roasting",
      "url": "http://mug-run.co.uk",
      "location": "Unit E3, Morfa Clwyd, Marsh Road, Rhyl, Wales, LL18 2AF",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/mug-run-logo.jpg",
      "updated_at": "13-Nov-2017 11:19",
      "twitter": "@mug_run",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.4934, 53.3144]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "My Daily Coffee",
      "description": "As devoted seekers of singularity and true to the concepts of origin and direct trade, we are a pleased to offer you a selection of dedicatedly sourced and hand roasted. Colombian speciality coffee to be brewed whit equal care. We are keen at hunting for unique micro lots and varietals throughout Colombia and establishing bonds with farmers and ethnic communities alike in order to bring to you the best quality coffee of the season\u2019s harvest.",
      "location": "Gallows Green, Dunmow, Essex, CM6",
      "handle": "my-daily-coffee",
      "url": "http://mydailycoffee.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.3779, 51.9173]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Nature's Roast",
      "description": "The finest coffee hand roasted in a wood-fired oven using local sustainably sourced wood.",
      "location": "Dorset, UK",
      "twitter": "@NaturesRoast",
      "handle": "natures-roast",
      "url": "http://www.naturesroast.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3382, 50.7391]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Neighbourhood Coffee",
      "url": "https://www.www.neighbourhoodcoffee.co.uk/",
      "location": "Liverpool, Merseyside",
      "profile_image_url": "www.neighbourhoodcoffee.co.uk/wp-content/uploads/2014/10/logowhite2.png",
      "updated_at": "06-May-2015 15:53",
      "twitter": "@NhoodCoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.9916, 53.4084]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "New Ground Coffee",
      "updated_at": "2020-05-21 08:58:57 UTC",
      "url": "https://www.newgroundcoffee.com/",
      "location": "Workshop, r/o Simon House, 2 Windmill Road, Oxford, OX3 7BU",
      "facebook": "newgroundcoffeesocial",
      "instagram": "@newgroundcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2111, 51.7594]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "New Town Coffee",
      "url": "http://www.newtowncoffee.com",
      "location": "21 York Place, Edinburgh, Scotland, EH1 3EN",
      "profile_image_url": "https://pbs.twimg.com/profile_images/2802960198/8ff44627788a5b8c3ea80b444be2027e_400x400.jpeg",
      "updated_at": "16-Jul-2018 08:05",
      "twitter": "@NewTownCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.1912, 55.9561]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "New Wave Coffee",
      "url": "http://newwavecoffee.co.uk",
      "location": "Hemel Hempstead, Hertfordshire",
      "profile_image_url": "pbs.twimg.com/profile_images/543052340182257664/Klrl910o.jpeg",
      "updated_at": "17-Sep-2015 09:32",
      "twitter": "@newwavecoffeeuk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.4486, 51.7532]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Newbeans Coffee",
      "updated_at": "2020-06-28 03:06:46 UTC",
      "url": "https://www.newbeans.co.uk/",
      "twitter": "@newbeanscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.0367, 55.7791]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 27, Penraevon Industrial Est., Jackson Road, Meanwood Road, Leeds, West Yorkshire, LS7 2AP",
      "name": "North Star Roast",
      "updated_at": "2020-06-28 01:49:20 UTC",
      "url": "https://www.northstarroast.com/",
      "twitter": "@NorthStarRoast",
      "instagram": "northstarcoffeeshop",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5427, 53.8119]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 5, Meantime Workshops, North Greenwich Road, Spittal, Berwick-Upon-Tweed, Fife, TD15 1RG",
      "name": "Northern Edge Coffee",
      "updated_at": "2020-06-28 04:09:02 UTC",
      "url": "https://www.northernedgecoffee.co.uk/",
      "twitter": "@NorthernEdge_",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.9925, 55.7582]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Crown House, 193 Chatsworth Road, Chesterfield, Derbyshire, S40 2BA",
      "name": "Northern Tea",
      "updated_at": "2020-04-08 01:58:53 UTC",
      "url": "https://www.northern-tea.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.446, 53.2341]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "6A Tileyard Studios, London, N7 9AH",
      "name": "Notes Roastery",
      "updated_at": "2020-06-28 02:30:59 UTC",
      "url": "https://notescoffee.com",
      "twitter": "@NotesRoastery",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1235, 51.5427]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "26 Hanbury St, London, E1 6QR",
      "name": "Nude Coffee Roasters",
      "updated_at": "2020-06-28 03:08:17 UTC",
      "url": "https://www.nudeespresso.com/",
      "twitter": "@NudeEspresso",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0731, 51.5202]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Old Leodensian",
      "url": "http://homeroastcoffee.co.uk",
      "location": "Kippax, Leeds, West Yorkshire, LS25",
      "profile_image_url": "thecoffeeroasters.x10.mx/images/old-leodensian-logo.jpg",
      "updated_at": "01-Aug-2016 12:33",
      "twitter": "@HomeRoastCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.371, 53.7669]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "54 Peckham Rye, London, SE15 4JR",
      "name": "OLD SPIKE ROASTERY",
      "updated_at": "2020-06-11 03:51:12 UTC",
      "url": "https://oldspikeroastery.com/",
      "twitter": "@OldSpikeRoast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0666, 51.4652]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Old Brewery Yard \u00b7 Lower Treluswell, Penryn, Cornwall, TR10 9AT",
      "name": "Olfactory Coffee",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0831/6631/t/16/assets/logo.png",
      "updated_at": "2019-07-04 08:20:24 UTC",
      "url": "https://www.olfactorycoffee.co.uk",
      "twitter": "@olfactorycoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.1155, 50.1802]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, Wheal Vrose Business Park, Helston, Cornwall, TR13 0FG",
      "name": "Origin Coffee",
      "updated_at": "2020-06-10 10:41:00 UTC",
      "url": "https://www.origincoffee.co.uk",
      "twitter": "@origincoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.2678, 50.1149]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Foundry Lane Studios, Foundry Lane, Newcastle-Upon-Tyne, NE6 1LH",
      "name": "Ouseburn Coffee Co.",
      "updated_at": "2020-06-28 02:33:50 UTC",
      "url": "https://www.ouseburncoffee.co.uk/",
      "twitter": "@OuseburnCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5905, 54.9747]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Outpost Coffee Roasters",
      "url": "https://www.outpost.coffee/",
      "location": "4 Stoney St, Nottingham, NG1 1LG",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/outpost-coffee.jpg",
      "updated_at": "18-Jun-2019 12:01",
      "twitter": "@OutpostRoasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1438, 52.9534]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Stables, Blackwood Estate, Lesmahagow, South Lanarkshire, Scotland, ML11 0JG",
      "name": "Ovenbird Coffee Roasters",
      "updated_at": "2020-06-10 10:44:12 UTC",
      "url": "https://ovenbird.co.uk",
      "twitter": "@ovenbird_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.9479, 55.6663]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Owens Coffee",
      "url": "https://owenscoffee.com/",
      "location": "New Mills Industrial Estate, Modbury, Ivybridge, Devon, PL21 0TP",
      "profile_image_url": "pbs.twimg.com/profile_images/435424578144190464/SdHrRO6L_400x400.jpeg",
      "updated_at": "06-May-2015 15:34",
      "twitter": "@OwensCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.8935, 50.3504]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Oxenham&Leigh Coffee",
      "url": "http://www.oxenhamleighcoffee.co.uk",
      "location": "Buckland Brewer, North Devon, EX39 5LU",
      "profile_image_url": "https://pbs.twimg.com/profile_images/2766234313/efba74f19a55cb9ef179d12c78c268f6_400x400.jpeg",
      "updated_at": "16-Jul-2018 07:59",
      "twitter": "@OxenhamLeigh",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.252, 50.965]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "OzoneCoffeeRoasters",
      "description": "Independent Coffee Roasters...we source, roast, brew and live coffee.",
      "location": "11 Leonard Street, London EC2A 4AQ",
      "twitter": "@OzoneCoffeeuk",
      "handle": "ozone-coffee-roasters",
      "url": "http://ozonecoffee.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.087, 51.5246]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Pact Coffee",
      "description": "Delicious coffees delivered fresh from roasting to home or work.",
      "location": "The Mint Building, The Biscuit Factory, 100 Clement's Road, Bermondsey, SE16 4DG",
      "twitter": "@pactcoffee",
      "handle": "pact-coffee",
      "url": "https://www.pactcoffee.com/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0628, 51.4942]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Papercup Coffee",
      "url": "https://papercupcoffeecompany.bigcartel.com/",
      "location": "603 Great Western Road, Glasgow, Scotland, G12 8HX",
      "profile_image_url": "https://pbs.twimg.com/profile_images/3607564988/84b2b2927c1bd294cebc39153d6d224f_400x400.jpeg",
      "updated_at": "16-Jul-2018 09:42",
      "twitter": "@pccoffeeuk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2853, 55.8764]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Passion Fruit Coffee",
      "url": "https://passionfruitcoffee.co.uk/",
      "location": "209 Kings Rd, Chorlton, Manchester, M21 0XY",
      "profile_image_url": "http://static.squarespace.com/static/53450a71e4b0081b9666e73f/t/53c0753ee4b00a2450791a54/1414188633473",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@PassionFruitMCR",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2608, 53.4415]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Roastery, 60 Basepoint Business & Innovation Centre, Caxton Close, Andover, Hampshire, SP10 3QN",
      "name": "Peaberry Coffee",
      "updated_at": "2020-06-11 03:47:44 UTC",
      "url": "https://peaberrycoffee.co.uk",
      "twitter": "@peaberry_roast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5074, 51.217]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "12 Blackwood Gardens, Leeds, LS16 7RQ",
      "name": "Pebble & Pine Coffee",
      "updated_at": "2020-06-27 06:20:36 UTC",
      "url": "https://pebbleandpine.co.uk",
      "twitter": "@PebblePine",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.6249, 53.8495]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "28 Sydney street, Brighton, BN1 4EP",
      "name": "Pelicano House",
      "updated_at": "2020-06-28 01:03:49 UTC",
      "url": "https://www.pelicanocoffee.com/",
      "twitter": "@Pelicanocoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1375, 50.8278]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "10 Acacia Business Centre, Howard Rd, Leytonstone, London, E11 3PJ",
      "name": "Perky Blenders Coffee Roasters",
      "updated_at": "2020-06-27 06:25:35 UTC",
      "url": "https://perkyblenders.com/",
      "twitter": "@perkyblenders",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.0074, 51.5588]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Pharmacie Coffee Roasters",
      "url": "https://pharmacie.coffee/",
      "location": "18 Cambridge Grove, Brighton and Hove, BN3 3ED",
      "profile_image_url": "thecoffeeroasters.x10.mx/images/pharmacie_roasters_logo.jpg",
      "updated_at": "05-Apr-2016 10:53",
      "twitter": "@pharmaciecoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1657, 50.8336]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Marygate, Holy Island, Northumberland, TD15 2SJ",
      "name": "Pilgrims Coffee",
      "updated_at": "2020-06-16 04:25:50 UTC",
      "url": "https://www.pilgrimscoffee.com/",
      "twitter": "@PilgrimsCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8005, 55.6712]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Pollards Shop",
      "url": "http://pollardscoffee.co.uk",
      "location": "627 Ecclesall Rd, Sheffield, South Yorkshire, S11 8PT",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/pollards-logo.jpg",
      "updated_at": "03-Feb-2019 12:02",
      "twitter": "@PollardsShopUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5002, 53.3681]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Units A, B & C Tinsley Industrial Estate, Shepcote Lane, Sheffield, South Yorkshire, S9 1DR",
      "name": "Pollards Wholesale Coffee",
      "updated_at": "2020-05-21 08:58:37 UTC",
      "url": "http://pollards.com/wholesale/",
      "twitter": "@PollardsUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.408, 53.3965]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 3 Kilcohan Industrial Complex, Kilcohan, Waterford, Ireland",
      "name": "Ponticelli Espresso",
      "updated_at": "2020-06-28 04:41:32 UTC",
      "url": "http://www.ponticelli.ie/",
      "twitter": "@PonticelliE",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-7.1121, 52.2441]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Porter's Coffee",
      "description": "Premium, flame roasted coffee delivered straight to your door.",
      "location": "36 Mossgate Park Heysham LA3 2WN",
      "twitter": "@Getporters",
      "handle": "porters-coffee",
      "url": "http://getporters.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8898, 54.0375]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Preseli Coffee",
      "url": "http://preselicoffee.com",
      "location": "2 Lettards Court, Letterston, Pembrokeshire, Wales, SA62 5SR",
      "profile_image_url": "https://pbs.twimg.com/profile_images/2555447770/iqlkzq03838ilsttzq9f_400x400.jpeg",
      "updated_at": "16-Jul-2018 08:06",
      "twitter": "@PreseliCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.0036, 51.9266]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Pump n Grind",
      "url": "http://pumpngrind.co.uk",
      "location": "Leeds, UK",
      "profile_image_url": "pbs.twimg.com/profile_images/689073941839740928/zbHH4M3K.jpg",
      "updated_at": "27-Oct-2016 22:21",
      "twitter": "@pumpngrind",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5491, 53.8008]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Pumphrey's Coffee",
      "url": "https://www.pumphreys-coffee.co.uk/",
      "location": "Bridge Street, Blaydon, Tyne and Wear, NE21 4JH",
      "profile_image_url": "cdn6.bigcommerce.com/s-nbc124/product_images/black_logo_header_1413552990__33838.jpg",
      "updated_at": "06-May-2015 15:42",
      "twitter": "@PumphreysBE",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.7181, 54.9661]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Puro Gusto Coffee",
      "description": "Boutique Irish Roaster with a passion for all things coffee. We'd love you to try our roasts. DM us and we might be able to arrange some samples. Enjoy!!",
      "location": "Dublin Ireland",
      "twitter": "@PuroGustoCoffee",
      "handle": "puro-gusto-coffee",
      "url": "https://facebook.com/purogustocoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2603, 53.3498]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Annacotty Business Park, Annacotty, Limerick, Ireland",
      "name": "P\u00f3naire Irish Handcrafted Coffee",
      "updated_at": "2020-06-28 04:43:48 UTC",
      "url": "https://www.ponaire.ie/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-8.5259, 52.6696]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Quarter Horse Coffee",
      "url": "https://quarterhorsecoffee.com/",
      "location": "88-90 Bristol street, Birmingham, B5 7AH",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0744/8895/files/QH_Logo_0219-02_WEB_400x200.jpg",
      "updated_at": "01-May-2019 08:17",
      "twitter": "@QtrHorseCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8993, 52.4716]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 7, Stirling Works, Love Lane, Cirencester, Gloucestershire, GL7 1YG",
      "name": "Rave Coffee",
      "profile_image_url": "cdn.shopify.com/s/files/1/0390/4361/t/2/assets/logo.png",
      "updated_at": "2019-07-04 17:01:12 UTC",
      "url": "https://ravecoffee.co.uk/",
      "twitter": "@RaveCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.9607, 51.705]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "LIMEKILN FARM, SHERBORNE, DORSET, DT9 6PS",
      "name": "Reads Coffee",
      "updated_at": "2020-06-28 03:47:47 UTC",
      "url": "http://readscoffee.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5159, 50.9365]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Stanley Rd, Deal, Kent, CT14 7BT",
      "name": "Real Deal Roasters",
      "updated_at": "2020-06-28 03:59:12 UTC",
      "url": "https://www.realdealroasters.co.uk",
      "twitter": "@realdealroaster",
      "facebook": "realdealroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.4036, 51.2213]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 4C, Lake Road Estate, Coniston, Cumbria, LA21 8EW",
      "name": "Red Bank Coffee Roasters",
      "updated_at": "2020-04-27 00:52:22 UTC",
      "url": "https://redbankcoffee.com",
      "twitter": "@redbankroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0746, 54.3673]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Red Cherry coffee",
      "url": "https://redcherrycoffee.co.uk/",
      "location": "Whitstable, Kent",
      "profile_image_url": "pbs.twimg.com/profile_images/835523708/red_cherry_logo3_400x400.jpg",
      "updated_at": "06-May-2015 15:38",
      "twitter": "@redcherrycoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.0243, 51.361]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Red Monkey Coffee UK",
      "url": "http://www.redmonkeycoffee.co.uk",
      "location": "Bache Farm, Westhope, Near Ludlow, Shropshire, SY7 9LG",
      "profile_image_url": "www.redmonkeycoffee.co.uk/rmcsplash_r1_c1.gif",
      "updated_at": "06-May-2015 15:45",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7687, 52.4563]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Red Roaster",
      "url": "https://www.redroaster.co.uk/",
      "location": "1d St James's St, Brighton, BN2 1RE",
      "profile_image_url": "pbs.twimg.com/profile_images/112755555/1428829670_fb21155c78_400x400.jpg",
      "updated_at": "06-May-2015 15:41",
      "twitter": "@theredroaster",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1362, 50.8211]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Redber",
      "url": "https://www.redber.co.uk/",
      "location": "Unit 2, Merrow Depot Merrow Lane, Guildford, Surrey, GU4 7BQ",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/redber-logo.png",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@RedberCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5311, 51.2575]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Suite 3, Maybank Business Centre, 208 Maybank Road, London, E18 1ET",
      "name": "Regal Coffee Ltd.",
      "updated_at": "2020-06-27 06:46:30 UTC",
      "url": "https://www.regalcoffeeroasters.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.0369, 51.5972]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Kendal, Cumbria",
      "name": "Rinaldo's Coffee",
      "updated_at": "2019-12-21 17:45:31 UTC",
      "url": "https://rinscoffee.com",
      "twitter": "@RinsCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7463, 54.328]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Ristretto Coffee",
      "url": "https://ristrettocoffee.com/",
      "location": "Unit 49, Banbridge Enterprise Centre, Scarva Road Industrial Estate, Banbridge, County Down, Ireland, BT32 3QD",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/ristretto_logo_footer.jpg",
      "updated_at": "06-May-2015 15:42",
      "twitter": "@ristrettocoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.291, 54.3499]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Ritual Coffee",
      "updated_at": "2020-05-21 08:59:06 UTC",
      "url": "https://ritualcoffee.org",
      "location": "Cheltenham, Gloucestershire",
      "facebook": "RitualCoffeeCompany",
      "instagram": "ritualcoffeecompany",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.0783, 51.8994]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roast Batch",
      "url": "http://roastbatch.com",
      "location": "Newcastle-upon-Tyne",
      "profile_image_url": "s3.amazonaws.com/cratejoy_vendor_images/2331705d33074c248336506588290cfa.png",
      "updated_at": "01-Aug-2016 12:20",
      "twitter": "@RoastBatch",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.6178, 54.9783]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roast Central",
      "description": "An independent on line coffee roaster based in Falkirk! We roast brilliant coffee to order, and send it straight to you!",
      "location": "Falkirk",
      "twitter": "@RoastFiend",
      "handle": "roast-central",
      "url": "http://www.roastcentral.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.7839, 56.0019]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roast Lab Coffee Roasters",
      "updated_at": "2020-05-21 06:53:37 UTC",
      "url": "https://roastlab.coffee",
      "linked_in_handle": "roastlabcoffeeroasters",
      "location": "Langtons Meadow, Farnham Common, Buckinghamshire, SL2 3NS",
      "facebook": "roastlabcoffeeroasters",
      "instagram": "roastlabcoffeeroasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.6108, 51.555]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 18, Kenn Court Business Park, Roman Farm Road, Bristol, BS4 1UL",
      "name": "Roasted Rituals",
      "profile_image_url": "https://pbs.twimg.com/profile_images/595612956328665089/WFfW8uhk_400x400.jpg",
      "updated_at": "2019-11-17 18:16:50 UTC",
      "url": "https://roastedritualscoffee.com/",
      "twitter": "@RoastedRituals",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5891, 51.4183]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roaster B",
      "description": "Inspired by the world\u2019s greatest cities, we are passionate about capturing the spirit of each city within a pack of high quality freshly roasted coffee beans.",
      "location": "Windsor, United Kingdom",
      "twitter": "@roasterbcoffee",
      "handle": "roasterb-coffee-co-windsor",
      "url": "http://www.roasterb.com",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.6136, 51.4817]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Old Quarry Farm, Newton Abbot, Devon, TQ12 5FN",
      "name": "Roasters Artisan",
      "updated_at": "2020-02-24 22:59:51 UTC",
      "url": "https://www.roasterscoffee.com",
      "twitter": "@roastersartisan",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.5831, 50.5113]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 7, Blackdown park, Willand, Devon, EX15 2FS",
      "name": "Roastworks Coffee Co",
      "profile_image_url": "https://pbs.twimg.com/profile_images/1022151487991033857/Xcl9JEGr_400x400.jpg",
      "updated_at": "2019-07-04 08:43:48 UTC",
      "url": "https://roastworks.co.uk",
      "twitter": "@RoastworksDevon",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.3738, 50.8943]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roberts & Co.",
      "url": "http://www.e-coffee.co.uk",
      "location": "The Coffee Roastery, Cedar Farm, Back Lane, Mawdesley, Ormskirk, Lancashire, L40 3SY",
      "profile_image_url": "www.e-coffee.co.uk/skins/roberts/media/logo.png",
      "updated_at": "06-May-2015 15:46",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.7654, 53.6205]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roost",
      "url": "https://www.roostcoffee.co.uk/",
      "location": "Malton, North Yorkshire",
      "profile_image_url": "www.roostcoffee.co.uk/wp-content/uploads/2015/11/Roost-Coffee-Logo3.png",
      "updated_at": "12-May-2016 09:36",
      "twitter": "@Roost_Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.7979, 54.1368]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 10, Mill Road Industrial Estate, Radstock, Near Bath, BA3 5TX",
      "name": "Round Hill Roastery",
      "updated_at": "2020-06-28 01:45:44 UTC",
      "url": "https://roundhillroastery.com",
      "twitter": "@roundhillcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.4367, 51.2941]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Roundsquare Roastery",
      "description": "Ayrshire's only coffee roastery. Hand roasted, the artisan way. sales@roundsquare.org.uk",
      "location": "Above Su Casa Coffee House, Unit 4, Lorne Arcade, 115 High St, Ayr KA7 1QL",
      "twitter": "@RoundsquareAyr",
      "handle": "roundsquare-roastery",
      "url": "http://www.roundsquareroastery.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.6305, 55.4627]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Granary, East Rounton, Northallerton, North Yorkshire, DL6 2LG",
      "name": "Rounton Coffee Roasters",
      "updated_at": "2019-12-22 11:02:47 UTC",
      "url": "https://www.rountoncoffee.co.uk/",
      "twitter": "@RountonCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3294, 54.4248]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Sacred Grounds Coffee Company",
      "url": "https://sacred-grounds.coffee/",
      "location": "Arbroath, Scotland",
      "profile_image_url": "pbs.twimg.com/profile_images/581091553042665472/6ccuusvu_400x400.jpg",
      "updated_at": "01-Aug-2016 12:35",
      "twitter": "@SacredGrounds14",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5915, 56.5591]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Sasha House Petite",
      "url": "http://shpetite.ie",
      "location": "Drury Street Carpark, Drury Street, Dublin, Ireland",
      "profile_image_url": "shpetite.ie/images/logo.gif",
      "updated_at": "06-May-2015 15:49",
      "twitter": "@SashaHouseDub",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2634, 53.3422]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Second City Coffee",
      "url": "https://www.secondcitycoffee.co.uk/",
      "location": "Manchester",
      "profile_image_url": "secondcitycoffee.co.uk/wp-content/uploads/2014/10/2ND-CITY-LOGO-HOLDING-PAGE1.png",
      "updated_at": "06-May-2015 15:58",
      "twitter": "@secondctycoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2426, 53.4808]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Sidewalk Coffee Co",
      "url": "https://www.sidewalkcoffee.co.uk/",
      "location": "Unit 1, School Court, Furlong Way, Highfields Caldecote, Cambridge, CB23 7AA",
      "profile_image_url": "pbs.twimg.com/profile_images/756920402832687104/pdtO0l2I.jpg",
      "updated_at": "17-Feb-2017 22:05",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0251, 52.2077]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "The Lodge, English Drove, Thorney, Peterborough, Cambridgeshire, PE6 0TL",
      "name": "Silver Oak Coffee",
      "updated_at": "2020-06-10 10:47:45 UTC",
      "url": "https://silveroakcoffee.co.uk/",
      "twitter": "@SilverOakCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1059, 52.6218]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 13 Blackwater Road, Dublin Industrial Estate, Dublin, Ireland , 11",
      "name": "Silverskin Coffee",
      "updated_at": "2020-06-28 01:09:59 UTC",
      "url": "https://silverskincoffee.ie/",
      "twitter": "@Silverskin_",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.291, 53.3726]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Antrim, Northern Ireland",
      "name": "Slumberjack Coffee",
      "updated_at": "2020-11-11 03:16:58 UTC",
      "url": "https://www.slumberjackcoffee.com",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.2072, 54.7195]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "68 Goldstone Villas, Hove, Brighton and Hove, BN3 3RU",
      "name": "Small Batch Coffee",
      "updated_at": "2020-06-28 03:10:42 UTC",
      "url": "https://www.smallbatchcoffee.co.uk/",
      "twitter": "@SmallBatchCR",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1715, 50.8338]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "49 St Joseph's Road, Handsworth , Sheffield, South Yorkshire, S13 9AU",
      "name": "Smith Street Coffee",
      "updated_at": "2020-06-28 05:07:18 UTC",
      "url": "https://www.smithstreetcoffeeroasters.co.uk/",
      "twitter": "@SmithStCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3863, 53.3728]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Smiths Coffee Company",
      "description": "Smiths are specialist coffee bean suppliers in the UK. We are delighted to offer our customers a comprehensive range of freshly roasted coffee beans from around the world. This includes single estate, speciality, Fairtrade and organic coffees as well as a wide range of blends to suit every occasion. A range of flavoured coffees and syrups are also available",
      "location": "Arabica House, Ebberns Road, Apsley, Hemel Hempstead, Herts HP3 9RD",
      "twitter": "none",
      "handle": "smiths-coffee-company",
      "url": "https://www.smithscoffee.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.4632, 51.7373]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "2 Earnshaw Court, Norwich, Norfolk, NR7 0BJ",
      "name": "Smokey Barn Coffee",
      "updated_at": "2020-06-28 03:13:41 UTC",
      "url": "https://www.smokeybarn.co.uk/",
      "twitter": "@SmokeyBarn",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.3366, 52.6272]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Southampton",
      "name": "SOroast",
      "updated_at": "2020-06-28 01:03:41 UTC",
      "url": "https://www.soroastcoffee.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4044, 50.9097]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "London",
      "name": "Specialty Coffee Co",
      "updated_at": "2020-06-28 03:15:44 UTC",
      "url": "https://www.thespecialtycoffeecompany.com",
      "twitter": "@SpecialtyCofCo",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Spectrum Coffee",
      "url": "http://www.spectrumcoffeeroasters.co.uk",
      "location": "20J Evans Business Park, Marston Moor Business Park, Rudgate, Tockwith, North Yorkshire, YO26 7QF",
      "profile_image_url": "cdn.shopify.com/s/files/1/1017/9983/t/3/assets/logo.png",
      "updated_at": "19-Dec-2015 09:52",
      "twitter": "@spectrum_york",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3065, 53.9653]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Spiller & Tait",
      "url": "https://www.spillerandtait.co.uk/",
      "location": "Units 1&2, South Farm Court, South Farm Road,  Budleigh Salterton, Devon, EX9 7AZ",
      "profile_image_url": "www.spillerandtait.co.uk/uploads/3/4/4/8/3448017/1394779503.png",
      "updated_at": "06-May-2015 15:59",
      "twitter": "@SpillerandTait",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.3147, 50.6393]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Square Mile Coffee",
      "url": "https://shop.squaremilecoffee.com/",
      "location": "8 Pritchards Rd, London, E2 9AP",
      "profile_image_url": "https://pbs.twimg.com/profile_images/875669568085262336/6wKNlhXc_400x400.jpg",
      "updated_at": "02-May-2019 20:31",
      "twitter": "@squaremile",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0613, 51.5326]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "12 Station Yard, Edington, Wiltshire, BA13 4NT",
      "name": "Square root Coffee",
      "updated_at": "2020-06-28 05:02:22 UTC",
      "url": "https://www.squarerootcoffee.com/",
      "twitter": "@sqrootcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.1104, 51.283]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "49a Kirk Ports North, Berwick, East Lothian, Scotland, EH39 4HL",
      "name": "Steampunk Coffee Roasters",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/1488/1242/files/croppedtotextlogo-01_copy_400x200.png?v=1489677269",
      "updated_at": "2019-06-20 17:08:57 UTC",
      "url": "https://www.steampunkcoffee.co.uk/",
      "twitter": "@SteampunkCoffee",
      "facebook": "steampunkcoffee",
      "instagram": "steampunkcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.719, 56.0581]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Steencup Coffee",
      "description": "Official supplier of Sanremo coffee equipment and artisan specialty coffee roaster based in East London",
      "location": "116 Holbrook Rd, Stratford, London, E15",
      "twitter": "@Steencup",
      "handle": "steencup-coffee",
      "url": "http://www.steencup.com",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.0121, 51.5312]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Riverbank Trent Bridge, Nottingham, NG2 2GS",
      "name": "Stewarts Coffees",
      "updated_at": "2020-06-28 01:50:23 UTC",
      "url": "https://www.stewartscoffees.co.uk/",
      "twitter": "@Stewartscoffees",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1347, 52.9378]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Suite 1, The Lawn, Union Road, Lincoln, LN1 3BU",
      "name": "Stokes Tea and Coffee",
      "updated_at": "2020-06-30 09:12:56 UTC",
      "url": "https://stokescoffee.com/",
      "twitter": "@StokesCoffee",
      "facebook": "stokescoffee",
      "instagram": "stokescoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.5415, 53.23]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Norwich, NR2 1DE",
      "name": "Strangers Coffee",
      "updated_at": "2020-06-27 06:22:59 UTC",
      "url": "https://strangerscoffee.com/",
      "twitter": "@StrangersCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.2928, 52.6295]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Stubbs Coffee",
      "url": "https://facebook.com/stubbscoffees",
      "location": "London",
      "profile_image_url": "https://pbs.twimg.com/profile_images/613646706757009408/tHOvBtBv_400x400.png",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@stubbscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Sundlaug Coffee Co.",
      "description": "Sundlaug Coffee Co. is a small, independent speciality coffee roastery. We source some of the best coffees available, with an emphasis on traceability and sustainability, before carefully roasting them in small batches to ensure our customers always receive the freshest beans. Our roasting style is influenced by Nordic coffee culture, typified by a focus on the highest quality beans and lighter roast profiles that allow different flavours to shine through in each cup.",
      "location": "Unit B, Brewery Yard, Welbeck, Worksop, Nottinghamshire, S80 3LT",
      "twitter": "@sundlaugcoffee",
      "handle": "sundlaug-coffee-co",
      "url": "http://sundlaugcoffee.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1691, 53.2599]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Sydney Road Coffee",
      "url": "http://SydneyRoadCoffee.co.uk",
      "location": "Unit 26, Space Business Centre, Olympus Park, Quedgeley, Gloucester, GL2 4AL",
      "profile_image_url": "pbs.twimg.com/profile_images/624525589878341632/RzM1CVyM_400x400.jpg",
      "updated_at": "21-Sep-2015 16:52",
      "twitter": "@SydRdCoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2738, 51.8285]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "T-A-P",
      "url": "http://tapcoffee.co.uk",
      "location": "193 Wardour Street, London, W1F 8ZF",
      "profile_image_url": "https://instagram.fmxp1-1.fna.fbcdn.net/vp/89ac938eb303b1ccaf5df3f58dc99542/5D65FD49/t51.2885-19/s320x320/45272561_1918529388263517_8789073267529875456_n.jpg?_nc_ht=instagram.fmxp1-1.fna.fbcdn.net",
      "updated_at": "02-May-2019 20:57",
      "twitter": "@tapcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1358, 51.5154]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Tamp Culture Coffee",
      "description": "Speciality Coffee Roasters crafting flat whites and brewing on the AeroPress @ The Oracle, Reading",
      "location": "The Oracle shopping Centre, Reading, RG1 2AG",
      "twitter": "@TampCulture",
      "handle": "tamp-culture-coffee",
      "url": "http://tampculture.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.9713, 51.4536]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "53 Church Street, Leigh, Greater Manchester, WN7 1AY",
      "name": "Tank Coffee",
      "updated_at": "2020-06-10 10:49:51 UTC",
      "url": "https://www.tankcoffee.com/",
      "twitter": "@TankCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5164, 53.498]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Tapa Organic Glasgow",
      "url": "https://www.digitalgabbar.com/",
      "location": "721 Pollokshaws Rd, Strathbungo, Glasgow, Scotland, G41 2AA",
      "profile_image_url": "pbs.twimg.com/profile_images/378800000370291822/e503fc068909d2168bbe94350c65ea77_400x400.jpeg",
      "updated_at": "06-May-2015 15:43",
      "twitter": "@tapaorganic",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.2707, 55.8359]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Tate",
      "url": "http://tate.org.uk/visit/coffee-by-tate",
      "location": "Herne Hill, London",
      "profile_image_url": "https://storage.googleapis.com/tate-digital/ui/3.3.1-compressed/static/images/tate-logo.png",
      "updated_at": "02-May-2019 20:47",
      "twitter": "@benjaminpres",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.101, 51.457]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "3 Creekside, Deptford, London, SE8 4SA",
      "name": "Taylor St Baristas",
      "updated_at": "2020-05-21 08:58:35 UTC",
      "url": "https://taylorstcoffee.myshopify.com/",
      "twitter": "@Taylor_St",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0218, 51.4765]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Taylors of Harrogate",
      "url": "https://www.taylorsofharrogate.com/",
      "location": "1 Parliament Street, Harrogate, North Yorkshire, HG1 2QU",
      "profile_image_url": "pbs.twimg.com/profile_images/595502185674334208/vrED3L7N_400x400.jpg",
      "updated_at": "03-Jun-2015 14:03",
      "twitter": "@TaylorsCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5431, 53.9932]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 17, Millmead industrial estate, Tottenham Hale, London, N17 9BU",
      "name": "TERRONE Coffee UK",
      "updated_at": "2020-06-28 02:34:22 UTC",
      "url": "https://www.terrone.co.uk",
      "twitter": "@Terrone",
      "facebook": "TerroneUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0568, 51.5909]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "67 George St, Perth, Perthshire, Scotland, PH1 5LB",
      "name": "The Bean Shop",
      "updated_at": "2020-06-28 03:32:11 UTC",
      "url": "https://www.thebeanshop.co.uk",
      "twitter": "@TheBeanShopUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.4276, 56.3981]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Humber St Market, Hull and 22 Unit Factory Estate, Boulevard, Hull, Kingston upon Hull, HU3 4AY",
      "name": "The Blending Room",
      "updated_at": "2020-06-28 03:16:41 UTC",
      "url": "https://www.theblendingroom.co.uk/",
      "twitter": "@TheBlendingRoom",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.3622, 53.7338]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Blue Bean Coffee Co.",
      "url": "https://www.thebluebeancoffee.co.uk/",
      "location": "Kent",
      "profile_image_url": "pbs.twimg.com/profile_images/550704918919909376/qdE_gMlW_400x400.jpeg",
      "updated_at": "01-Aug-2016 10:25",
      "twitter": "@TheBlueBeanCo",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.5217, 51.2787]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Coffee Bean - Van & Roaster",
      "url": "https://www.thecoffeebean-vanandroaster.co.uk/",
      "location": "Aberdare, South Wales",
      "profile_image_url": "pbs.twimg.com/profile_images/528205464387862530/9XBU2VUn_400x400.png",
      "updated_at": "06-May-2015 15:46",
      "twitter": "@CoffeebeanThe",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.4518, 51.7162]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Coffee Circle - James Guard",
      "description": "Hand roasting beautiful coffees for the good good people of Manchester",
      "location": "Manchester",
      "twitter": "@CoffeeCircle",
      "handle": "james-guard",
      "url": "http://www.thecoffeecircle.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.2485, 53.4793]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Coffee Company - Torquay",
      "url": "https://www.coffeecompanytorquay.com/",
      "location": "70A Windsor Road, Torquay, Devon, TQ1 1SZ",
      "profile_image_url": "",
      "updated_at": "06-May-2015 15:46",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.5245, 50.4738]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit G, Housham Hall, Matching Tye, Essex, CM17 0PB",
      "name": "The Coffee Officina",
      "updated_at": "2020-06-10 10:50:59 UTC",
      "url": "https://thecoffeeofficina.com/",
      "twitter": "@coffeeofficina",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.1786, 51.7861]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Festival House, Jessop Avenue, Cheltenham, Gloustershire, GL50 3SH",
      "name": "The Coffee Pod",
      "updated_at": "2020-06-04 02:59:58 UTC",
      "url": "https://facebook.com/ScandinavianCoffeePod",
      "twitter": "@PodCoffee",
      "facebook": "ScandinavianCoffeePod",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.0831, 51.9006]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Coffee Roasters",
      "description": "Over 80 splendid coffees from 13 artisan roasters - all in one place",
      "location": "Nightingale House, Gloucester Rd, Bath, BA1 8BJ",
      "twitter": "@CoffeeRoastUK",
      "handle": "the-coffee-roasters",
      "url": "https://thecoffeeroasters.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3444, 51.4113]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit C, Duck Farm Workshop, Puddletown, Dorchester, Dorset, DT2 8QL",
      "name": "The Dorset Coffee Company",
      "updated_at": "2020-06-28 05:00:36 UTC",
      "url": "https://dorsetcoffee.co.uk",
      "twitter": "@dorsetcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3689, 50.722]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "46-47 iO Centre, Armstrong Road  Royal Arsenal, Woolwich, London, SE18 6AT",
      "name": "The Drury Tea & Coffee Co. Ltd.",
      "updated_at": "2020-06-30 09:20:58 UTC",
      "url": "https://www.drurycoffee.com",
      "twitter": "@DruryUK",
      "facebook": "DruryUK",
      "instagram": "drury_uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0797, 51.4949]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Ethiopian Coffee Co",
      "url": "https://www.theethiopiancoffeecompany.co.uk/",
      "location": "61 Amwell Street, Islington, London, EC1R 1UR",
      "profile_image_url": "pbs.twimg.com/profile_images/414259197/to_go_400x400.jpg",
      "updated_at": "06-May-2015 15:39",
      "twitter": "@EthiopianCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1106, 51.5298]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Reigate, Surrey",
      "name": "The Fresh Coffee Co",
      "updated_at": "2020-06-28 01:48:46 UTC",
      "url": "https://www.thefreshcoffeecompany.com/",
      "twitter": "@FreshCoffeeCo",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.2059, 51.2373]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Galway Roast",
      "url": "http://thegalwayroast.com",
      "location": "Vicar Street, Tuam, Co. Galway, Ireland",
      "profile_image_url": "pbs.twimg.com/profile_images/1498269508/galway-roast-logo_400x400.jpg",
      "updated_at": "06-May-2015 15:58",
      "twitter": "@galwayroast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-8.8528, 53.5131]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Golden Bean",
      "url": "https://facebook.com/thegoldenbeancork",
      "location": "Ballymaloe House, Shanagarry, Co. Cork, Ireland",
      "profile_image_url": "https://scontent-bru.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/1794589_588912094531962_18220085_n.jpg?oh=c47d484e57665e967a4b4010cd135cd7&oe=554EE9FA",
      "updated_at": "11-Jun-2017 18:11",
      "twitter": "@thegoldenbean",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-8.0748, 51.8652]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "3 Peacock Parade, Lake Street, Leighton Buzzard, Bedfordshire, LU7 1JH",
      "name": "The House of Coffee",
      "updated_at": "2020-06-28 02:31:44 UTC",
      "url": "http://thehouseofcoffee.co.uk",
      "twitter": "@HouseofCoffee1",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.6603, 51.9166]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "The Isle of Wight Espresso Company",
      "url": "http://iow-espresso.co.uk",
      "location": "Spring Tides, 37 Spring Hill, Ventnor, Isle Of Wight, PO38 1PF",
      "profile_image_url": "pbs.twimg.com/profile_images/454013291367383040/E8qPI-QP_400x400.jpeg",
      "updated_at": "06-May-2015 15:46",
      "twitter": "@island_roasted",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2025, 50.5969]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "1 Newtec Place, Magdalen Road, Oxford, Oxfordshire, OX4 1RE",
      "name": "The Missing Bean",
      "updated_at": "2020-06-28 04:50:57 UTC",
      "url": "https://www.themissingbean.co.uk/",
      "twitter": "@TheMissingBean",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2358, 51.7418]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "71 Carron Place, Kelvin Industrial Estate, East Kilbride, Glasgow, Scotland, G75 0YL",
      "name": "The Roast Den",
      "updated_at": "2020-06-28 04:49:46 UTC",
      "url": "http://roast-den.com",
      "twitter": "@RoastdenUK",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.1716, 55.7457]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Brighton",
      "name": "The Roasted Bean Co.",
      "updated_at": "2020-06-28 01:30:38 UTC",
      "url": "https://www.roastedbean.co.uk/",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1372, 50.8225]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Winchester, Hampshire, SO22 6BB",
      "name": "The Roasting Party",
      "updated_at": "2020-06-28 01:49:58 UTC",
      "url": "https://theroastingparty.co.uk",
      "twitter": "@RoastingParty",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.3278, 51.0703]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Clapton, London, E5",
      "name": "The Roasting Shed",
      "updated_at": "2020-06-28 03:26:12 UTC",
      "url": "https://www.theroastingshed.com/",
      "twitter": "@theroastingshed",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.057, 51.5616]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "55 Main Road, Ogmore By Sea, The Vale of Glamorgan, South Wales, CF32 0PL",
      "name": "The Welsh Coffee Co",
      "updated_at": "2020-06-28 02:34:44 UTC",
      "url": "http://welshcoffee.com",
      "twitter": "@welshcoffeeco",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.6058, 51.4558]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "TheRoastHouseTralee",
      "url": "http://www.theroasthouse.ie/",
      "location": "3 Denny Street, Tralee, Co. Kerry, Ireland",
      "profile_image_url": "pbs.twimg.com/profile_images/3124737762/3dbd4db45f1101000a0dab57ecf47ea7_400x400.jpeg",
      "updated_at": "03-Jun-2015 13:45",
      "twitter": "@Roast_House",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-9.7054, 52.2691]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Thistledown Cottage Coffee",
      "description": "Small batch roaster of quality coffees from around the world, based in Suffolk. Available online and at a selection of local Farmers Markets.",
      "location": "Thistledown Cottage, 5 The Street, Brome Eye, Suffolk, IP23 8AE",
      "twitter": "@Freshly_Roasted",
      "handle": "thistledown-cottage-coffee",
      "url": "http://www.thistledowncottagecoffee.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.1597, 52.3454]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Thomsons Coffee",
      "url": "https://www.thomsonscoffee.com/",
      "location": "Burnfield Ave, Glasgow, Scotland, G46 7TL",
      "profile_image_url": "pbs.twimg.com/profile_images/564360169186803712/YqpP4Gie_400x400.jpeg",
      "updated_at": "06-May-2015 15:37",
      "twitter": "@thomsonscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-4.3014, 55.8098]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "23 High street, Selkirk, TD7 4BZ",
      "name": "Three Hills Coffee",
      "updated_at": "2020-05-27 05:00:10 UTC",
      "url": "https://www.threehillscoffee.com",
      "twitter": "@3HillsCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.8405, 55.548]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "London",
      "name": "ThreeSixty\u02da Coffee",
      "updated_at": "2020-06-11 03:59:51 UTC",
      "url": "http://www.ThreeSixtyCoffee.co.uk",
      "twitter": "@360_Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "123 Stokes Croft, Bristol, BS1 3RZ",
      "name": "TripleCoRoast",
      "updated_at": "2020-06-27 06:50:51 UTC",
      "url": "https://www.triplecoroast.com",
      "twitter": "@TripleCoRoast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5899, 51.4642]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 7-10 Piper Road, Hardwick Narrows Est, Kings Lynn,  Norfolk, PE30 4BH",
      "name": "Tropic Coffee Ltd",
      "updated_at": "2020-06-28 04:48:20 UTC",
      "url": "https://www.tropiccoffee.co.uk",
      "twitter": "@TropicCoffeeLtd",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.4112, 52.7359]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Twin Cafe",
      "url": "https://www.twincafe.org/",
      "location": "Sheffield, South Yorkshire",
      "profile_image_url": "pbs.twimg.com/profile_images/566598210240532480/egI6jga_.png",
      "updated_at": "06-May-2015 15:59",
      "twitter": "@twincafe12",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4701, 53.3811]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Twin Roasters",
      "description": "Artisan Micro coffee roasters - Richard & Ronan Dalton. Yes, we are real twins! and we roast and ship the finest single origin fresh coffee direct to your door.",
      "location": "Castletown, Drumcliffe, Sligo, Ireland",
      "twitter": "@twinroasters",
      "handle": "twin-roasters",
      "url": "http://www.twinroasters.com",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-8.4976, 54.327]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Two Day Coffee",
      "url": "https://twodaycoffee.co.uk/",
      "location": "135 St Michael's Hill, Bristol, BS2 8BS",
      "profile_image_url": "pbs.twimg.com/profile_images/1165547554/Logo_400x400.jpg",
      "updated_at": "19-May-2015 19:42",
      "twitter": "@TwoDayCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.6016, 51.4606]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Two Dogs Coffee Roasting Company",
      "updated_at": "2020-04-26 06:18:38 UTC",
      "url": "https://www.twodogscoffeecompany.com",
      "location": "Treorchy, Wales, CF42 6RS",
      "facebook": "twodogsroasting",
      "instagram": "@twodogscoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.5051, 51.6607]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit Q16, Greenogue Business Park, Rathcoole, Dublin, Ireland",
      "name": "Two Spots Coffee",
      "updated_at": "2020-06-28 01:50:58 UTC",
      "url": "http://twospotscoffee.ie",
      "twitter": "@twospots_ie",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.4774, 53.2992]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Tynemouth, Newcastle upon Tyne, Tyne & Wear",
      "name": "Tynemouth Coffee Co.",
      "updated_at": "2020-06-28 04:08:54 UTC",
      "url": "http://tynemouthcoffee.com",
      "twitter": "@TynemouthCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.4256, 55.0176]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "11a Windrush Industrial. Park, Linkwood Road, Witney, Oxfordshire",
      "name": "Ue Coffee Roasters",
      "updated_at": "2019-12-22 11:02:56 UTC",
      "url": "https://uecoffeeroasters.com/",
      "twitter": "@uecoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.5194, 51.7918]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "7a South Crescent, London, E16 4TL",
      "name": "Union Hand Roasted",
      "updated_at": "2019-12-22 11:01:07 UTC",
      "url": "https://unionroasted.com/",
      "twitter": "@Unionroasted",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.001, 51.5204]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "United Coffee",
      "description": "With United Coffee, it\u2019s the best cup of coffee every time, both in the home and out of the home. Quality coffee is our passion. We never stand still; we\u2019re forward-thinking, innovative and streets ahead of the competition",
      "location": "2 Bradbourne Drive Tilbrook Milton Keynes MK7 8AT",
      "twitter": "none",
      "handle": "united-coffee",
      "url": "http://www.unitedcoffeeuk.com",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.6886, 52.0102]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "129 High Street, Kinross, Scotland, KY13 8AQ",
      "name": "Unorthodox Roasters",
      "updated_at": "2020-05-21 08:58:33 UTC",
      "url": "https://www.unorthodoxroasters.co.uk",
      "twitter": "@unorthodoxroast",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.4209, 56.203]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Upperlands Coffee Company",
      "description": "Upperlands Coffee Company is a small family business run by Julie and John Henderson. They can be found every Saturday in St Georges speciality food market in Belfast and on the first Sunday of every month (through the summer) at Farmleigh Farmers Market in Phoenix Park Dublin",
      "location": "12 East Bridge Street St, George's Market, Belfast BT7",
      "handle": "upperlands-coffee-company",
      "url": "http://www.upperlandscoffeecompany.com",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.9202, 54.5829]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 14, Chart House Business Park, Richmond Road, Fairview, Dublin 3, Ireland",
      "name": "Upside Coffee",
      "updated_at": "2020-06-28 01:03:12 UTC",
      "url": "https://www.upsidecoffee.com/",
      "twitter": "@upside_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-6.23, 53.365]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Urban Coffee Company",
      "url": "http://www.urbancoffee.co.uk",
      "location": "30 Church Street, Colmore Business District, Birmingham, West Midlands, B3 2NP",
      "profile_image_url": "pbs.twimg.com/profile_images/378800000581569996/5fcfa791f7a4e5775cf5683c1f79c9bc_400x400.png",
      "updated_at": "06-May-2015 15:41",
      "twitter": "@urbancoffeeco",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.9004, 52.4821]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Urban Roast Coffee Co",
      "description": "Midlands based Speciality Micro Roastery, offering fabulously roasted coffee direct to your door",
      "location": "West Midlands",
      "twitter": "@urban_roast",
      "handle": "urban-roast",
      "url": "http://urbanroastcoffee.co.uk",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8298, 52.4751]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Utopia coffee",
      "url": "http://utopiacoffee.co.uk",
      "location": "The Royals,  Southend-on-Sea, Essex, SS1 1DQ",
      "profile_image_url": "https://pbs.twimg.com/profile_images/3016352795/2518308d1cc0c3540937210a9697f1da_400x400.jpeg",
      "updated_at": "17-Jul-2018 13:56",
      "twitter": "@Gr8Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [0.7153, 51.5347]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Vagabond Coffee",
      "url": "https://vagabondcoffeeroasters.com/",
      "location": "London, N7",
      "profile_image_url": "pbs.twimg.com/profile_images/572380921949462528/uSg4fAq9_400x400.jpeg",
      "updated_at": "15-Apr-2016 14:33",
      "twitter": "@Vagabondcoffeer",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1206, 51.5544]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit D17, Ground Floor, Parkhall Trading Estate, 62 Tritton Road, London, SE21 8DE",
      "name": "Volcano Coffee Works",
      "updated_at": "2020-06-28 02:36:10 UTC",
      "url": "https://volcanocoffeeworks.com",
      "twitter": "@Volcano_Coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0941, 51.4326]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "W. Martyn",
      "url": "https://www.wmartyn.co.uk/",
      "location": "135 Muswell Hill Broadway,  London, N10 3RS",
      "profile_image_url": "www.wmartyn.co.uk/wp-content/uploads/2012/12/Logo2a-300x104.jpg",
      "updated_at": "06-May-2015 15:46",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1434, 51.5906]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 11, Crusader Industrial Estate, Hermitage Road, London, N4 1LZ",
      "name": "Weanie Beans",
      "updated_at": "2020-04-26 06:00:01 UTC",
      "url": "https://www.weaniebeans.com",
      "twitter": "@WeanieBeans",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0911, 51.5764]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 23 Eckland Lodge Business Park, Desborough Road, Market Harborough, Leicestershire, LE16 8HB",
      "name": "Well Roasted Coffee",
      "updated_at": "2020-06-28 00:07:19 UTC",
      "url": "https://www.wellroastedcoffee.com/",
      "twitter": "@well_roasted",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.8436, 52.4568]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Bournemouth, Dorset",
      "name": "Wellington Coffee",
      "updated_at": "2020-06-11 04:41:32 UTC",
      "url": "https://wellingtoncoffee.co.uk/",
      "twitter": "@WellingtonCoffe",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8808, 50.7192]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "6-8 Hall Street, Halifax, HX1 5AY",
      "name": "White Rose Coffee Roasters",
      "updated_at": "2020-05-21 08:58:45 UTC",
      "url": "https://whiterosecoffeeroasters.co.uk",
      "twitter": "@WRRoasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.8661, 53.723]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Wholey Bean",
      "url": "http://wholeybean.com",
      "location": "London",
      "profile_image_url": "pbs.twimg.com/profile_images/558060819838038016/4dh6jPjp_400x400.jpeg",
      "updated_at": "06-May-2015 15:58",
      "twitter": "@wholeybean",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1278, 51.5074]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Wilkinson's of Norwich",
      "url": "https://www.wilkinsonsofnorwich.com/",
      "location": "5 Lobster Lane, Norwich, Norfolk, NR2 1DQ",
      "profile_image_url": "cdn.shopify.com/s/files/1/0181/3537/files/wilkinsons-of-norwich.jpg",
      "updated_at": "06-May-2015 15:56",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [1.2932, 52.6298]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "17 Church Green Close, Kings Worthy, Winchester, Hampshire, SO23 7TT",
      "name": "Winchester Coffee",
      "updated_at": "2020-06-11 02:59:33 UTC",
      "url": "https://www.winchestercoffeeschool.co.uk/",
      "twitter": "@wincoffeeschool",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.2987, 51.0873]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Wogan Coffee",
      "url": "http://www.wogancoffee.co.uk",
      "location": "2 Clement Street, Bristol, BS2 9EQ",
      "profile_image_url": "https://wogancoffee.com/wp-content/uploads/2018/01/wogan-coffee-logo-4-2.jpg",
      "updated_at": "01-May-2019 08:18",
      "twitter": "@WoganCoffee",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.5808, 51.4606]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Ampthill, Bedfordshire",
      "name": "Wooden Hill Coffee",
      "updated_at": "2020-06-28 01:12:38 UTC",
      "url": "https://woodenhillcoffee.co.uk/",
      "twitter": "@WoodenHcoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.4951, 52.0273]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Workhouse Coffee &Co",
      "url": "http://workhousecoffee.co.uk",
      "location": "335 Oxford Rd, Reading, Berkshire, RG30 1AY",
      "profile_image_url": "workhousecoffee.co.uk/headerimg.png",
      "updated_at": "06-May-2015 15:37",
      "twitter": "@WorkhouseCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.9933, 51.4561]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Workshop Coffee Co.",
      "url": "https://workshopcoffee.com/",
      "location": "27 Clerkenwell Road, Clerkenwell, London, EC1M 5RN",
      "profile_image_url": "pbs.twimg.com/profile_images/438325872685109248/FR5ow5UD_400x400.jpeg",
      "updated_at": "06-May-2015 15:31",
      "twitter": "@WorkshopEC1",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.1026, 51.5223]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "World Coffees Ltd",
      "url": "http://worldcoffees.co.uk",
      "location": "The Old Forge,  Denmans Lane, Lindfield, West Sussex, RH16 2LB",
      "profile_image_url": "cdn.shopify.com/s/files/1/0240/2767/t/16/assets/logo.png",
      "updated_at": "06-May-2015 15:56",
      "marker-symbol": "danger",
      "marker-color": "#e32400",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-0.0821, 51.0127]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "ARGAL HOME FARM KERGILLIACK, Falmouth, Cornwall, TR11 5PD",
      "name": "YallahCoffee",
      "profile_image_url": "pbs.twimg.com/profile_images/2931178569/6a5bdd5e84ed2e6e415550c6d8f9140b_400x400.jpeg",
      "updated_at": "2019-07-04 08:10:50 UTC",
      "url": "https://yallahcoffee.co.uk/",
      "twitter": "@YallahCoffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-5.1266, 50.1532]
    }
  }, {
    "type": "Feature",
    "properties": {
      "location": "Unit 8, London Ebor Business Park, Millfield Lane, Nether Poppleton, York, YO26 6QY",
      "name": "York Coffee Emporium",
      "updated_at": "2019-12-23 16:18:54 UTC",
      "url": "https://yorkemporium.co.uk/",
      "twitter": "@york_coffee",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-1.1347, 53.9747]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Forth Coffee Roasters",
      "url": "https://www.forthcoffee.com",
      "location": "Forth Coffee Roasters, Unit 3-4 Flexspace, Harvest Road, Newbridge, EH28 8LW, Scotland",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/1747/9553/files/Front_Main_logo_130x@2x.png",
      "updated_at": "09-Mar-2016 16:10",
      "twitter": "@ForthRoasters",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.3998, 55.9352]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Zen Coffee Roasters",
      "description": "We source our green coffee through the most respected merchants in the trade whose ethos is to ensure a fair return for the grower, that coffee is produced in a sustainable way and where workers are properly compensated. We use high quality, traceable beans sourced in small lots, primarily from South America and East Africa, each batch being carefully selected to display the characteristics of the region. These are then hand roasted at our premises. The Zen ethos is to help people step aside the hurly burly of modern life and allow themselves a moment to connect with their own energy. Coffee doesn\u2019t just stimulate the mind and tastebuds, its an antioxidant too. So in small amounts its good for both your mind and your health. More than that it provides a simple excuse to relax, be that be at the end of a meal or as a brief interlude, either alone or in company. So please make the most of Zen and in so doing we hope to help you make a small step in your journey to make the most of you!",
      "location": "Mile Oak Industrial Estate, Maesbury Rd, Oswestry, SY10 8GA",
      "handle": "zen-coffee-roasters",
      "url": "https://www.zencoffee.co.uk",
      "marker-symbol": "danger",
      "marker-color": "#ff8647",
      "status": "unknown"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-3.0416, 52.8437]
    }
  }, {
    "type": "Feature",
    "properties": {
      "name": "Zombie Coffee Co & Roastery",
      "url": "http://zombiecoffeeco.co.uk",
      "location": "Clitheroe, Lankshire, BB7",
      "profile_image_url": "https://cdn.shopify.com/s/files/1/0181/3537/files/zombie-coffee-logo.jpg",
      "updated_at": "16-Jul-2018 08:44",
      "marker-symbol": "cafe"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [-2.3931, 53.8711]
    }
  }]
}
```
