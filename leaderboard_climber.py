def leader_board():
    user: str = "g964"
    user_score: int = 36097
    your_score: int = 20000
    if your_score > user_score:
        print("Winning")
    if your_score == user_score:
        print("Only need one")
    diff = user_score - your_score
    beta_kata = int(diff / 3)
    eight_kyu_kata = int(diff % 3)
    sum_up = beta_kata + eight_kyu_kata
    if sum_up < 1000:
        print("To beat " + user + "'s score, I must complete " + str(beta_kata) + " Beta kata and " + str(
            eight_kyu_kata) + " 8kyu kata.")

    else:
        print("To beat " + user + "'s score, I must complete " + str(beta_kata) + " Beta kata and " + str(
            eight_kyu_kata) + " 8kyu kata." + "Dammit")
