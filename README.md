# GPT Custom QA

## Requirements

* Node.js
* React
* Next
* Docker

## Getting Started

1. Create an environment variable for your OpeanAI API key. This should live in a ```.env``` file in the root of the project directory.

2. Build the Docker image for the backend code and run the backend server container from the built image.

    ```cd backend```

    ```make build```

    ```make run-container```

3. Test that your container is running properly.

    ```make test```

4. Once you get a response from the server using ```make test```, run the Next.JS frontend app.

    ```cd frontend```
    ```make run-dev```

5. When you run the Next.JS project, a browser window will desplay and you can enter a question and get an answer.
