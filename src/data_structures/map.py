import pandas as pd
from collections import defaultdict


class Map:
    def __init__(self, deck_path: str) -> None:
        if deck_path == "":
            raise ValueError("Deck path cannot be empty.")

        self.places = self._create_map_from_deck(deck_path)

    @property
    def has_completed_any_region(self) -> bool:
        for _, places in self.places.items():
            all_visited = True
            for one_place in places:
                if not one_place.is_visited:
                    all_visited = False
            if all_visited:
                return True
        return False

    @property
    def nr_of_visited_places(self) -> int:
        counter = 0
        for _, places in self.places.items():
            for one_place in places:
                if one_place.is_visited:
                    counter += 1
        return counter

    @property
    def get_visited_places(self) -> list[str]:
        visited_places = []
        for _, places in self.places.items():
            for one_place in places:
                if one_place.is_visited:
                    visited_places.append(one_place.site)
        return visited_places

    def visit_place(self, site: str) -> None:
        for _, places in self.places.items():
            for one_place in places:
                if one_place.site == site:
                    one_place._is_visited = True

    def _create_map_from_deck(self, deck_path: str) -> dict:
        places = defaultdict(list)

        df = pd.read_csv(deck_path)
        card_data: list[dict] = df.to_dict(orient="records")

        for element in card_data:
            one_place = Places(element["site"])
            places[element["region"]].append(one_place)

        return dict(places)


class Places:
    def __init__(self, site: str, visited: bool = False):
        self.site = site
        self._is_visited = visited

    @property
    def is_visited(self):
        return self._is_visited
