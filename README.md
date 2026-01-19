# Asteroids

A simple Asteroids-style arcade game. Pilot your ship through an asteroid field, dodge incoming rocks, and blast them to pieces.

## Features

- Player-controlled spaceship with basic movement
- Asteroids that drift across the screen
- Shoot projectiles to destroy asteroids
- Collision detection between ship, bullets, and asteroids
- Game over / restart behavior

> Note: This is a learning project, so the code is focused on clarity over polish.

## Technologies Used

- Python v3.13
- pygame v2.6.1
- `uv` for dependency and environment management

## Getting Started

### Prerequisites

- Python `3.13` installed (or let `uv` manage it automatically)
- `uv` installed ([installation instructions](https://docs.astral.sh/uv/getting-started/installation/))

### Install Dependencies

From the project root:

```bash
uv sync
```

This will:

- Create a virtual environment (if needed)
- Install pygame v2.6.1
- Pin everything to python = "3.13" as configured

## Running the Game

After uv sync completes, run:

```bash
source .venv/bin/activate # to activate the virtual environment; run `deactivate` to deactivate

uv run main.py
```

## How to Play

- Movement: W / A / S / D or arrow keys to move
- Shoot: Space to fire
- Quit: `Ctrl + C` in your terminal or close the window

### Objective

- Avoid colliding with asteroids
- Shoot asteroids to destroy them
- Survive as long as possible

## Possible Extensions

Some ideas for future improvements:

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

## License

This project is for educational purposes. You may adapt and reuse it as you like. Add a formal license (e.g. MIT) if needed.
