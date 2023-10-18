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
        val = {"repr": repr(self), "score": self.score}
        return val

    @property
    def score(self) -> int:
        score = 0
        for one_score in self._score_per_type.values():
            score += sum(one_score)
        return score

    @property
    def this_round_summary(self) -> str:
        rep = "#####\n"
        rep += "# This rounds score:\n"
        for key, value in self._score_per_type.items():
            if value[-1] == 0:
                continue

            rep += f"# {key}: {value[-1]}\n"
        return rep

    @property
    def this_round_summary_values(self) -> dict:
        val = {}
        for key, value in self._score_per_type.items():
            val[key] = value[-1]
        return val

    def add_score(self, value: int, reason: str) -> None:
        if reason not in self._score_per_type:
            self._score_per_type[reason] = [0 for _ in range(self._round)]

        self._score_per_type[reason][-1] += value

    def new_round(self) -> None:
        self._round += 1
        for key in self._score_per_type:
            self._score_per_type[key].append(0)

    def _longest_str_in_keys(self):
        record = 0
        for key in self._score_per_type:
            if len(key) > record:
                record = len(key)
        return record
