def optimize_prompt(base_prompt, reward):
    if reward < 0:
        return base_prompt + "\nPlease answer more clearly, concisely, and with examples."
    elif reward > 0:
        return base_prompt + "\nKeep this style of explanation."
    return base_prompt


