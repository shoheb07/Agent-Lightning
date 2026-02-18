def reward_function(output: str, expected: str) -> float:
    """
    Simple reward logic.
    +1 for correct answer
    -1 for wrong answer
    """

    return 1.0 if output.strip().lower() == expected.strip().lower() else -1.0