# Mystery Secrets

A simple Flask web service that reveals top secrets one by one via an API endpoint.

## Features

- Serves secrets at `/secret` endpoint.
- Returns a new secret each time until all are revealed.

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```sh
   python sever.py
   ```

   Or, if deploying with a platform that uses a `Procfile`:
   ```sh
   web: python server.py
   ```

## Usage

- Access `http://localhost:5000/secret` in your browser or via `curl`:
  ```sh
  curl http://localhost:5000/secret
  ```

## Files

- `sever.py`: Main Flask application ([sever.py](sever.py))
- `requirements.txt`: Python dependencies ([requirements.txt](requirements.txt))
- `Procfile`: Process type declaration for deployment ([Procfile](Procfile))

## License

MIT
