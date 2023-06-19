## Fitfusion Backend

Backend application for FitFusion application and API.


## API Endpoints & HTTP Methods:



























https://fitfusion.herokuapp.com/api/v1/breakfast - GET

Response:

```
{
    "data": [
        {
            "_id": "6482ae98284d162283913333",
            "description": "Place the oats, chia seeds, maple syrup or honey, salt, and yogurt, if using, in a lidded container or jar.\nPour in the almond milk, and stir thoroughly to combine. Make sure that there are no chia seeds clumped around the bottom or sides of the jar!\nCover and store overnight, or for up to 5 days, in the fridge.",
            "img": "https://fitfusion.s3.us-west-1.amazonaws.com/overnight-oats.png",
            "ingredients": "Whole rolled oats – Also known as old fashioned oats. Quick oats and steel-cut oats will NOT work here. Quick oats will be too mushy, while steel-cut oats will be chewy and tough.\nChia seeds – For extra protein and the perfect thick and creamy texture.\nAlmond milk – Or any milk you like! Dairy milk and oat milk both work well. Coconut milk adds rich flavor and yields an especially creamy texture.\nMaple syrup – For sweetness. Honey works too.\nAnd a pinch of salt – To make the oats extra-flavorful.",
            "time": 15,
            "title": "Overnight Oats"
        }
    ],
    "message": "Successfully found 1 recipes",
    "status": 200
}

```

https://fitfusion.herokuapp.com/api/v1/breakfast/:id - GET

Response:

```

{
    "data": {
        "_id": "6482ae98284d162283913333",
        "description": "Place the oats, chia seeds, maple syrup or honey, salt, and yogurt, if using, in a lidded container or jar.\nPour in the almond milk, and stir thoroughly to combine. Make sure that there are no chia seeds clumped around the bottom or sides of the jar!\nCover and store overnight, or for up to 5 days, in the fridge.",
        "img": "https://fitfusion.s3.us-west-1.amazonaws.com/overnight-oats.png",
        "ingredients": "Whole rolled oats – Also known as old fashioned oats. Quick oats and steel-cut oats will NOT work here. Quick oats will be too mushy, while steel-cut oats will be chewy and tough.\nChia seeds – For extra protein and the perfect thick and creamy texture.\nAlmond milk – Or any milk you like! Dairy milk and oat milk both work well. Coconut milk adds rich flavor and yields an especially creamy texture.\nMaple syrup – For sweetness. Honey works too.\nAnd a pinch of salt – To make the oats extra-flavorful.",
        "time": 15,
        "title": "Overnight Oats"
    },
    "message": "Success!",
    "status": 200
}

```

https://fitfusion.herokuapp.com/api/v1/breakfast/:id - PUT

Response:

```

{
    "data": {
        "_id": "6482ae98284d162283913333",
        "description": "Place the oats, chia seeds, maple syrup or honey, salt, and yogurt, if using, in a lidded container or jar.\nPour in the almond milk, and stir thoroughly to combine. Make sure that there are no chia seeds clumped around the bottom or sides of the jar!\nCover and store overnight, or for up to 5 days, in the fridge.",
        "img": "https://fitfusion.s3.us-west-1.amazonaws.com/overnight-oats.png",
        "ingredients": "Whole rolled oats – Also known as old fashioned oats. Quick oats and steel-cut oats will NOT work here. Quick oats will be too mushy, while steel-cut oats will be chewy and tough.\nChia seeds – For extra protein and the perfect thick and creamy texture.\nAlmond milk – Or any milk you like! Dairy milk and oat milk both work well. Coconut milk adds rich flavor and yields an especially creamy texture.\nMaple syrup – For sweetness. Honey works too.\nAnd a pinch of salt – To make the oats extra-flavorful.",
        "time": 14,
        "title": "Overnight Oats"
    },
    "message": "Recipe has been successfully updated!",
    "status": 200
}

```

https://fitfusion.herokuapp.com/api/v1/breakfast - POST

Response:

```

{
    "data": {
        "description": "Place the oats, chia seeds, maple syrup or honey, salt, and yogurt, if using, in a lidded container or jar.\nPour in the almond milk, and stir thoroughly to combine. Make sure that there are no chia seeds clumped around the bottom or sides of the jar!\nCover and store overnight, or for up to 5 days, in the fridge.",
        "file": "",
        "ingredients": "Whole rolled oats – Also known as old fashioned oats. Quick oats and steel-cut oats will NOT work here. Quick oats will be too mushy, while steel-cut oats will be chewy and tough.\nChia seeds – For extra protein and the perfect thick and creamy texture.\nAlmond milk – Or any milk you like! Dairy milk and oat milk both work well. Coconut milk adds rich flavor and yields an especially creamy texture.\nMaple syrup – For sweetness. Honey works too.\nAnd a pinch of salt – To make the oats extra-flavorful",
        "time": 14,
        "title": "Overnight Oats"
    },
    "message": "Successfully created a recipe!",
    "status": 201
}

```


https://fitfusion.herokuapp.com/api/v1/breakfast/:id - DELETE

Response: 

```
{
    "data": {},
    "message": "Successfully deleted #1 recipe with id 64909f6b632b0a47bdb0c2f5",
    "status": 200
}

```

The following endpoints have identival responses and HTTP mathods available as the above.

https://fitfusion.herokuapp.com/api/v1/lunch
https://fitfusion.herokuapp.com/api/v1/dinner
https://fitfusion.herokuapp.com/api/v1/smoothies
https://fitfusion.herokuapp.com/api/v1/snacks
https://fitfusion.herokuapp.com/api/v1/desserts
https://fitfusion.herokuapp.com/api/v1/custom













