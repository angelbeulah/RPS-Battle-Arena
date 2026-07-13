from flask import Flask, session, render_template, request, url_for, redirect
import random

app = Flask(__name__)
app.secret_key = "rock,paper,scissors"

choices = ["rock", "paper", "scissors"]


def get_winner(user, computer):
    if user == computer:
        return "Draw!"

    if (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "User Wins!"
    else:
        return "Computer Wins!"


@app.route("/")
def home():
    if "wins" not in session:
        session["wins"] = 0
        session["losses"] = 0
        session["draws"] = 0

    total_games = (
        session["wins"]
        + session["losses"]
        + session["draws"]
    )

    if total_games > 0:
        win_rate = round((session["wins"] / total_games) * 100)
    else:
        win_rate = 0

    return render_template(
        "index.html",
        session=session,
        total_games=total_games,
        win_rate=win_rate,
    )


@app.route("/play", methods=["POST"])
def play():
    user_choice = request.form["choice"]
    computer_choice = random.choice(choices)

    winner = get_winner(user_choice, computer_choice)

    if winner == "User Wins!":
        session["wins"] += 1
    elif winner == "Computer Wins!":
        session["losses"] += 1
    else:
        session["draws"] += 1

    total_games = (
        session["wins"]
        + session["losses"]
        + session["draws"]
    )

    if total_games > 0:
        win_rate = round((session["wins"] / total_games) * 100)
    else:
        win_rate = 0

    return render_template(
        "results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner,
        session=session,
        total_games=total_games,
        win_rate=win_rate,
    )


@app.route("/reset")
def reset():
    session["wins"] = 0
    session["losses"] = 0
    session["draws"] = 0

    return redirect(url_for("home"))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)