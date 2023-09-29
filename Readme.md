Certainly! Here's a `README.md` file that provides instructions on how to deploy the Player and Game Master servers using Docker and test the game:

````markdown
# Number Guessing Game Deployment with Docker

This project consists of two Python servers, a Player server, and a Game Master server, that play a number-guessing game with each other. You can deploy these servers using Docker and test the game.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game
```
````

## Build Docker Images

1. Navigate to the `Player` and `GameMaster` directories.

   ```bash
   cd Player
   ```

2. Build the Docker image for the Player server:

   ```bash
   docker build -t player-server .
   ```

3. Navigate to the `GameMaster` directory.

   ```bash
   cd ../GameMaster
   ```

4. Build the Docker image for the Game Master server:

   ```bash
   docker build -t game-master-server .
   ```

## Deploy Player and Game Master Servers

1. Start the Player server as a Docker container:

   ```bash
   docker run -d -p 5000:5000 --name player-container player-server
   ```

2. Start the Game Master server as a Docker container:

   ```bash
   docker run -d -p 5001:5001 --name game-master-container game-master-server
   ```

## Test the Game

Now that the Player and Game Master servers are running as Docker containers, you can test the game by making HTTP requests to their respective endpoints.

### Player Server

- Health Check:

  ```bash
  curl http://localhost:5000/health
  ```

- Hostname:

  ```bash
  curl http://localhost:5000/hostname
  ```

- Play the Game:

  ```bash
  curl http://localhost:5000/play
  ```

### Game Master Server

- Health Check:

  ```bash
  curl http://localhost:5001/health
  ```

- Start a New Game (replace `min_number` and `max_number` with desired values):

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"min_number": 1, "max_number": 1000}' http://localhost:5001/start_game
  ```

- Play a Game (replace `game_id` with the game ID obtained from the previous step):

  ```bash
  curl http://localhost:5001/play_game/<game_id>
  ```

## Cleanup

To stop and remove the Docker containers when you're done testing:

```bash
docker stop player-container game-master-container
docker rm player-container game-master-container
```

This concludes the deployment and testing of the Number Guessing Game using Docker. Enjoy watching the Player and Game Master servers play the game!

```

Replace `"https://github.com/yourusername/number-guessing-game.git"` with the actual URL of your Git repository. This `README.md` provides step-by-step instructions for deploying the servers and testing the game.
```
