# Fitfusion Backend

Backend application for FitFusion application and API.

## Installation

Clone repository to your local machine and create a virtual environment. This can be done by running the following command:

```
python -m venv <your-env-name>
```

Activate the virtual environment
```
source <your-env-name>/bin/activate
```

Install the dependancies
```
pip install -r requirements.txt
```

Start application

```
python3 app.py
```


## API Endpoints & HTTP Methods:

https://fitfusion.herokuapp.com/api/v1/workout - GET

Reponse:

```JSON
{
    "data": [
        {
            "_id": "648158fb3aa4dd146875c420",
            "activity": "Full Body Workout",
            "calories": 400,
            "link": "https://www.youtube.com/embed/sM3c25BS1bY",
            "time": 30
        }
    ],
    "message": "Successfully found 1 workouts",
    "status": 200
}

```

https://fitfusion.herokuapp.com/api/v1/workout - POST

Response:

```JSON
{
    "data": {
        "activity": "Full Body Workout",
        "calories": 400,
        "link": "https://www.youtube.com/embed/sM3c25BS1bY",
        "time": 30
    },
    "message": "Successfully created a workout!",
    "status": 201
}

```

https://fitfusion.herokuapp.com/api/v1/workout/:id - PUT

Response:

```JSON
{
    "data": {
        "_id": "6490a343632b0a47bdb0c2f6",
        "activity": "Full Body Workout",
        "calories": 1400,
        "link": "https://www.youtube.com/embed/sM3c25BS1bY",
        "time": 30
    },
    "message": "wWorkout has been successfully updated!",
    "status": 200
}

```

https://fitfusion.herokuapp.com/api/v1/workout/:id - DELETE

Response:

```JSON
{
    "data": {},
    "message": "Successfully deleted #1 workout with id 6490a343632b0a47bdb0c2f6",
    "status": 200
}

```


https://fitfusion.herokuapp.com/api/v1/chat - POST

Response:

```JSON

{
    "data": "Hello there! How can I assist you today?",
    "message": "Received a response!",
    "status": 200
}

```

https://fitfusion.herokuapp.com/api/v1/breakfast - GET

Response:

```JSON
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

```JSON

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

```JSON

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

```JSON

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

```JSON
{
    "data": {},
    "message": "Successfully deleted #1 recipe with id 64909f6b632b0a47bdb0c2f5",
    "status": 200
}

```

The following endpoints have identical responses and HTTP methods available as the endpoint ```/breakfast```.

* https://fitfusion.herokuapp.com/api/v1/lunch
* https://fitfusion.herokuapp.com/api/v1/dinner
* https://fitfusion.herokuapp.com/api/v1/smoothies
* https://fitfusion.herokuapp.com/api/v1/snacks
* https://fitfusion.herokuapp.com/api/v1/desserts
* https://fitfusion.herokuapp.com/api/v1/form













