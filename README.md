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

The original JSON file was scraped together from a few places and updated by hand over time.

Instead, it makes more sense in the future to use the Companies House data. The
original data was riddled with fake busniesses or just small businesses that
didn't last very long. Some of the data originates from when all you needed was a twitter handle or 
a facebook page and as such, legitmate business are hard to separate from the fake ones.

You can view the original geojson data here though it is quite out of data at this point.

[OriginalGeoJSON](https://geojson.io/#data=data:text/x-url,https%3A%2F%2Fraw.githubusercontent.com%2Fmhamilt%2Fabsolute-roasters%2Frefs%2Fheads%2Fmain%2Fabsolute_roasters_geo.json)
  
Data from Companies House paints a different picture. This is every busniess who
ever registered as being a coffee seller or manufacturer. Dissolution dates only
go back as far as 2012, busniesses that closed before that time do not have their
data avilable.

[Companies House GeoJSON](https://geojson.io/#data=data:text/x-url,https%3A%2F%2Fraw.githubusercontent.com%2Fmhamilt%2Fabsolute-roasters%2Frefs%2Fheads%2Fmain%2Fsrc%2Fcompanies_house.geojson)

