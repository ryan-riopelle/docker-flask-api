# Docker Flask API template 🐳

<!-- Project description -->
This repository aims to be an easy to extend template for building a Python API using Flask and running it with only Python or using Docker, Docker-Compose, and Makefile.

## Prerequisities

Before you begin, ensure you have met the following requirements:

#### For Docker usage:
* You have a _Windows/Linux/Mac_ machine with the latest version of [Docker](https://www.docker.com/) installed.

Version Check:
```bash
docker -v
```

#### For docker-compose

Install Steps:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.11.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Version Check:
```bash
docker-compose -v
```

#### For Makefile

Install Steps For Mac if brew is already installed (google it for windows/linux):
```bash
brew install make
```

Version Check:
```bash
make --version
```

## Install/Run with Docker

If you want to install the dependencies and work using Docker, you can simply follow this steps. If you want to simply work locally using only Python, jump back to the "[Install/Run with only Python](https://github.com/RodolfoFerro/docker-flask-api#installrun-with-only-python)" section.

Clone the project repository:
```bash
git clone https://github.com/ryan-riopelle/docker-flask-api.git
cd docker-flask-api
```

Using `Makefile with Docker-Compose`:
```bash
$ make startdevenv
````

Now you should be able to test the API at <http://localhost:5001/>.

View docker containers:
```bash
$ docker ps
```

Login to docker containers:
```bash
$ docker exec -it <container_name or container_id> /bin/bash
```

To stop the Docker containers:
```bash
$ make stopdevenv
```

Sending Test Request To API
```bash
$ curl --request GET \
  --url http://localhost:5001/home
```
Response
```
Its Taco Time!
```

Sending Get Request To API With Parameters
```bash
$ curl --request GET \
  --url 'http://localhost:5001/get_menu_items?item_type=food&keyword_search=burrito&names_only=false'
```
Response
```bash
{
  "category": "success",
  "data": [
    "7-Layer Burrito",
    "Bean Burrito",
    "Beefy 5-Layer Burrito",
    "Beefy Fritos® Burrito",
    "Black Bean Burrito",
    "Burrito Supreme® - Beef",
    "Burrito Supreme® - Chicken",
    "Burrito Supreme® - Steak",
    "Cheesy Bean & Rice Burrito",
    "Cheesy Burrito - Bacon",
    "Cheesy Burrito - Bacon - Fresco Style",
    "Cheesy Burrito - Sausage",
    "Cheesy Burrito - Sausage - Fresco Style",
    "Cheesy Burrito - Steak",
    "Cheesy Burrito - Steak - Fresco Style",
    "Cheesy Potato Burrito",
    "Chili Cheese Burrito (regional)",
    "Combo Burrito",
    "Fresco Bean Burrito",
    "Fresco Burrito Supreme® - Chicken",
    "Fresco Burrito Supreme® - Steak",
    "Grande Scrambler Burrito - Bacon",
    "Grande Scrambler Burrito - Sausage",
    "Grande Scrambler Burrito - Steak",
    "Grilled Breakfast Burrito - Bacon",
    "Grilled Breakfast Burrito - Fiesta Potato",
    "Grilled Breakfast Burrito - Sausage",
    "Power Menu Burrito - Chicken",
    "Power Menu Burrito - Steak",
    "Power Menu Burrito - Veggie",
    "Shredded Chicken Burrito",
    "Smothered Burrito - Beef",
    "Smothered Burrito - Shredded Chicken",
    "Smothered Burrito - Steak",
    "XXL Grilled Stuft Burrito - Beef",
    "XXL Grilled Stuft Burrito - Chicken",
    "XXL Grilled Stuft Burrito - Steak"
  ],
  "status": 200
}
```

Sending Get Request To API With Parameters
```bash
$ curl --request GET \
  --url 'http://localhost:5001/get_item_by_health_indicator?item_type=food&keyword_search=taco&indicator=calories&='
```

Response
```bash
{
  "category": "success",
  "data": {
    "Carbohydrates": 13,
    "calories": 140,
    "caloriesFromFat": 70,
    "cholesterol": 15,
    "cost": 1.19,
    "dietaryFiber": 3,
    "name": "Fresco Crunchy Taco - Beef",
    "protein": 6,
    "saturatedFat": 2,
    "sodium": 300,
    "sugars": 1,
    "totalFat": 7,
    "transFat": 0
  },
  "status": 200
}
```



Got the data from 
https://github.com/jontonsoup4/taco-bell-as-a-service