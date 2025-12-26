def compute_reward(rating):
    if rating >= 4:
        return 1.0      # very good
    elif rating == 3:
        return 0.5      # acceptable
    else:
        return -1.0     # bad
