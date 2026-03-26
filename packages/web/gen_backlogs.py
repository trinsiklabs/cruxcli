#!/usr/bin/env python3
"""Generate levnation and levciti content backlogs."""

import json
from datetime import datetime, timezone

# ============================================================
# DATA: Cities
# ============================================================

# Top 100 US cities by population (p0)
TOP_100_US_CITIES = [
    ("new-york", "New York", "NY"), ("los-angeles", "Los Angeles", "CA"),
    ("chicago", "Chicago", "IL"), ("houston", "Houston", "TX"),
    ("phoenix", "Phoenix", "AZ"), ("philadelphia", "Philadelphia", "PA"),
    ("san-antonio", "San Antonio", "TX"), ("san-diego", "San Diego", "CA"),
    ("dallas", "Dallas", "TX"), ("jacksonville", "Jacksonville", "FL"),
    ("san-jose", "San Jose", "CA"), ("austin", "Austin", "TX"),
    ("fort-worth", "Fort Worth", "TX"), ("columbus", "Columbus", "OH"),
    ("charlotte", "Charlotte", "NC"), ("indianapolis", "Indianapolis", "IN"),
    ("san-francisco", "San Francisco", "CA"), ("seattle", "Seattle", "WA"),
    ("denver", "Denver", "CO"), ("washington-dc", "Washington", "DC"),
    ("nashville", "Nashville", "TN"), ("oklahoma-city", "Oklahoma City", "OK"),
    ("el-paso", "El Paso", "TX"), ("boston", "Boston", "MA"),
    ("portland-oregon", "Portland", "OR"), ("las-vegas", "Las Vegas", "NV"),
    ("memphis", "Memphis", "TN"), ("louisville", "Louisville", "KY"),
    ("baltimore", "Baltimore", "MD"), ("milwaukee", "Milwaukee", "WI"),
    ("albuquerque", "Albuquerque", "NM"), ("tucson", "Tucson", "AZ"),
    ("fresno", "Fresno", "CA"), ("mesa", "Mesa", "AZ"),
    ("sacramento", "Sacramento", "CA"), ("atlanta", "Atlanta", "GA"),
    ("kansas-city-missouri", "Kansas City", "MO"), ("colorado-springs", "Colorado Springs", "CO"),
    ("omaha", "Omaha", "NE"), ("raleigh", "Raleigh", "NC"),
    ("long-beach", "Long Beach", "CA"), ("virginia-beach", "Virginia Beach", "VA"),
    ("miami", "Miami", "FL"), ("oakland", "Oakland", "CA"),
    ("minneapolis", "Minneapolis", "MN"), ("tampa", "Tampa", "FL"),
    ("tulsa", "Tulsa", "OK"), ("arlington-texas", "Arlington", "TX"),
    ("new-orleans", "New Orleans", "LA"), ("wichita", "Wichita", "KS"),
    ("cleveland", "Cleveland", "OH"), ("bakersfield", "Bakersfield", "CA"),
    ("aurora-colorado", "Aurora", "CO"), ("anaheim", "Anaheim", "CA"),
    ("honolulu", "Honolulu", "HI"), ("santa-ana", "Santa Ana", "CA"),
    ("riverside", "Riverside", "CA"), ("corpus-christi", "Corpus Christi", "TX"),
    ("lexington", "Lexington", "KY"), ("stockton", "Stockton", "CA"),
    ("st-paul", "St. Paul", "MN"), ("henderson", "Henderson", "NV"),
    ("pittsburgh", "Pittsburgh", "PA"), ("cincinnati", "Cincinnati", "OH"),
    ("greensboro", "Greensboro", "NC"), ("anchorage", "Anchorage", "AK"),
    ("plano", "Plano", "TX"), ("lincoln", "Lincoln", "NE"),
    ("orlando", "Orlando", "FL"), ("irvine", "Irvine", "CA"),
    ("newark", "Newark", "NJ"), ("durham", "Durham", "NC"),
    ("chula-vista", "Chula Vista", "CA"), ("toledo", "Toledo", "OH"),
    ("fort-wayne", "Fort Wayne", "IN"), ("st-petersburg", "St. Petersburg", "FL"),
    ("laredo", "Laredo", "TX"), ("jersey-city", "Jersey City", "NJ"),
    ("chandler", "Chandler", "AZ"), ("madison", "Madison", "WI"),
    ("lubbock", "Lubbock", "TX"), ("scottsdale", "Scottsdale", "AZ"),
    ("reno", "Reno", "NV"), ("buffalo", "Buffalo", "NY"),
    ("gilbert", "Gilbert", "AZ"), ("glendale-arizona", "Glendale", "AZ"),
    ("north-las-vegas", "North Las Vegas", "NV"), ("winston-salem", "Winston-Salem", "NC"),
    ("chesapeake", "Chesapeake", "VA"), ("norfolk", "Norfolk", "VA"),
    ("fremont", "Fremont", "CA"), ("garland", "Garland", "TX"),
    ("irving", "Irving", "TX"), ("hialeah", "Hialeah", "FL"),
    ("richmond", "Richmond", "VA"), ("boise", "Boise", "ID"),
    ("spokane", "Spokane", "WA"), ("baton-rouge", "Baton Rouge", "LA"),
    ("tacoma", "Tacoma", "WA"), ("san-bernardino", "San Bernardino", "CA"),
    ("modesto", "Modesto", "CA"), ("des-moines", "Des Moines", "IA"),
]

# US cities 100K-300K population range (p2) — ~300 more cities
US_CITIES_OVER_100K = [
    ("fontana", "Fontana", "CA"), ("moreno-valley", "Moreno Valley", "CA"),
    ("fayetteville", "Fayetteville", "NC"), ("glendale-california", "Glendale", "CA"),
    ("yonkers", "Yonkers", "NY"), ("huntington-beach", "Huntington Beach", "CA"),
    ("salt-lake-city", "Salt Lake City", "UT"), ("grand-rapids", "Grand Rapids", "MI"),
    ("tallahassee", "Tallahassee", "FL"), ("oxnard", "Oxnard", "CA"),
    ("birmingham", "Birmingham", "AL"), ("rochester-ny", "Rochester", "NY"),
    ("sioux-falls", "Sioux Falls", "SD"), ("port-st-lucie", "Port St. Lucie", "FL"),
    ("frisco", "Frisco", "TX"), ("cape-coral", "Cape Coral", "FL"),
    ("amarillo", "Amarillo", "TX"), ("peoria-arizona", "Peoria", "AZ"),
    ("overland-park", "Overland Park", "KS"), ("knoxville", "Knoxville", "TN"),
    ("tempe", "Tempe", "AZ"), ("brownsville", "Brownsville", "TX"),
    ("mckinney", "McKinney", "TX"), ("pompano-beach", "Pompano Beach", "FL"),
    ("ontario-california", "Ontario", "CA"), ("columbia-south-carolina", "Columbia", "SC"),
    ("providence", "Providence", "RI"), ("clarksville", "Clarksville", "TN"),
    ("elk-grove", "Elk Grove", "CA"), ("eugene", "Eugene", "OR"),
    ("salem-oregon", "Salem", "OR"), ("cary", "Cary", "NC"),
    ("palm-bay", "Palm Bay", "FL"), ("dayton", "Dayton", "OH"),
    ("garden-grove", "Garden Grove", "CA"), ("killeen", "Killeen", "TX"),
    ("springfield-missouri", "Springfield", "MO"), ("hampton", "Hampton", "VA"),
    ("lakewood-colorado", "Lakewood", "CO"), ("vancouver-washington", "Vancouver", "WA"),
    ("paterson", "Paterson", "NJ"), ("alexandria", "Alexandria", "VA"),
    ("roseville", "Roseville", "CA"), ("hayward", "Hayward", "CA"),
    ("surprise", "Surprise", "AZ"), ("macon", "Macon", "GA"),
    ("kansas-city-kansas", "Kansas City", "KS"), ("sunnyvale", "Sunnyvale", "CA"),
    ("springfield-illinois", "Springfield", "IL"), ("pomona", "Pomona", "CA"),
    ("rancho-cucamonga", "Rancho Cucamonga", "CA"), ("santa-clarita", "Santa Clarita", "CA"),
    ("chattanooga", "Chattanooga", "TN"), ("bellevue", "Bellevue", "WA"),
    ("torrance", "Torrance", "CA"), ("bridgeport", "Bridgeport", "CT"),
    ("savannah", "Savannah", "GA"), ("joliet", "Joliet", "IL"),
    ("naperville", "Naperville", "IL"), ("pasadena-texas", "Pasadena", "TX"),
    ("syracuse", "Syracuse", "NY"), ("mcallen", "McAllen", "TX"),
    ("mesquite", "Mesquite", "TX"), ("midland", "Midland", "TX"),
    ("palmdale", "Palmdale", "CA"), ("murfreesboro", "Murfreesboro", "TN"),
    ("rockford", "Rockford", "IL"), ("columbia-missouri", "Columbia", "MO"),
    ("olathe", "Olathe", "KS"), ("denton", "Denton", "TX"),
    ("thornton", "Thornton", "CO"), ("fullerton", "Fullerton", "CA"),
    ("gainesville", "Gainesville", "FL"), ("waco", "Waco", "TX"),
    ("west-valley-city", "West Valley City", "UT"), ("warren", "Warren", "MI"),
    ("orange", "Orange", "CA"), ("west-jordan", "West Jordan", "UT"),
    ("clearwater", "Clearwater", "FL"), ("manchester", "Manchester", "NH"),
    ("west-palm-beach", "West Palm Beach", "FL"), ("costa-mesa", "Costa Mesa", "CA"),
    ("round-rock", "Round Rock", "TX"), ("pueblo", "Pueblo", "CO"),
    ("elgin", "Elgin", "IL"), ("carlsbad", "Carlsbad", "CA"),
    ("lowell", "Lowell", "MA"), ("wilmington", "Wilmington", "NC"),
    ("berkeley", "Berkeley", "CA"), ("concord", "Concord", "CA"),
    ("centennial", "Centennial", "CO"), ("davie", "Davie", "FL"),
    ("murrieta", "Murrieta", "CA"), ("lewisville", "Lewisville", "TX"),
    ("high-point", "High Point", "NC"), ("antioch", "Antioch", "CA"),
    ("richardson", "Richardson", "TX"), ("pearland", "Pearland", "TX"),
    ("temecula", "Temecula", "CA"), ("erie", "Erie", "PA"),
    ("hartford", "Hartford", "CT"), ("new-haven", "New Haven", "CT"),
    ("college-station", "College Station", "TX"), ("south-bend", "South Bend", "IN"),
    ("sterling-heights", "Sterling Heights", "MI"), ("carrollton", "Carrollton", "TX"),
    ("coral-springs", "Coral Springs", "FL"), ("miramar", "Miramar", "FL"),
    ("norman", "Norman", "OK"), ("lee-summit", "Lee's Summit", "MO"),
    ("sandy-springs", "Sandy Springs", "GA"), ("beaumont", "Beaumont", "TX"),
    ("allen", "Allen", "TX"), ("green-bay", "Green Bay", "WI"),
    ("abilene", "Abilene", "TX"), ("las-cruces", "Las Cruces", "NM"),
    ("evansville", "Evansville", "IN"), ("tyler", "Tyler", "TX"),
    ("west-covina", "West Covina", "CA"), ("sparks", "Sparks", "NV"),
    ("broken-arrow", "Broken Arrow", "OK"), ("lakeland", "Lakeland", "FL"),
    ("hillsboro", "Hillsboro", "OR"), ("arvada", "Arvada", "CO"),
    ("inglewood", "Inglewood", "CA"), ("downey", "Downey", "CA"),
    ("waterbury", "Waterbury", "CT"), ("elgin-texas", "Elgin", "TX"),
    ("san-mateo", "San Mateo", "CA"), ("edmond", "Edmond", "OK"),
    ("longmont", "Longmont", "CO"), ("westminster-colorado", "Westminster", "CO"),
    ("burbank", "Burbank", "CA"), ("norwalk", "Norwalk", "CA"),
    ("south-gate", "South Gate", "CA"), ("boulder", "Boulder", "CO"),
    ("goodyear", "Goodyear", "AZ"), ("buckeye", "Buckeye", "AZ"),
    ("jurupa-valley", "Jurupa Valley", "CA"), ("lake-charles", "Lake Charles", "LA"),
    ("daly-city", "Daly City", "CA"), ("kennewick", "Kennewick", "WA"),
    ("league-city", "League City", "TX"), ("lawton", "Lawton", "OK"),
    ("davenport", "Davenport", "IA"), ("pflugerville", "Pflugerville", "TX"),
    ("tuscaloosa", "Tuscaloosa", "AL"), ("north-charleston", "North Charleston", "SC"),
    ("san-leandro", "San Leandro", "CA"), ("davie", "Davie", "FL"),
    ("cedar-rapids", "Cedar Rapids", "IA"), ("greenville-sc", "Greenville", "SC"),
    ("fishers", "Fishers", "IN"), ("napa", "Napa", "CA"),
    ("new-braunfels", "New Braunfels", "TX"), ("flower-mound", "Flower Mound", "TX"),
    ("plantation", "Plantation", "FL"), ("compton", "Compton", "CA"),
    ("racine", "Racine", "WI"), ("menifee", "Menifee", "CA"),
    ("canton", "Canton", "OH"), ("baytown", "Baytown", "TX"),
    ("mission", "Mission", "TX"), ("pharr", "Pharr", "TX"),
    ("columbia-maryland", "Columbia", "MD"), ("st-george", "St. George", "UT"),
    ("nampa", "Nampa", "ID"), ("bend", "Bend", "OR"),
    ("redding", "Redding", "CA"), ("hemet", "Hemet", "CA"),
    ("perris", "Perris", "CA"), ("suffolk", "Suffolk", "VA"),
    ("yuma", "Yuma", "AZ"), ("pine-bluff", "Pine Bluff", "AR"),
    ("kettering", "Kettering", "OH"), ("san-marcos-texas", "San Marcos", "TX"),
    ("conroe", "Conroe", "TX"), ("plantation", "Plantation", "FL"),
    ("tracy", "Tracy", "CA"), ("livermore", "Livermore", "CA"),
    ("eagan", "Eagan", "MN"), ("eden-prairie", "Eden Prairie", "MN"),
    ("blaine", "Blaine", "MN"), ("woodbury", "Woodbury", "MN"),
    ("lakeville", "Lakeville", "MN"), ("maple-grove", "Maple Grove", "MN"),
    ("st-cloud", "St. Cloud", "MN"), ("duluth", "Duluth", "MN"),
    ("rochester-mn", "Rochester", "MN"), ("moorhead", "Moorhead", "MN"),
    ("springfield-massachusetts", "Springfield", "MA"), ("worcester", "Worcester", "MA"),
    ("cambridge", "Cambridge", "MA"), ("brockton", "Brockton", "MA"),
    ("fall-river", "Fall River", "MA"), ("new-bedford", "New Bedford", "MA"),
    ("lynn", "Lynn", "MA"), ("quincy", "Quincy", "MA"),
    ("lawrence", "Lawrence", "MA"), ("somerville", "Somerville", "MA"),
    ("jackson-mississippi", "Jackson", "MS"), ("gulfport", "Gulfport", "MS"),
    ("biloxi", "Biloxi", "MS"), ("hattiesburg", "Hattiesburg", "MS"),
    ("missoula", "Missoula", "MT"), ("billings", "Billings", "MT"),
    ("great-falls", "Great Falls", "MT"), ("fargo", "Fargo", "ND"),
    ("bismarck", "Bismarck", "ND"), ("grand-forks", "Grand Forks", "ND"),
    ("charleston-wv", "Charleston", "WV"), ("huntington", "Huntington", "WV"),
    ("parkersburg", "Parkersburg", "WV"), ("cheyenne", "Cheyenne", "WY"),
    ("casper", "Casper", "WY"), ("charleston-sc", "Charleston", "SC"),
    ("athens-georgia", "Athens", "GA"), ("sandy", "Sandy", "UT"),
    ("orem", "Orem", "UT"), ("provo", "Provo", "UT"),
    ("ogden", "Ogden", "UT"), ("st-george", "St. George", "UT"),
    ("albany-ny", "Albany", "NY"), ("schenectady", "Schenectady", "NY"),
    ("utica", "Utica", "NY"), ("binghamton", "Binghamton", "NY"),
    ("new-rochelle", "New Rochelle", "NY"), ("mount-vernon-ny", "Mount Vernon", "NY"),
    ("white-plains", "White Plains", "NY"), ("hempstead", "Hempstead", "NY"),
    ("trenton", "Trenton", "NJ"), ("camden", "Camden", "NJ"),
    ("passaic", "Passaic", "NJ"), ("elizabeth", "Elizabeth", "NJ"),
    ("clifton", "Clifton", "NJ"), ("east-orange", "East Orange", "NJ"),
    ("bayonne", "Bayonne", "NJ"), ("union-city-nj", "Union City", "NJ"),
    ("hoboken", "Hoboken", "NJ"), ("west-new-york", "West New York", "NJ"),
    ("vineland", "Vineland", "NJ"), ("dover", "Dover", "DE"),
    ("little-rock", "Little Rock", "AR"), ("fort-smith", "Fort Smith", "AR"),
    ("fayetteville-ar", "Fayetteville", "AR"), ("springdale", "Springdale", "AR"),
    ("jonesboro", "Jonesboro", "AR"), ("north-little-rock", "North Little Rock", "AR"),
    ("conway", "Conway", "AR"), ("rogers", "Rogers", "AR"),
    ("bentonville", "Bentonville", "AR"), ("hot-springs", "Hot Springs", "AR"),
]

# US State capitals (many already in top 100 or 100K+, but ensure all present)
US_STATE_CAPITALS = [
    ("montgomery", "Montgomery", "AL"), ("juneau", "Juneau", "AK"),
    ("phoenix", "Phoenix", "AZ"), ("little-rock", "Little Rock", "AR"),
    ("sacramento", "Sacramento", "CA"), ("denver", "Denver", "CO"),
    ("hartford", "Hartford", "CT"), ("dover", "Dover", "DE"),
    ("tallahassee", "Tallahassee", "FL"), ("atlanta", "Atlanta", "GA"),
    ("honolulu", "Honolulu", "HI"), ("boise", "Boise", "ID"),
    ("springfield-illinois", "Springfield", "IL"), ("indianapolis", "Indianapolis", "IN"),
    ("des-moines", "Des Moines", "IA"), ("topeka", "Topeka", "KS"),
    ("frankfort", "Frankfort", "KY"), ("baton-rouge", "Baton Rouge", "LA"),
    ("augusta", "Augusta", "ME"), ("annapolis", "Annapolis", "MD"),
    ("boston", "Boston", "MA"), ("lansing", "Lansing", "MI"),
    ("st-paul", "St. Paul", "MN"), ("jackson-mississippi", "Jackson", "MS"),
    ("jefferson-city", "Jefferson City", "MO"), ("helena", "Helena", "MT"),
    ("lincoln", "Lincoln", "NE"), ("carson-city", "Carson City", "NV"),
    ("concord-nh", "Concord", "NH"), ("trenton", "Trenton", "NJ"),
    ("santa-fe", "Santa Fe", "NM"), ("albany-ny", "Albany", "NY"),
    ("raleigh", "Raleigh", "NC"), ("bismarck", "Bismarck", "ND"),
    ("columbus", "Columbus", "OH"), ("oklahoma-city", "Oklahoma City", "OK"),
    ("salem-oregon", "Salem", "OR"), ("harrisburg", "Harrisburg", "PA"),
    ("providence", "Providence", "RI"), ("columbia-south-carolina", "Columbia", "SC"),
    ("pierre", "Pierre", "SD"), ("nashville", "Nashville", "TN"),
    ("austin", "Austin", "TX"), ("salt-lake-city", "Salt Lake City", "UT"),
    ("montpelier", "Montpelier", "VT"), ("richmond", "Richmond", "VA"),
    ("olympia", "Olympia", "WA"), ("charleston-wv", "Charleston", "WV"),
    ("madison", "Madison", "WI"), ("cheyenne", "Cheyenne", "WY"),
]

# National capitals (p1)
NATIONAL_CAPITALS = [
    ("london-uk", "London", "UK"), ("ottawa", "Ottawa", "Canada"),
    ("canberra", "Canberra", "Australia"), ("berlin", "Berlin", "Germany"),
    ("paris", "Paris", "France"), ("brasilia", "Brasília", "Brazil"),
    ("new-delhi", "New Delhi", "India"), ("tokyo", "Tokyo", "Japan"),
    ("beijing", "Beijing", "China"), ("moscow", "Moscow", "Russia"),
    ("seoul", "Seoul", "South Korea"), ("mexico-city", "Mexico City", "Mexico"),
    ("buenos-aires", "Buenos Aires", "Argentina"), ("bogota", "Bogotá", "Colombia"),
    ("lima", "Lima", "Peru"), ("santiago", "Santiago", "Chile"),
    ("cairo", "Cairo", "Egypt"), ("nairobi", "Nairobi", "Kenya"),
    ("pretoria", "Pretoria", "South Africa"), ("abuja", "Abuja", "Nigeria"),
    ("accra", "Accra", "Ghana"), ("addis-ababa", "Addis Ababa", "Ethiopia"),
    ("rome", "Rome", "Italy"), ("madrid", "Madrid", "Spain"),
    ("lisbon", "Lisbon", "Portugal"), ("amsterdam", "Amsterdam", "Netherlands"),
    ("brussels", "Brussels", "Belgium"), ("vienna", "Vienna", "Austria"),
    ("bern", "Bern", "Switzerland"), ("stockholm", "Stockholm", "Sweden"),
    ("oslo", "Oslo", "Norway"), ("copenhagen", "Copenhagen", "Denmark"),
    ("helsinki", "Helsinki", "Finland"), ("dublin", "Dublin", "Ireland"),
    ("athens-greece", "Athens", "Greece"), ("warsaw", "Warsaw", "Poland"),
    ("prague", "Prague", "Czech Republic"), ("budapest", "Budapest", "Hungary"),
    ("bucharest", "Bucharest", "Romania"), ("kyiv", "Kyiv", "Ukraine"),
    ("ankara", "Ankara", "Turkey"), ("riyadh", "Riyadh", "Saudi Arabia"),
    ("tehran", "Tehran", "Iran"), ("baghdad", "Baghdad", "Iraq"),
    ("islamabad", "Islamabad", "Pakistan"), ("dhaka", "Dhaka", "Bangladesh"),
    ("bangkok", "Bangkok", "Thailand"), ("hanoi", "Hanoi", "Vietnam"),
    ("jakarta", "Jakarta", "Indonesia"), ("manila", "Manila", "Philippines"),
    ("kuala-lumpur", "Kuala Lumpur", "Malaysia"), ("singapore", "Singapore", "Singapore"),
    ("taipei", "Taipei", "Taiwan"), ("pyongyang", "Pyongyang", "North Korea"),
    ("ulaanbaatar", "Ulaanbaatar", "Mongolia"), ("kabul", "Kabul", "Afghanistan"),
    ("kathmandu", "Kathmandu", "Nepal"), ("colombo", "Colombo", "Sri Lanka"),
    ("rabat", "Rabat", "Morocco"), ("tunis", "Tunis", "Tunisia"),
    ("algiers", "Algiers", "Algeria"), ("tripoli", "Tripoli", "Libya"),
    ("khartoum", "Khartoum", "Sudan"), ("kinshasa", "Kinshasa", "DR Congo"),
    ("dar-es-salaam", "Dar es Salaam", "Tanzania"), ("kampala", "Kampala", "Uganda"),
    ("maputo", "Maputo", "Mozambique"), ("lusaka", "Lusaka", "Zambia"),
    ("harare", "Harare", "Zimbabwe"), ("antananarivo", "Antananarivo", "Madagascar"),
    ("dakar", "Dakar", "Senegal"), ("bamako", "Bamako", "Mali"),
    ("ouagadougou", "Ouagadougou", "Burkina Faso"), ("niamey", "Niamey", "Niger"),
    ("ndjamena", "N'Djamena", "Chad"), ("bangui", "Bangui", "Central African Republic"),
    ("yaounde", "Yaoundé", "Cameroon"), ("libreville", "Libreville", "Gabon"),
    ("brazzaville", "Brazzaville", "Congo"), ("luanda", "Luanda", "Angola"),
    ("windhoek", "Windhoek", "Namibia"), ("gaborone", "Gaborone", "Botswana"),
    ("maseru", "Maseru", "Lesotho"), ("mbabane", "Mbabane", "Eswatini"),
    ("mogadishu", "Mogadishu", "Somalia"), ("djibouti-city", "Djibouti", "Djibouti"),
    ("asmara", "Asmara", "Eritrea"), ("juba", "Juba", "South Sudan"),
    ("belmopan", "Belmopan", "Belize"), ("guatemala-city", "Guatemala City", "Guatemala"),
    ("san-salvador", "San Salvador", "El Salvador"), ("tegucigalpa", "Tegucigalpa", "Honduras"),
    ("managua", "Managua", "Nicaragua"), ("san-jose-costa-rica", "San José", "Costa Rica"),
    ("panama-city", "Panama City", "Panama"), ("havana", "Havana", "Cuba"),
    ("kingston", "Kingston", "Jamaica"), ("port-au-prince", "Port-au-Prince", "Haiti"),
    ("santo-domingo", "Santo Domingo", "Dominican Republic"),
    ("port-of-spain", "Port of Spain", "Trinidad and Tobago"),
    ("nassau", "Nassau", "Bahamas"), ("bridgetown", "Bridgetown", "Barbados"),
    ("georgetown-guyana", "Georgetown", "Guyana"), ("paramaribo", "Paramaribo", "Suriname"),
    ("quito", "Quito", "Ecuador"), ("la-paz", "La Paz", "Bolivia"),
    ("asuncion", "Asunción", "Paraguay"), ("montevideo", "Montevideo", "Uruguay"),
    ("caracas", "Caracas", "Venezuela"), ("suva", "Suva", "Fiji"),
    ("wellington", "Wellington", "New Zealand"), ("port-moresby", "Port Moresby", "Papua New Guinea"),
    ("reykjavik", "Reykjavík", "Iceland"), ("tallinn", "Tallinn", "Estonia"),
    ("riga", "Riga", "Latvia"), ("vilnius", "Vilnius", "Lithuania"),
    ("minsk", "Minsk", "Belarus"), ("chisinau", "Chișinău", "Moldova"),
    ("tbilisi", "Tbilisi", "Georgia"), ("yerevan", "Yerevan", "Armenia"),
    ("baku", "Baku", "Azerbaijan"), ("tashkent", "Tashkent", "Uzbekistan"),
    ("astana", "Astana", "Kazakhstan"), ("bishkek", "Bishkek", "Kyrgyzstan"),
    ("dushanbe", "Dushanbe", "Tajikistan"), ("ashgabat", "Ashgabat", "Turkmenistan"),
    ("skopje", "Skopje", "North Macedonia"), ("tirana", "Tirana", "Albania"),
    ("podgorica", "Podgorica", "Montenegro"), ("belgrade", "Belgrade", "Serbia"),
    ("sarajevo", "Sarajevo", "Bosnia and Herzegovina"), ("zagreb", "Zagreb", "Croatia"),
    ("ljubljana", "Ljubljana", "Slovenia"), ("bratislava", "Bratislava", "Slovakia"),
    ("nicosia", "Nicosia", "Cyprus"), ("valletta", "Valletta", "Malta"),
    ("luxembourg-city", "Luxembourg City", "Luxembourg"),
    ("vaduz", "Vaduz", "Liechtenstein"), ("san-marino", "San Marino", "San Marino"),
    ("andorra-la-vella", "Andorra la Vella", "Andorra"), ("monaco", "Monaco", "Monaco"),
]

# Tier 1 international cities (top 50 per country) — p1
UK_TOP_50 = [
    "london", "birmingham-uk", "manchester", "glasgow", "liverpool",
    "leeds", "sheffield", "edinburgh", "bristol", "cardiff",
    "leicester", "coventry", "nottingham", "newcastle", "sunderland",
    "brighton", "hull", "plymouth", "stoke-on-trent", "wolverhampton",
    "derby", "swansea", "southampton", "reading-uk", "aberdeen",
    "dundee", "oxford", "cambridge-uk", "york", "bath",
    "exeter", "norwich", "portsmouth", "lancaster", "gloucester",
    "chester", "salisbury", "winchester", "canterbury", "peterborough",
    "worcester-uk", "preston", "blackpool", "luton", "middlesbrough",
    "bradford", "belfast", "derry", "inverness", "stirling",
]

CANADA_TOP_50 = [
    "toronto", "montreal", "vancouver-bc", "calgary", "edmonton",
    "ottawa-canada", "winnipeg", "quebec-city", "hamilton-ontario", "kitchener",
    "london-ontario", "victoria-bc", "halifax", "oshawa", "windsor-ontario",
    "saskatoon", "regina", "st-johns", "barrie", "kelowna",
    "abbotsford", "guelph", "kingston-ontario", "thunder-bay", "moncton",
    "brantford", "red-deer", "lethbridge", "kamloops", "nanaimo",
    "fredericton", "charlottetown", "saint-john-nb", "sudbury", "sault-ste-marie",
    "north-bay", "chatham-kent", "belleville", "sarnia", "medicine-hat",
    "prince-george", "peterborough-ontario", "woodstock-ontario", "brockville", "cornwall-ontario",
    "moose-jaw", "prince-albert", "swift-current", "brandon", "whitehorse",
]

AUSTRALIA_TOP_50 = [
    "sydney", "melbourne-australia", "brisbane", "perth-australia", "adelaide",
    "gold-coast", "canberra-city", "newcastle-australia", "wollongong", "sunshine-coast",
    "hobart", "geelong", "townsville", "cairns", "darwin-australia",
    "toowoomba", "ballarat", "bendigo", "launceston", "mackay",
    "rockhampton", "bunbury", "bundaberg", "hervey-bay", "wagga-wagga",
    "coffs-harbour", "gladstone", "mildura", "shepparton", "tamworth",
    "port-macquarie", "orange-australia", "dubbo", "albury", "bathurst-australia",
    "geraldton", "kalgoorlie", "devonport", "burnie", "alice-springs",
    "mount-gambier", "warrnambool", "lismore", "grafton", "armidale",
    "broome", "karratha", "port-hedland", "mount-isa", "emerald",
]

GERMANY_TOP_50 = [
    "berlin-city", "hamburg", "munich", "cologne", "frankfurt",
    "stuttgart", "dusseldorf", "leipzig", "dortmund", "essen",
    "bremen", "dresden", "hanover", "nuremberg", "duisburg",
    "bochum", "wuppertal", "bielefeld", "bonn", "munster",
    "mannheim", "karlsruhe", "augsburg", "wiesbaden", "gelsenkirchen",
    "aachen", "monchengladbach", "braunschweig", "kiel", "chemnitz",
    "krefeld", "halle", "magdeburg", "freiburg", "oberhausen",
    "lubeck", "erfurt", "rostock", "mainz", "kassel",
    "hagen", "potsdam", "saarbrucken", "hamm", "ludwigshafen",
    "oldenburg", "mulheim", "osnabrück", "leverkusen", "heidelberg",
]

FRANCE_TOP_50 = [
    "paris-city", "marseille", "lyon", "toulouse", "nice",
    "nantes", "montpellier", "strasbourg", "bordeaux", "lille",
    "rennes", "reims", "saint-etienne", "toulon", "le-havre",
    "grenoble", "dijon", "angers", "nimes", "saint-denis",
    "villeurbanne", "clermont-ferrand", "le-mans", "aix-en-provence", "brest",
    "tours", "amiens", "limoges", "perpignan", "metz",
    "besancon", "orleans", "rouen", "mulhouse", "caen",
    "nancy", "argenteuil", "saint-paul-reunion", "montreuil", "roubaix",
    "tourcoing", "avignon", "dunkirk", "poitiers", "pau",
    "calais", "la-rochelle", "cannes", "antibes", "colmar",
]

BRAZIL_TOP_50 = [
    "sao-paulo", "rio-de-janeiro", "brasilia-city", "salvador", "fortaleza",
    "belo-horizonte", "manaus", "curitiba", "recife", "goiania",
    "belem", "porto-alegre", "guarulhos", "campinas", "sao-luis",
    "sao-goncalo", "maceio", "duque-de-caxias", "natal", "campo-grande",
    "teresina", "sao-bernardo-do-campo", "joao-pessoa", "santo-andre", "osasco",
    "sao-jose-dos-campos", "jaboatao-dos-guararapes", "ribeirao-preto", "uberlandia", "sorocaba",
    "contagem", "aracaju", "feira-de-santana", "cuiaba", "joinville",
    "juiz-de-fora", "londrina", "aparecida-de-goiania", "niteroi", "ananindeua",
    "porto-velho", "serra", "belford-roxo", "campos-dos-goytacazes", "caxias-do-sul",
    "sao-jose-do-rio-preto", "macapa", "florianopolis", "santos", "vila-velha",
]

INDIA_TOP_50 = [
    "mumbai", "delhi", "bangalore", "hyderabad", "ahmedabad",
    "chennai", "kolkata", "pune", "jaipur", "lucknow",
    "kanpur", "nagpur", "visakhapatnam", "indore", "thane",
    "bhopal", "patna", "vadodara", "ghaziabad", "ludhiana",
    "agra", "nashik", "faridabad", "meerut", "rajkot",
    "varanasi", "srinagar", "aurangabad", "dhanbad", "amritsar",
    "allahabad", "ranchi", "howrah", "coimbatore", "jabalpur",
    "gwalior", "vijayawada", "jodhpur", "madurai", "raipur",
    "kota", "chandigarh", "guwahati", "solapur", "hubli-dharwad",
    "mysore", "tiruchirappalli", "bareilly", "aligarh", "moradabad",
]

JAPAN_TOP_50 = [
    "tokyo-city", "yokohama", "osaka", "nagoya", "sapporo",
    "fukuoka", "kobe", "kawasaki", "kyoto", "saitama",
    "hiroshima", "sendai", "chiba", "kitakyushu", "sakai",
    "niigata", "hamamatsu", "kumamoto", "sagamihara", "shizuoka",
    "okayama", "kagoshima", "funabashi", "hachioji", "kawaguchi",
    "himeji", "matsuyama", "higashiosaka", "utsunomiya", "matsudo",
    "nishinomiya", "ichikawa", "kurashiki", "amagasaki", "oita",
    "kanazawa", "nagasaki", "yokosuka", "toyama", "toyota",
    "gifu", "takatsuki", "iwaki", "nagano", "toyonaka",
    "wakayama", "nara", "takasaki", "asahikawa", "koriyama",
]

# ============================================================
# DATA: Politicians
# ============================================================

# US Congress — we'll generate all 535 members
# Senate: 100 members (2 per state)
US_STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
]

US_STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
}

# House districts per state (based on 2020 census)
HOUSE_DISTRICTS = {
    "AL": 7, "AK": 1, "AZ": 9, "AR": 4, "CA": 52, "CO": 8, "CT": 5,
    "DE": 1, "FL": 28, "GA": 14, "HI": 2, "ID": 2, "IL": 17, "IN": 9,
    "IA": 4, "KS": 4, "KY": 6, "LA": 6, "ME": 2, "MD": 8, "MA": 9,
    "MI": 13, "MN": 8, "MS": 4, "MO": 8, "MT": 2, "NE": 3, "NV": 4,
    "NH": 2, "NJ": 12, "NM": 3, "NY": 26, "NC": 14, "ND": 1, "OH": 15,
    "OK": 5, "OR": 6, "PA": 17, "RI": 2, "SC": 7, "SD": 1, "TN": 9,
    "TX": 38, "UT": 4, "VT": 1, "VA": 11, "WA": 10, "WV": 2, "WI": 8,
    "WY": 1,
}

# State legislature sizes
STATE_LEGISLATURE_SIZES = {
    "AL": (35, 105), "AK": (20, 40), "AZ": (30, 60), "AR": (35, 100),
    "CA": (40, 80), "CO": (35, 65), "CT": (36, 151), "DE": (21, 41),
    "FL": (40, 120), "GA": (56, 180), "HI": (25, 51), "ID": (35, 70),
    "IL": (59, 118), "IN": (50, 100), "IA": (50, 100), "KS": (40, 125),
    "KY": (38, 100), "LA": (39, 105), "ME": (35, 151), "MD": (47, 141),
    "MA": (40, 160), "MI": (38, 110), "MN": (67, 134), "MS": (52, 122),
    "MO": (34, 163), "MT": (50, 100), "NE": (49, 0), "NV": (21, 42),
    "NH": (24, 400), "NJ": (40, 80), "NM": (42, 70), "NY": (63, 150),
    "NC": (50, 120), "ND": (47, 94), "OH": (33, 99), "OK": (48, 101),
    "OR": (30, 60), "PA": (50, 203), "RI": (38, 75), "SC": (46, 124),
    "SD": (35, 70), "TN": (33, 99), "TX": (31, 150), "UT": (29, 75),
    "VT": (30, 150), "VA": (40, 100), "WA": (49, 98), "WV": (34, 100),
    "WI": (33, 99), "WY": (30, 60),
}

# Top 10 states for p1 state legislature processing
TOP_10_STATES = ["CA", "TX", "FL", "NY", "PA", "IL", "OH", "GA", "NC", "MI"]

# ============================================================
# DATA: Political Systems
# ============================================================

POLITICAL_SYSTEMS = {
    "capitalism": {
        "name": "Capitalism",
        "beliefs": [
            "private-property-rights", "free-market-pricing", "profit-motive",
            "competition-drives-innovation", "voluntary-exchange", "consumer-sovereignty",
            "limited-government-intervention", "capital-accumulation", "entrepreneurship",
            "price-signals-allocate-resources", "meritocracy-rewards-talent",
            "creative-destruction", "comparative-advantage", "rule-of-law-contracts",
            "individual-economic-freedom", "wealth-creation-not-zero-sum",
            "self-interest-produces-social-good", "market-self-correction",
        ],
        "implementations": [
            "us-gilded-age", "us-new-deal-era", "us-neoliberal-era", "uk-thatcherism",
            "singapore-model", "chile-pinochet", "post-2008-crisis", "nordic-mixed-economy",
            "hong-kong-laissez-faire", "japan-developmental-state",
        ],
    },
    "socialism": {
        "name": "Socialism",
        "beliefs": [
            "collective-ownership-means-production", "workers-control", "wealth-redistribution",
            "economic-planning", "social-safety-net", "class-solidarity",
            "labor-theory-of-value", "exploitation-under-capitalism",
            "cooperative-over-competitive", "universal-public-services",
            "progressive-taxation", "anti-imperialism", "economic-democracy",
            "social-ownership-natural-resources", "needs-based-distribution",
        ],
        "implementations": [
            "soviet-union", "maoist-china", "cuba", "venezuela", "yugoslavia-self-management",
            "kibbutz-movement", "nordic-social-democracy", "uk-post-war-consensus",
            "allende-chile", "tanzania-ujamaa",
        ],
    },
    "communism": {
        "name": "Communism",
        "beliefs": [
            "abolition-private-property", "classless-society", "from-each-ability-to-each-need",
            "centralized-economic-planning", "vanguard-party-theory", "class-consciousness",
            "historical-materialism", "dictatorship-of-proletariat", "withering-of-state",
            "collective-ownership-all-property", "abolition-wage-labor",
            "internationalism", "revolution-necessary", "false-consciousness",
            "base-determines-superstructure", "surplus-value-extraction",
            "inevitable-capitalism-collapse", "commune-as-political-unit",
        ],
        "implementations": [
            "soviet-union-lenin", "soviet-union-stalin", "soviet-union-post-stalin",
            "maoist-china-great-leap", "maoist-china-cultural-revolution", "deng-xiaoping-reforms",
            "khmer-rouge-cambodia", "cuba-revolution", "north-korea-juche",
            "vietnam", "east-germany", "poland-prl", "czechoslovakia",
            "hungary-1956", "romania-ceausescu", "albania-hoxha",
        ],
    },
    "fascism": {
        "name": "Fascism",
        "beliefs": [
            "national-rebirth-myth", "organic-nationalism", "totalitarian-state",
            "cult-of-personality", "corporatist-economics", "militarism",
            "social-darwinism", "anti-liberalism", "anti-communism",
            "racial-or-ethnic-supremacy", "palingenetic-ultranationalism",
            "rejection-of-enlightenment", "action-over-thought",
            "national-community-over-individual", "heroic-vitalism",
        ],
        "implementations": [
            "nazi-germany", "mussolini-italy", "franco-spain", "imperial-japan",
            "salazar-portugal", "vichy-france", "ustase-croatia",
            "arrow-cross-hungary", "iron-guard-romania",
        ],
    },
    "libertarianism": {
        "name": "Libertarianism",
        "beliefs": [
            "self-ownership", "non-aggression-principle", "minimal-state",
            "free-market-absolutism", "individual-rights-paramount", "voluntary-association",
            "private-property-inviolable", "anti-taxation", "anti-regulation",
            "spontaneous-order", "drug-legalization", "gun-rights-absolute",
            "open-borders-or-private-borders", "privatize-everything",
            "sound-money-gold-standard", "anti-central-banking",
        ],
        "implementations": [
            "us-libertarian-movement", "free-state-project-nh", "chile-chicago-boys",
            "hong-kong-positive-nonintervention", "new-zealand-rogernomics",
            "estonia-flat-tax", "seasteading-attempts", "crypto-decentralization",
        ],
    },
    "social-democracy": {
        "name": "Social Democracy",
        "beliefs": [
            "regulated-capitalism", "strong-welfare-state", "universal-healthcare",
            "free-education", "progressive-taxation", "collective-bargaining-rights",
            "mixed-economy", "parliamentary-democracy", "social-mobility",
            "equality-of-opportunity", "environmental-regulation",
            "international-cooperation", "human-rights-framework",
            "market-failures-require-intervention", "social-insurance",
        ],
        "implementations": [
            "sweden-model", "denmark-flexicurity", "norway-oil-fund",
            "finland-education", "germany-social-market-economy",
            "netherlands-polder-model", "uk-nhs-creation", "canada-healthcare",
            "australia-medicare", "new-zealand-welfare-state",
        ],
    },
    "democratic-socialism": {
        "name": "Democratic Socialism",
        "beliefs": [
            "democratic-control-of-economy", "worker-cooperatives", "decommodification",
            "anti-capitalism-through-democracy", "social-ownership",
            "participatory-budgeting", "economic-rights-as-human-rights",
            "anti-austerity", "post-capitalist-transition", "green-new-deal",
            "universal-basic-services", "community-wealth-building",
            "democratize-the-workplace", "public-banking",
        ],
        "implementations": [
            "sanders-movement-us", "corbyn-labour-uk", "mondragon-cooperative",
            "kerala-model-india", "porto-alegre-participatory-budget",
            "bolivia-mas", "greece-syriza", "podemos-spain",
        ],
    },
    "authoritarianism": {
        "name": "Authoritarianism",
        "beliefs": [
            "strong-leader-necessary", "order-over-freedom", "limited-political-participation",
            "state-above-individual", "elite-decision-making", "controlled-media",
            "security-justifies-restriction", "stability-paramount",
            "dissent-is-dangerous", "modernization-through-authority",
            "benevolent-dictatorship-possible", "masses-need-guidance",
        ],
        "implementations": [
            "singapore-lee-kuan-yew", "china-ccp", "russia-putin",
            "turkey-erdogan", "hungary-orban", "egypt-sisi",
            "rwandan-kagame", "uae-development-model",
            "south-korea-park-chung-hee", "pinochet-chile",
        ],
    },
    "theocracy": {
        "name": "Theocracy",
        "beliefs": [
            "divine-law-supreme", "religious-authority-over-secular",
            "scripture-as-constitution", "moral-legislation-mandatory",
            "blasphemy-punishable", "religious-education-compulsory",
            "clerical-governance", "sin-as-crime", "gender-roles-divinely-ordained",
            "apostasy-punishable", "religious-courts",
        ],
        "implementations": [
            "iran-islamic-republic", "saudi-arabia-wahhabism", "taliban-afghanistan",
            "calvin-geneva", "papal-states", "tibet-pre-1959",
            "israel-religious-parties", "aceh-sharia",
        ],
    },
    "anarchism": {
        "name": "Anarchism",
        "beliefs": [
            "abolition-of-state", "voluntary-cooperation", "mutual-aid",
            "direct-action", "horizontal-organization", "anti-hierarchy",
            "commons-over-property", "prefigurative-politics",
            "autonomy-and-self-governance", "anti-capitalism",
            "federation-of-communes", "consensus-decision-making",
        ],
        "implementations": [
            "spanish-civil-war-catalonia", "paris-commune-1871", "ukraine-makhnovshchina",
            "zapatistas-chiapas", "rojava-northern-syria", "kibbutz-early-anarchist",
            "christiana-copenhagen", "occupy-movement",
        ],
    },
    "monarchism": {
        "name": "Monarchism",
        "beliefs": [
            "hereditary-right-to-rule", "divine-right-of-kings", "stability-through-continuity",
            "national-unity-through-crown", "constitutional-limits-on-democracy",
            "tradition-as-authority", "noblesse-oblige", "organic-social-hierarchy",
            "ceremonial-vs-executive-power", "loyal-opposition",
        ],
        "implementations": [
            "uk-constitutional-monarchy", "saudi-absolute-monarchy",
            "japan-symbolic-monarchy", "thailand-monarchy", "morocco-monarchy",
            "jordan-monarchy", "bhutan-monarchy", "spain-restored-monarchy",
            "sweden-ceremonial-monarchy", "brunei-absolute-monarchy",
        ],
    },
    "federalism": {
        "name": "Federalism",
        "beliefs": [
            "divided-sovereignty", "subsidiarity-principle", "states-as-laboratories",
            "power-sharing", "constitutional-enumeration", "intergovernmental-cooperation",
            "minority-protection-through-decentralization", "fiscal-federalism",
            "competitive-governance", "anti-centralization",
        ],
        "implementations": [
            "us-federalism", "german-federalism", "swiss-federalism",
            "canadian-federalism", "australian-federalism", "indian-federalism",
            "brazilian-federalism", "eu-supranational-federalism",
            "nigerian-federalism", "russian-federalism",
        ],
    },
    "confederalism": {
        "name": "Confederalism",
        "beliefs": [
            "state-sovereignty-paramount", "weak-central-authority", "right-of-secession",
            "voluntary-union", "unanimous-consent", "decentralized-military",
            "no-direct-taxation-by-center", "treaty-based-governance",
        ],
        "implementations": [
            "us-articles-of-confederation", "confederate-states-america",
            "swiss-old-confederacy", "german-confederation-1815",
            "senegambia-confederation", "arab-federation", "benelux-union",
        ],
    },
    "meritocracy": {
        "name": "Meritocracy",
        "beliefs": [
            "talent-determines-position", "standardized-testing", "equal-opportunity-not-outcome",
            "expertise-in-governance", "competitive-selection", "reward-proportional-to-contribution",
            "education-as-equalizer", "anti-nepotism", "credential-based-authority",
            "objective-measurement-possible",
        ],
        "implementations": [
            "singapore-meritocratic-governance", "china-imperial-examination",
            "us-civil-service-reform", "uk-civil-service-northcote-trevelyan",
            "japan-corporate-meritocracy", "south-korea-education-system",
        ],
    },
    "technocracy": {
        "name": "Technocracy",
        "beliefs": [
            "expert-governance", "evidence-based-policy", "depoliticize-decision-making",
            "scientific-management-of-society", "efficiency-over-representation",
            "data-driven-government", "complexity-requires-expertise",
            "democratic-incompetence-in-technical-matters",
        ],
        "implementations": [
            "singapore-technocratic-governance", "eu-commission-technocracy",
            "italy-monti-government", "greece-papademos-government",
            "china-engineer-politicians", "covid-public-health-technocracy",
        ],
    },
    "populism": {
        "name": "Populism",
        "beliefs": [
            "people-vs-elite", "popular-sovereignty-absolute", "anti-establishment",
            "direct-democracy-preference", "charismatic-leadership",
            "common-sense-over-expertise", "national-will-expression",
            "anti-pluralism", "moral-purity-of-people", "conspiracy-of-elites",
        ],
        "implementations": [
            "trump-maga-us", "bolsonaro-brazil", "orban-hungary",
            "five-star-italy", "podemos-spain", "syriza-greece",
            "chavez-venezuela", "peron-argentina", "erdogan-turkey",
            "duterte-philippines",
        ],
    },
    "nationalism": {
        "name": "Nationalism",
        "beliefs": [
            "nation-as-primary-identity", "national-self-determination",
            "cultural-preservation", "border-sovereignty", "national-interest-first",
            "common-language-unity", "historical-narrative-importance",
            "immigration-control", "economic-nationalism-protectionism",
            "military-strength-national-pride",
        ],
        "implementations": [
            "french-revolution-nationalism", "german-unification-bismarck",
            "italian-risorgimento", "zionism-israel", "hindu-nationalism-india",
            "japanese-nationalism", "kurdish-nationalism", "catalan-independence",
            "scottish-independence", "quebec-sovereignty",
        ],
    },
    "globalism": {
        "name": "Globalism",
        "beliefs": [
            "free-trade-benefits-all", "international-institutions",
            "open-borders-ideal", "cultural-exchange-enriches", "global-governance",
            "human-rights-universal", "climate-requires-cooperation",
            "economic-interdependence-prevents-war", "cosmopolitan-identity",
            "supranational-law",
        ],
        "implementations": [
            "european-union", "united-nations-system", "wto-free-trade",
            "imf-world-bank", "nafta-usmca", "asean-integration",
            "african-union", "paris-climate-accord", "icc-international-law",
        ],
    },
    "conservatism": {
        "name": "Conservatism",
        "beliefs": [
            "tradition-as-wisdom", "gradual-change-only", "skepticism-of-utopia",
            "organic-society", "respect-for-institutions", "personal-responsibility",
            "family-as-foundation", "religious-moral-framework",
            "free-enterprise", "strong-national-defense",
            "law-and-order", "limited-government", "fiscal-responsibility",
            "cultural-continuity", "burkean-prudence",
        ],
        "implementations": [
            "reagan-revolution-us", "thatcher-uk", "bismarck-conservatism",
            "tory-party-evolution", "republican-party-us", "cdu-germany",
            "liberal-party-australia", "conservative-party-canada",
            "one-nation-conservatism-uk", "neoconservatism-us",
        ],
    },
    "progressivism": {
        "name": "Progressivism",
        "beliefs": [
            "progress-through-reform", "social-justice", "equality-expansion",
            "government-as-positive-force", "science-guides-policy",
            "institutional-reform", "civil-rights-expansion", "environmental-protection",
            "labor-rights", "education-reform", "healthcare-as-right",
            "anti-discrimination", "democratic-participation-expansion",
            "evidence-based-governance",
        ],
        "implementations": [
            "us-progressive-era-1900s", "new-deal-us", "great-society-us",
            "civil-rights-movement", "new-labour-uk", "scandinavian-progressivism",
            "obama-era-us", "trudeau-canada", "macron-centrism-france",
        ],
    },
}

# ============================================================
# DATA: Controversy Classes
# ============================================================

CONTROVERSY_CLASSES = [
    ("abortion-rights", "Abortion Rights"),
    ("gun-control", "Gun Control and Firearms Regulation"),
    ("immigration-policy", "Immigration Policy"),
    ("healthcare-system", "Healthcare System Design"),
    ("death-penalty", "Capital Punishment"),
    ("drug-legalization", "Drug Legalization and Decriminalization"),
    ("free-speech-limits", "Free Speech and Its Limits"),
    ("religious-freedom-vs-discrimination", "Religious Freedom vs. Anti-Discrimination"),
    ("climate-change-policy", "Climate Change Policy"),
    ("wealth-inequality", "Wealth Inequality and Redistribution"),
    ("voting-rights", "Voting Rights and Election Integrity"),
    ("police-reform", "Police Reform and Public Safety"),
    ("education-curriculum", "Education Curriculum and Standards"),
    ("gender-identity", "Gender Identity and Trans Rights"),
    ("surveillance-privacy", "Surveillance vs. Privacy"),
    ("nuclear-energy", "Nuclear Energy"),
    ("minimum-wage", "Minimum Wage and Living Wage"),
    ("housing-affordability", "Housing Affordability and Zoning"),
    ("censorship-media", "Media Censorship and Regulation"),
    ("military-intervention", "Military Intervention and Foreign Policy"),
    ("vaccine-mandates", "Vaccine Mandates and Public Health"),
    ("ai-regulation", "AI Regulation and Ethics"),
    ("cryptocurrency-regulation", "Cryptocurrency Regulation"),
    ("rent-control", "Rent Control"),
    ("school-choice-vouchers", "School Choice and Vouchers"),
    ("affirmative-action", "Affirmative Action"),
    ("euthanasia-assisted-suicide", "Euthanasia and Assisted Suicide"),
    ("sex-work-legalization", "Sex Work Legalization"),
    ("universal-basic-income", "Universal Basic Income"),
    ("reparations", "Reparations"),
    ("term-limits", "Term Limits"),
    ("electoral-college", "Electoral College vs. Popular Vote"),
    ("court-packing", "Court Packing and Judicial Reform"),
    ("gerrymandering", "Gerrymandering and Redistricting"),
    ("corporate-personhood", "Corporate Personhood"),
    ("right-to-work", "Right to Work Laws"),
    ("eminent-domain", "Eminent Domain"),
    ("qualified-immunity", "Qualified Immunity"),
    ("bail-reform", "Bail Reform"),
    ("mandatory-minimums", "Mandatory Minimum Sentencing"),
    ("stand-your-ground", "Stand Your Ground Laws"),
    ("sanctuary-cities", "Sanctuary Cities"),
    ("book-banning", "Book Banning and Library Challenges"),
    ("prayer-in-schools", "Prayer in Public Schools"),
    ("separation-church-state", "Separation of Church and State"),
    ("genetic-engineering", "Genetic Engineering and CRISPR"),
    ("animal-rights", "Animal Rights and Factory Farming"),
    ("water-fluoridation", "Water Fluoridation"),
    ("homeschooling-regulation", "Homeschooling Regulation"),
    ("sex-education", "Sex Education in Schools"),
    ("draft-conscription", "Military Draft and Conscription"),
    ("foreign-aid", "Foreign Aid"),
    ("trade-protectionism", "Trade Protectionism vs. Free Trade"),
    ("social-media-regulation", "Social Media Regulation"),
    ("data-privacy", "Data Privacy and Big Tech"),
    ("autonomous-weapons", "Autonomous Weapons"),
    ("space-militarization", "Space Militarization"),
    ("nuclear-proliferation", "Nuclear Proliferation"),
    ("indigenous-rights", "Indigenous Rights and Land Claims"),
    ("refugee-policy", "Refugee Policy and Asylum"),
    ("child-labor-laws", "Child Labor Laws"),
    ("gig-economy-regulation", "Gig Economy Worker Classification"),
    ("union-rights", "Union Rights and Collective Bargaining"),
    ("patent-reform", "Patent Reform and IP"),
    ("net-neutrality", "Net Neutrality"),
    ("environmental-regulation", "Environmental Regulation and Industry"),
    ("carbon-tax", "Carbon Tax"),
    ("plastic-ban", "Plastic Bans and Waste"),
    ("factory-farming", "Factory Farming Regulation"),
    ("water-rights", "Water Rights and Scarcity"),
    ("energy-transition", "Energy Transition and Fossil Fuels"),
    ("public-transit-funding", "Public Transit vs. Car Infrastructure"),
    ("homelessness-policy", "Homelessness Policy"),
    ("mental-health-policy", "Mental Health Policy and Involuntary Commitment"),
    ("student-loan-debt", "Student Loan Debt and Education Costs"),
    ("age-verification-internet", "Age Verification and Internet Access"),
    ("deepfake-regulation", "Deepfake Regulation"),
    ("lab-grown-meat", "Lab-Grown Meat Regulation"),
    ("psychedelic-therapy", "Psychedelic Therapy Legalization"),
    ("right-to-repair", "Right to Repair"),
]

# ============================================================
# DATA: Controversy class templates
# ============================================================

CONTROVERSY_TEMPLATES = [
    ("template-school-board", "School Board Controversy Template"),
    ("template-city-council", "City Council Controversy Template"),
    ("template-code-enforcement", "Code Enforcement Controversy Template"),
    ("template-county-commission", "County Commission Controversy Template"),
    ("template-state-legislature", "State Legislature Controversy Template"),
    ("template-police-sheriff", "Police/Sheriff Controversy Template"),
    ("template-public-utilities", "Public Utilities Controversy Template"),
    ("template-parks-recreation", "Parks & Recreation Controversy Template"),
    ("template-health-department", "Health Department Controversy Template"),
    ("template-library-board", "Library Board Controversy Template"),
    ("template-planning-commission", "Planning Commission Controversy Template"),
    ("template-transportation", "Transportation Authority Controversy Template"),
    ("template-election-board", "Election Board Controversy Template"),
    ("template-environmental", "Environmental Agency Controversy Template"),
    ("template-national-policy", "National Policy Controversy Template"),
    ("template-international", "International Relations Controversy Template"),
    ("template-judicial", "Judicial/Court Controversy Template"),
    ("template-executive-action", "Executive Action Controversy Template"),
    ("template-regulatory-agency", "Regulatory Agency Controversy Template"),
    ("template-military-defense", "Military/Defense Controversy Template"),
]

# Daily controversy seed pages — 500 at launch
# We generate slugs for these based on country+class combinations
TIER_1_COUNTRIES = [
    "us", "uk", "canada", "australia", "germany", "france", "brazil", "india",
    "japan", "south-korea", "mexico", "italy", "spain", "netherlands", "sweden",
    "norway", "denmark", "finland", "ireland", "poland", "turkey", "south-africa",
    "nigeria", "egypt", "indonesia", "philippines", "thailand", "argentina",
    "colombia", "chile",
]

# Historical controversies — Tier 1: 500 most significant
HISTORICAL_CONTROVERSIES = [
    # US
    "us-slavery-abolition", "us-civil-war-secession", "us-reconstruction",
    "us-womens-suffrage", "us-prohibition", "us-new-deal", "us-japanese-internment",
    "us-mccarthy-red-scare", "us-civil-rights-1960s", "us-vietnam-war",
    "us-watergate", "us-roe-v-wade-1973", "us-iran-hostage", "us-reaganomics",
    "us-iran-contra", "us-gulf-war-1991", "us-clinton-impeachment",
    "us-bush-v-gore-2000", "us-iraq-war-2003", "us-financial-crisis-2008",
    "us-obamacare", "us-marriage-equality", "us-trump-election-2016",
    "us-capitol-jan6", "us-dobbs-roe-reversal",
    # UK
    "uk-magna-carta", "uk-english-civil-war", "uk-glorious-revolution",
    "uk-corn-laws", "uk-chartist-movement", "uk-irish-home-rule",
    "uk-suffragettes", "uk-general-strike-1926", "uk-appeasement-munich",
    "uk-nhs-creation-1948", "uk-suez-crisis", "uk-troubles-northern-ireland",
    "uk-miners-strike-1984", "uk-poll-tax", "uk-iraq-war-dodgy-dossier",
    "uk-brexit-referendum", "uk-scottish-independence-2014",
    # France
    "france-revolution-1789", "france-reign-of-terror", "france-napoleon-coup",
    "france-dreyfus-affair", "france-vichy-collaboration", "france-algerian-war",
    "france-may-1968", "france-headscarf-ban", "france-charlie-hebdo",
    "france-yellow-vests", "france-pension-reform",
    # Germany
    "germany-unification-1871", "germany-weimar-republic", "germany-nazi-rise",
    "germany-holocaust", "germany-berlin-wall", "germany-reunification-1990",
    "germany-refugee-crisis-2015", "germany-nuclear-phase-out",
    # Russia/Soviet
    "russia-bolshevik-revolution", "russia-stalin-purges", "russia-gulag-system",
    "russia-cuban-missile-crisis", "russia-afghan-invasion-1979",
    "russia-chernobyl", "russia-soviet-collapse", "russia-chechen-wars",
    "russia-crimea-annexation", "russia-ukraine-invasion-2022",
    # China
    "china-opium-wars", "china-boxer-rebellion", "china-communist-revolution",
    "china-great-leap-forward", "china-cultural-revolution", "china-tiananmen-1989",
    "china-hong-kong-handover", "china-one-child-policy",
    "china-tibet-occupation", "china-uyghur-detention",
    # India
    "india-partition-1947", "india-kashmir-conflict", "india-emergency-1975",
    "india-bhopal-disaster", "india-babri-masjid", "india-nuclear-tests-1998",
    "india-caa-nrc-protests", "india-farm-laws-protest",
    # Japan
    "japan-meiji-restoration", "japan-manchuria-invasion", "japan-pearl-harbor",
    "japan-atomic-bombings", "japan-comfort-women", "japan-fukushima",
    # Middle East
    "israel-creation-1948", "israel-six-day-war", "israel-settlement-expansion",
    "israel-gaza-conflicts", "iran-revolution-1979", "iraq-kuwait-invasion",
    "arab-spring-2011", "syrian-civil-war", "yemen-civil-war",
    # Africa
    "south-africa-apartheid", "south-africa-mandela-release",
    "rwanda-genocide-1994", "congo-wars", "nigeria-biafra-war",
    "kenya-mau-mau", "ethiopia-eritrea-war", "libya-gaddafi-overthrow",
    # Latin America
    "cuba-revolution-1959", "chile-allende-coup-1973", "argentina-dirty-war",
    "brazil-military-dictatorship", "mexico-drug-war", "venezuela-crisis",
    "colombia-farc-peace", "nicaragua-sandinista-revolution",
    # Global / Cross-cutting
    "ww1-causes-blame", "ww2-appeasement-debate", "cold-war-containment",
    "decolonization-legacy", "nuclear-arms-race", "globalization-debate",
    "war-on-terror", "climate-change-denial", "covid-pandemic-response",
    "refugee-crisis-global",
    # Fill to 500 with more specific controversies
]

# We'll pad to 500 with generated entries below
ADDITIONAL_HISTORICAL = []
for country in ["us", "uk", "france", "germany", "russia", "china", "india", "japan",
                 "brazil", "mexico", "south-africa", "australia", "canada", "italy",
                 "spain", "turkey", "egypt", "indonesia", "south-korea", "argentina",
                 "colombia", "chile", "nigeria", "poland", "iran", "iraq", "israel"]:
    for era in ["colonial", "independence", "industrial", "modern", "contemporary"]:
        slug = f"{country}-{era}-political-controversy"
        if slug not in [h for h in HISTORICAL_CONTROVERSIES]:
            ADDITIONAL_HISTORICAL.append(slug)

ALL_HISTORICAL = HISTORICAL_CONTROVERSIES + ADDITIONAL_HISTORICAL
ALL_HISTORICAL = ALL_HISTORICAL[:500]  # Cap at 500

# Voter guides — 50 states
VOTER_GUIDE_STATES = US_STATES

# Languages for translation
LANGUAGES = ["es", "fr", "de", "pt", "ja"]

# ============================================================
# GENERATION FUNCTIONS
# ============================================================

def gen_levciti_backlog():
    """Generate the complete levciti.com backlog."""
    tickets = []
    seen_slugs = set()

    def add(slug, title, typ, priority, deps=None):
        if slug in seen_slugs:
            return
        seen_slugs.add(slug)
        tickets.append({
            "slug": slug,
            "title": title,
            "type": typ,
            "pipeline": "levciti_content",
            "priority": priority,
            "dependencies": deps or [],
            "status": "backlog",
        })

    # ---- Top 100 US cities (p0) ----
    for slug, name, state in TOP_100_US_CITIES:
        city_slug = f"city-us-{slug}"
        add(city_slug, f"{name}, {state} -- City Dashboard", "city_page", "p0")
        add(f"{city_slug}-comparison", f"{name}, {state} -- City Comparison", "city_comparison", "p0", [city_slug])
        add(f"{city_slug}-local-controversy", f"{name}, {state} -- Local Controversy Coverage", "local_controversy", "p0", [city_slug])

    # ---- US State capitals not already in top 100 (p2) ----
    for slug, name, state in US_STATE_CAPITALS:
        city_slug = f"city-us-{slug}"
        add(city_slug, f"{name}, {state} -- City Dashboard", "city_page", "p2")
        add(f"{city_slug}-comparison", f"{name}, {state} -- City Comparison", "city_comparison", "p2", [city_slug])
        add(f"{city_slug}-local-controversy", f"{name}, {state} -- Local Controversy Coverage", "local_controversy", "p2", [city_slug])

    # ---- US cities over 100K (p2) ----
    for slug, name, state in US_CITIES_OVER_100K:
        city_slug = f"city-us-{slug}"
        add(city_slug, f"{name}, {state} -- City Dashboard", "city_page", "p2")
        add(f"{city_slug}-comparison", f"{name}, {state} -- City Comparison", "city_comparison", "p2", [city_slug])
        add(f"{city_slug}-local-controversy", f"{name}, {state} -- Local Controversy Coverage", "local_controversy", "p2", [city_slug])

    # ---- National capitals (p1) ----
    for slug, name, country in NATIONAL_CAPITALS:
        city_slug = f"city-intl-{slug}"
        add(city_slug, f"{name}, {country} -- City Dashboard", "city_page", "p1")
        add(f"{city_slug}-comparison", f"{name}, {country} -- City Comparison", "city_comparison", "p1", [city_slug])
        add(f"{city_slug}-local-controversy", f"{name}, {country} -- Local Controversy Coverage", "local_controversy", "p1", [city_slug])

    # ---- Tier 1 international cities (p1) ----
    intl_cities = [
        ("uk", UK_TOP_50), ("canada", CANADA_TOP_50), ("australia", AUSTRALIA_TOP_50),
        ("germany", GERMANY_TOP_50), ("france", FRANCE_TOP_50), ("brazil", BRAZIL_TOP_50),
        ("india", INDIA_TOP_50), ("japan", JAPAN_TOP_50),
    ]
    for country, cities in intl_cities:
        for city_slug_raw in cities:
            city_slug = f"city-{country}-{city_slug_raw}"
            nice_name = city_slug_raw.replace("-", " ").title()
            add(city_slug, f"{nice_name}, {country.upper()} -- City Dashboard", "city_page", "p1")
            add(f"{city_slug}-comparison", f"{nice_name}, {country.upper()} -- City Comparison", "city_comparison", "p1", [city_slug])
            add(f"{city_slug}-local-controversy", f"{nice_name}, {country.upper()} -- Local Controversy Coverage", "local_controversy", "p1", [city_slug])

    # ---- Translations ----
    base_tickets = list(tickets)  # snapshot before translations
    for lang in LANGUAGES:
        for t in base_tickets:
            tr_slug = f"{t['slug']}-{lang}"
            add(tr_slug, f"[{lang.upper()}] {t['title']}", t["type"], "p2" if t["priority"] == "p0" else "p3", [t["slug"]])

    # Summary
    type_counts = {}
    priority_counts = {}
    for t in tickets:
        type_counts[t["type"]] = type_counts.get(t["type"], 0) + 1
        priority_counts[t["priority"]] = priority_counts.get(t["priority"], 0) + 1

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_tickets": len(tickets),
        "summary": {
            "by_type": type_counts,
            "by_priority": priority_counts,
        },
        "tickets": tickets,
    }


def gen_levnation_backlog():
    """Generate the complete levnation.com backlog."""
    tickets = []
    seen_slugs = set()

    def add(slug, title, typ, priority, deps=None):
        if slug in seen_slugs:
            return
        seen_slugs.add(slug)
        tickets.append({
            "slug": slug,
            "title": title,
            "type": typ,
            "pipeline": "levnation_content",
            "priority": priority,
            "dependencies": deps or [],
            "status": "backlog",
        })

    # ==== POLITICIANS ====

    # US Senate — 100 senators (p0)
    for state in US_STATES:
        state_name = US_STATE_NAMES[state]
        for seat in [1, 2]:
            slug = f"pol-us-senate-{state.lower()}-seat{seat}"
            add(slug, f"US Senator -- {state_name} Seat {seat}", "politician", "p0")

    # US House — 435 representatives (p0)
    for state in US_STATES:
        state_name = US_STATE_NAMES[state]
        districts = HOUSE_DISTRICTS[state]
        for d in range(1, districts + 1):
            slug = f"pol-us-house-{state.lower()}-{d:02d}"
            add(slug, f"US Representative -- {state_name} District {d}", "politician", "p0")

    # US Governors — 50 (p0)
    for state in US_STATES:
        state_name = US_STATE_NAMES[state]
        slug = f"pol-us-governor-{state.lower()}"
        add(slug, f"US Governor -- {state_name}", "politician", "p0")

    # US State Legislators — top 10 states (p1), rest (p2)
    for state in US_STATES:
        state_name = US_STATE_NAMES[state]
        senate_size, house_size = STATE_LEGISLATURE_SIZES[state]
        priority = "p1" if state in TOP_10_STATES else "p2"

        for s in range(1, senate_size + 1):
            slug = f"pol-us-state-senate-{state.lower()}-{s:03d}"
            add(slug, f"State Senator -- {state_name} District {s}", "politician", priority)

        for h in range(1, house_size + 1):
            slug = f"pol-us-state-house-{state.lower()}-{h:03d}"
            title_chamber = "State Representative" if state != "NE" else "State Senator (Unicameral)"
            add(slug, f"{title_chamber} -- {state_name} District {h}", "politician", priority)

    # UK Parliament — ~650 (p2)
    for i in range(1, 651):
        slug = f"pol-uk-mp-{i:04d}"
        add(slug, f"UK Member of Parliament -- Constituency {i}", "politician", "p2")

    # Canada Parliament — ~338 (p2)
    for i in range(1, 339):
        slug = f"pol-canada-mp-{i:04d}"
        add(slug, f"Canada Member of Parliament -- Riding {i}", "politician", "p2")

    # Australia Parliament — ~227 (p2)
    for i in range(1, 152):
        slug = f"pol-australia-mp-{i:04d}"
        add(slug, f"Australia Member of Parliament -- Division {i}", "politician", "p2")
    for i in range(1, 77):
        slug = f"pol-australia-senator-{i:04d}"
        add(slug, f"Australia Senator -- Seat {i}", "politician", "p2")

    # ==== CONTROVERSY CLASSES ====
    for slug, name in CONTROVERSY_CLASSES:
        add(f"class-{slug}", f"Controversy Class -- {name}", "controversy_class", "p0")

    # ==== CONTROVERSY TEMPLATES ====
    for slug, name in CONTROVERSY_TEMPLATES:
        add(slug, name, "controversy_class", "p0")

    # ==== DAILY CONTROVERSY PAGES (seed ~500) ====
    # Generate ~17 per Tier 1 country from top controversy classes
    controversy_count = 0
    for country in TIER_1_COUNTRIES:
        for cls_slug, cls_name in CONTROVERSY_CLASSES[:17]:
            slug = f"controversy-{country}-{cls_slug}"
            add(slug, f"[{country.upper()}] Active Controversy -- {cls_name}", "controversy", "p0")
            controversy_count += 1
            if controversy_count >= 500:
                break
        if controversy_count >= 500:
            break

    # ==== POLITICAL ENCYCLOPEDIA ====
    for sys_slug, sys_data in POLITICAL_SYSTEMS.items():
        sys_name = sys_data["name"]

        # Decomposition page
        add(f"polsys-{sys_slug}-decomposition", f"Political System -- {sys_name} Decomposition", "political_system", "p1")

        # Per-belief pages
        for belief_slug in sys_data["beliefs"]:
            add(f"polbelief-{sys_slug}-{belief_slug}", f"{sys_name} Belief -- {belief_slug.replace('-', ' ').title()}", "political_belief", "p1",
                [f"polsys-{sys_slug}-decomposition"])

        # Per-implementation pages
        for impl_slug in sys_data["implementations"]:
            add(f"polimpl-{sys_slug}-{impl_slug}", f"{sys_name} Implementation -- {impl_slug.replace('-', ' ').title()}", "political_implementation", "p2",
                [f"polsys-{sys_slug}-decomposition"])

    # ==== VOTER GUIDES ====
    for state in VOTER_GUIDE_STATES:
        state_name = US_STATE_NAMES[state]
        add(f"voter-guide-{state.lower()}", f"Personalized Voter Guide -- {state_name}", "voter_guide", "p1")

    # ==== HISTORICAL CONTROVERSIES ====
    for slug in ALL_HISTORICAL:
        add(f"historical-{slug}", f"Historical Controversy -- {slug.replace('-', ' ').title()}", "historical_controversy", "p2")

    # ==== TRANSLATIONS ====
    base_tickets = list(tickets)
    for lang in LANGUAGES:
        for t in base_tickets:
            # Only translate p0 and p1 content, skip individual politician pages for translation
            if t["type"] == "politician":
                continue  # Politicians don't need translation — their pages are data-driven
            tr_slug = f"{t['slug']}-{lang}"
            tr_priority = "p2" if t["priority"] in ("p0", "p1") else "p3"
            add(tr_slug, f"[{lang.upper()}] {t['title']}", t["type"], tr_priority, [t["slug"]])

    # Summary
    type_counts = {}
    priority_counts = {}
    for t in tickets:
        type_counts[t["type"]] = type_counts.get(t["type"], 0) + 1
        priority_counts[t["priority"]] = priority_counts.get(t["priority"], 0) + 1

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_tickets": len(tickets),
        "summary": {
            "by_type": type_counts,
            "by_priority": priority_counts,
        },
        "tickets": tickets,
    }


if __name__ == "__main__":
    import os

    out_dir = "/Users/user/personal/sb/trueassess/priv/data"

    # Generate levciti
    levciti = gen_levciti_backlog()
    path = os.path.join(out_dir, "levciti_backlog.json")
    with open(path, "w") as f:
        json.dump(levciti, f, indent=2, ensure_ascii=False)
    print(f"levciti_backlog.json: {levciti['total_tickets']} tickets")
    print(f"  By type: {json.dumps(levciti['summary']['by_type'], indent=4)}")
    print(f"  By priority: {json.dumps(levciti['summary']['by_priority'], indent=4)}")
    print()

    # Generate levnation
    levnation = gen_levnation_backlog()
    path = os.path.join(out_dir, "levnation_backlog.json")
    with open(path, "w") as f:
        json.dump(levnation, f, indent=2, ensure_ascii=False)
    print(f"levnation_backlog.json: {levnation['total_tickets']} tickets")
    print(f"  By type: {json.dumps(levnation['summary']['by_type'], indent=4)}")
    print(f"  By priority: {json.dumps(levnation['summary']['by_priority'], indent=4)}")
