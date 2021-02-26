# Absolute Roasters


![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Noun_coffee_with_milk_2695655.svg/240px-Noun_coffee_with_milk_2695655.svg.png)

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
  "facebook_handle":  "facebook_handle",
  "instagram_handle": "instagram_handle",
  "twitter_handle":   "@twitterHandle",
}
```
