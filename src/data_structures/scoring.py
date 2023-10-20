class Scoring:
    def __init__(self):
        self._round = 0
        self._score_per_type = {}

    def __int__(self) -> int:
        return self.score

    def __repr__(self) -> str:
        rep = ""
        col_len = 6
        name_len = self._longest_str_in_keys() + 3
        for key, value in self._score_per_type.items():
            rep += f"{key:<{name_len}}: "
            for i in value:
                rep += f"{i:<{col_len}}"
            rep += "\n"

        rep += f"{'Total':<{name_len}}: {self.score}"
        return rep

    @property
    def summary(self):
        """
        This returns both the score and the pretty print for the whole game.
        """
        val = {"repr": repr(self), "score": self.score}
        return val

    @property
    def score(self) -> int:
        """
        Returns the total score. (all creterias, all rounds)
        """
        score = 0
        for one_score in self._score_per_type.values():
            score += sum(one_score)
        return score

    @property
    def this_round_summary(self) -> str:
        """
        Pretty print values returned as a string
        """
        rep = "#####\n"
        rep += "# This rounds score:\n"
        for key, value in self._score_per_type.items():
            if value[-1] == 0:
                continue

            rep += f"# {key}: {value[-1]}\n"
        return rep

    @property
    def this_round_summary_values(self) -> dict:
        """
        Only values from this round returned
        """
        val = {}
        for key, value in self._score_per_type.items():
            val[key] = value[-1]
        return val

    def add_score(self, value: int, reason: str) -> None:
        """
        Adding score to this round, with a reason.
        """
        if reason not in self._score_per_type:
            self._score_per_type[reason] = [0 for _ in range(self._round)]

        self._score_per_type[reason][-1] += value

    def new_round(self) -> None:
        """
        This is just a counter for the rounds.
        """
        self._round += 1
        for key in self._score_per_type:
            self._score_per_type[key].append(0)

    def _longest_str_in_keys(self):
        record = 0
        for key in self._score_per_type:
            if len(key) > record:
                record = len(key)
        return record
