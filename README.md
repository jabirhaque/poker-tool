# Poker Tool

Poker Tool is a web application built using **Python (FastAPI)** for the backend and **React** for the frontend. The primary aim of the project is to provide statistical analytics to help poker players improve their decision-making during games.

## Current Features

- **Current Hand Odds Calculator**: This is the main feature of the app in its initial development stage. It takes the current game state (cards in hand, community cards, etc.) and calculates the probability of the player winning the hand.

## Planned Features

- **Expected Value (EV) Calculator**: This will extend the functionality of the odds calculator to focus on monetary outcomes. It will calculate the expected value of decisions based on potential winnings or losses.
- **Poker Hand Probabilities Table**: A table that lists the strongest hands in poker (e.g., royal flush, full house) along with the probability of each hand occurring.
- **Training Game**: A training tool aimed at helping players improve their understanding of probabilities in poker. It will likely include a competitive element, such as a scoreboard, to make the learning process engaging and challenging.

## Technologies Used

- **Backend**: Python (FastAPI)
- **Frontend**: React
- **Other**: (Include relevant tools or libraries as needed)

## Project Status

Poker Tool is currently in the early stages of development. The core feature — the **Current Hand Odds Calculator** — is functional, and we are actively working on implementing additional features.

## Getting Started

To run the project locally:

1. Clone the repository.
2. Install dependencies:
   - Backend: `pip install -r requirements.txt`
   - Frontend: `npm install`
3. Run the backend server:
   ```bash
   cd src
   uvicorn main:app --reload
4. Run the frontend:
   ```bash
   cd ui
   npm run dev
