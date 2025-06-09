def generate_traffic(event, context):
    import requests
    import random

    main_app_url = "http://service1-main-app"  # Replace with the actual service URL
    num_requests = random.randint(1, 10)  # Random number of requests to simulate traffic

    for _ in range(num_requests):
        response = requests.get(main_app_url)
        print(f"Request sent to {main_app_url}, response status: {response.status_code}")

    return {
        'statusCode': 200,
        'body': f"Generated {num_requests} requests to the main application."
    }