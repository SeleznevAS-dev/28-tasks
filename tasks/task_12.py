def MassVote(N: int, Votes: list[int]) -> str:
    sum_votes = sum(Votes)
    winners = {}
    for i in range(N):
        winners[i + 1] = round(Votes[i] / sum_votes, 3)

    winner1 = max(winners, key=winners.get)
    percent1 = winners.get(winner1)
    winners.pop(winner1)
    winner2 = max(winners, key=winners.get)
    percent2 = winners.get(winner2)
    final_winner = ""
    if percent1 == percent2:
        final_winner = "no winner"
    elif percent1 >= 0.5:
        final_winner = f"majority winner {winner1}"
    elif percent1 <= 0.5:
        final_winner = f"minority winner {winner1}"
    return final_winner

