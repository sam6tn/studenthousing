//data
var allLocations = [
{
  "model": "housing.post",
  "pk": 1,
  
    "name": "The Fred",
    "info": "Live in this wonderful apartment that is close to the corner and very cost efficient",
    "address": "1207 Wertland Street  Charlottesville, VA 22903",
    "price": 650,
    "rating": 3,
    "image_url": "https://livewithmsc.com/wp-content/uploads/2018/10/fred.jpg",
    "baths": 2,
    "rooms": 2,
    "available": true,
    "lat": 38.0346159,
    "lng": -78.4965872115102
  
},
{
  "model": "housing.post",
  "pk": 2,
  
    "name": "Wertland Square",
    "info": "Accessed",
    "address": "216 14th Street Charlottesville, VA 22903",
    "price": 850,
    "rating": 4,
    "image_url": "https://s2rf64.cloudimg.io/s/cdn/x/https://s3.amazonaws.com/cdn.ucribs.com/images/listings/11125/Wertland%20Square%202.jpg",
    "baths": 2,
    "rooms": 4,
    "available": false,
    "lat": 0.0,
    "lng": 0.0
  
},
{
  "model": "housing.post",
  "pk": 3,
  
    "name": "1815 JPA",
    "info": "Great community, washer/dryer in unit, bus stop",
    "address": "1815 Jefferson Park Ave, Charlottesville, VA 22903",
    "price": 550,
    "rating": 4,
    "image_url": "https://www.martinhorn.com/wp-content/uploads/2013/08/1815JPA_ext_SS_710x468.jpg",
    "baths": 2,
    "rooms": 4,
    "available": true,
    "lat": 38.02850705,
    "lng": -78.5106060695629
  
},
{
  "model": "housing.post",
  "pk": 4,
 
    "name": "The Flats at West Village",
    "info": "Included: washer/dryer in unit, trash, cable, internet, heat",
    "address": "852 West Main Street Charlottesville, VA 22903",
    "price": 800,
    "rating": 0,
    "image_url": "https://images1.apartments.com/i2/RWkEd_MSFPejCyjO6IWXjCW-ilssEmBL38ffVgsViJQ/111/the-flats-west-village-charlottesville-va-primary-photo.jpg",
    "baths": 4,
    "rooms": 4,
    "available": true,
    "lat": 38.031883,
    "lng": -78.4929221396699
  
},
{
  "model": "housing.post",
  "pk": 5,
 
    "name": "Oxbridge Place",
    "info": "close to the corner, gym, and study lounges.",
    "address": "313 13th St NW, Charlottesville, VA 22903",
    "price": 700,
    "rating": 4,
    "image_url": "https://cdn.apartmenthomeliving.com/VA/Charlottesville/3632697/170218/Oxbridge-Place-Apartments-Charlottesville-VA-photo-001_sm.jpg",
    "baths": 2,
    "rooms": 3,
    "available": false,
    "lat": 38.0364704,
    "lng": -78.497445057377
  
},
{
  "model": "housing.post",
  "pk": 6,
  
    "name": "GrandMarc at the Corner",
    "info": "Washer/Dryer in Unit Cable, Gas, High-Speed Internet, Recycling, Trash Removal, Water/Sewer included",
    "address": "301 15th St. NW Charlottesville, VA 22903",
    "price": 900,
    "rating": 0,
    "image_url": "https://img.offcampusimages.com/gFIhfde4s7vSPZ40Z4qRVB70KPk=/660x440/left/top/smart/images/loycivccswk4vzzlgqkai_k3qrqdgo5t9atpzzfazxg.jpeg",
    "baths": 2,
    "rooms": 4,
    "available": true,
    "lat": 38.0376871,
    "lng": -78.4991617
  
},
{
  "model": "housing.post",
  "pk": 7,
  
    "name": "Rugby McIntyre Efficiencies",
    "info": "studio apartments on Rugby Ave",
    "address": "611 Rugby Road Charlottesville, VA 22903",
    "price": 850,
    "rating": 0,
    "image_url": "http://www.brac.com/photos/14/large/14_160108_111258_5482.jpg",
    "baths": 1,
    "rooms": 1,
    "available": true,
    "lat": 38.04286655,
    "lng": -78.5000464769197
  
},
{
  "model": "housing.post",
  "pk": 8,
  
    "name": "The Standard",
    "info": "Modern living in fully furnished apartments with TV and a pool table.",
    "address": "853 West Main Street, Charlottesville, VA 22903",
    "price": 1000,
    "rating": 0,
    "image_url": "https://images1.apartments.com/i2/XL4c3SL88ZNx_3V9E_Z6UX2XsIc1zIl-pv4BnV78SWI/117/the-standard-at-charlottesville-charlottesville-va-primary-photo.jpg",
    "baths": 4,
    "rooms": 4,
    "available": true,
    "lat": 38.0322268377361,
    "lng": -78.4927312250983
  
},
{
  "model": "housing.post",
  "pk": 9,
  
    "name": "Jefferson Commons",
    "info": "Fitness and movie centers, pets allowed, parking.",
    "address": "1620 Jefferson Park Ave, Charlottesville, VA 22903",
    "price": 700,
    "rating": 0,
    "image_url": "https://image1.apartmentfinder.com/i2/3DPYT_IWwobkie3uL5NnjDD5ZSSSh8xfAwzPMO9vEO4/117/jefferson-commons-charlottesville-va-primary-photo.jpg",
    "baths": 2,
    "rooms": 4,
    "available": false,
    "lat": 38.0307936,
    "lng": -78.5079473761887
  
},
{
  "model": "housing.post",
  "pk": 10,
  
    "name": "University Heights",
    "info": "Affordable housing off ivy road, 1 2 3 4 bedrooms.",
    "address": "250 Colonnade Dr, Charlottesville, VA 22903",
    "price": 450,
    "rating": 0,
    "image_url": "https://image1.apartmentfinder.com/i2/U9HxjQ5kqwrsp75fadlDCCZLq2B4E0VB2kpkhXhrl2g/110/university-heights-charlottesville-va-building-photo.jpg",
    "baths": 2,
    "rooms": 4,
    "available": true,
    "lat": 0.0,
    "lng": 0.0
  
},
{
  "model": "housing.post",
  "pk": 11,
 
    "name": "1303 Wertland St",
    "info": "Near the Corner",
    "address": "1303 WERTLAND STREET,  CHARLOTTESVILLE, VA 22903",
    "price": 600,
    "rating": 0,
    "image_url": "https://static1.squarespace.com/static/53025668e4b0c7fb3f1c4156/54874f22e4b07ac01733ddf4/556dc904e4b0970bf67f4704/1433258253576/IMG_9130asmall.jpg?format=1500w",
    "baths": 2,
    "rooms": 2,
    "available": true,
    "lat": 38.03507305,
    "lng": -78.4976384480121
  
},
{
  "model": "housing.post",
  "pk": 12,
  
    "name": "1910 JPA",
    "info": "A full kitchen including range, refrigerator, and dishwasher. Also included within each apartment is a washer and dryer",
    "address": "1910 Jefferson Park Avenue, Charlottesville, VA 22903",
    "price": 600,
    "rating": 0,
    "image_url": "https://ivysquare.appfoliowebsites6.com/wp-content/uploads/sites/6136/2016/09/1910main.jpg",
    "baths": 2,
    "rooms": 3,
    "available": true,
    "lat": 38.02689405,
    "lng": -78.5119541424778
  
},
{
  "model": "housing.post",
  "pk": 13,
  
    "name": "The Greek",
    "info": "Only one unit left!",
    "address": "1510 Virginia Ave, Charlottesville, VA 22903",
    "price": 825,
    "rating": 0,
    "image_url": "https://www.cbsrentals.com/majorphotos/large/majorphoto_190128_013342_7826.jpg",
    "baths": 2,
    "rooms": 4,
    "available": true,
    "lat": 38.0382064,
    "lng": -78.4993202000322
  
},
{
  "model": "housing.post",
  "pk": 14,
    "name": "Cavalier Crossing",
    "info": "Living community with a shuttle to and from grounds.",
    "address": "100 Wahoo Way, Charlottesville, VA 22903",
    "price": 500,
    "rating": 0,
    "image_url": "https://images1.apartments.com/i2/prpYnOK95NcHws64oK4glHNUXsaArEDHwHf36oQ9qfQ/111/cavalier-crossing-charlottesville-va-primary-photo.jpg",
    "baths": 3,
    "rooms": 3,
    "available": true,
    "lat": 0.0,
    "lng": 0.0
  
}
];
