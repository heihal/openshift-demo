import os

def generate_traffic(event, context):
    import requests
    import random

    # Prioritize TARGET_URL from env, fallback to internal service name
    main_app_url = os.environ.get("TARGET_URL", "http://service1-main-app.hemhal-dev.svc.cluster.local:5000") 
    num_requests = random.randint(1, 10)  # Random number of requests to simulate traffic

    for _ in range(num_requests):
        response = requests.get(main_app_url)
        print(f"Request sent to {main_app_url}, response status: {response.status_code}")

    return {
        'statusCode': 200,
        'body': f"Generated {num_requests} requests to the main application."
    }
