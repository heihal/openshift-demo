# OpenShift Microservices Demo

This project demonstrates a microservices architecture using OpenShift with two Flask applications and a serverless function for traffic generation.

## Project Structure

```
openshift-microservices-demo
├── service1-main-app
│   ├── app.py                # Main Flask application
│   ├── templates
│   │   └── index.html        # Frontend for the main application
│   ├── requirements.txt       # Python dependencies for the main app
│   ├── Dockerfile             # Dockerfile for the main app
│   └── openshift
│       ├── deployment.yaml    # Deployment configuration for the main app
│       ├── service.yaml       # Service configuration for the main app
│       ├── route.yaml         # Route configuration for the main app
│       └── hpa.yaml           # Horizontal Pod Autoscaler for the main app
├── service2-message-app
│   ├── app.py                # Flask application for the second service
│   ├── requirements.txt       # Python dependencies for the second service
│   ├── Dockerfile             # Dockerfile for the second service
│   └── openshift
│       ├── deployment.yaml    # Deployment configuration for the second service
│       ├── service.yaml       # Service configuration for the second service
│       └── hpa.yaml           # Horizontal Pod Autoscaler for the second service
├── traffic-generator-func
│   ├── handler.py            # Serverless function for traffic generation
│   ├── requirements.txt       # Python dependencies for the traffic generator function
│   └── openshift
│       └── knative-service.yaml # Knative service configuration for the traffic generator
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd openshift-microservices-demo
   ```

2. **Build and Deploy Services**
   - Navigate to each service directory (`service1-main-app` and `service2-message-app`) and build the Docker images.
   - Deploy the applications to OpenShift using the provided YAML files in the `openshift` directories.

3. **Access the Main Application**
   - Use the route defined in `service1-main-app/openshift/route.yaml` to access the main application.

4. **Using the Application**
   - The main application displays a button that, when clicked, fetches a message from the second service.
   - The traffic generator function can be deployed to simulate user requests to the main application, triggering autoscaling.

## Usage Details

- The main application is built with Flask and serves a simple "Hello World" message.
- The second service responds with a message when called by the main application.
- The Horizontal Pod Autoscaler is configured for both services to scale based on traffic.
- The traffic generator function is designed to create load on the main application to test autoscaling behavior.

## License

This project is licensed under the MIT License.