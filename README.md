# Mystery Secrets

A simple Flask web service that reveals top secrets one by one via an API endpoint.  
This project is designed for the Model Deployment and Reproducibility course in the DSS program.

## Features

- Serves secrets at the `/secret` endpoint.
- Returns a new secret with each request until all are revealed.
- Easy to deploy and integrate into model deployment workflows.

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the server locally:**
   ```sh
   python server.py
   ```

3. **Deploy using a Procfile (for platforms like Heroku):**
   ```
   web: python server.py
   ```

## Usage

- Access secrets via:  
  `http://localhost:5000/secret`

- Example using `curl`:
  ```sh
  curl http://localhost:5000/secret
  ```

## Project Structure

- `server.py`: Main Flask application
- `requirements.txt`: Python dependencies
- `Procfile`: Deployment configuration

## License
