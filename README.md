# Weather API Testing

This repository contains scripts for testing a weather API using Python and Postman.

## Python Tests

### Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

### Running Python Tests

1. Set the `WEATHER_API_KEY` environment variable with your weather API key.

    ```bash
    export WEATHER_API_KEY=your_actual_api_key
    ```

2. Run the Python tests using pytest.

    ```bash
    pytest test_weather_api.py
    ```

## Postman Tests

### Prerequisites

- Postman

### Setup

1. Import the `weather.json` into Postman.

2. Create a Postman environment and set the following variables:

    - `WEATHER_API_KEY`: Your weather API key
    - `POSTMAN_ID`: Your Postman Collection ID

### Running Postman Tests

1. Open Postman and select the imported collection.

2. Set the environment to the one you created.

3. Run the collection.

## License

[MIT](https://github.com/krisztipely/weatherapi/blob/main/LICENSE) 2024, Krisztina-Ronkainen Lakner
