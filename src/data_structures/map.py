import pandas as pd
from collections import defaultdict


class Map:
    def __init__(self, deck_path: str) -> None:
        if deck_path == "":
            raise ValueError("Deck path cannot be empty.")

        self._places = self._create_map_from_deck(deck_path)
        self._visited_since_last_get = []

    @property
    def nr_of_visited_sites(self) -> int:
        counter = 0
        for _, places in self._places.items():
            for one_place in places:
                if one_place.is_visited:
                    counter += 1
        return counter

    @property
    def get_all_visited_sites(self) -> list[str]:
        visited_places = []
        for _, places in self._places.items():
            for one_place in places:
                if one_place.is_visited:
                    visited_places.append(one_place.name)
        return visited_places

    def get_visited_sites_since_last_get(self) -> list[str]:
        """
        This resets the counter for visited sites.
        """
        visited = self._visited_since_last_get
        self._visited_since_last_get = []
        return visited

    def get_completed_regions_not_taken(self, taken: list) -> list[str]:
        """
        This returns a list of all completed regions that are not taken.
        No side effects
        """
        completed_regions = []
        for region, places in self._places.items():
            if region in taken:
                continue

            if all(place.is_visited for place in places):
                completed_regions.append(region)
        return completed_regions

    def visit_site(self, site: str) -> None:
        for _, places in self._places.items():
            for one_place in places:
                if one_place.site == site:
                    if one_place.is_visited:
                        continue
                    self._visited_since_last_get.append(one_place.name)
                    one_place._is_visited = True

    def _create_map_from_deck(self, deck_path: str) -> dict:
        places = defaultdict(list)

        df = pd.read_csv(deck_path)
        card_data: list[dict] = df.to_dict(orient="records")

        for element in card_data:
            one_place = Places(element["site"], element["name"])
            places[element["region"]].append(one_place)

        return dict(places)


class Places:
    """
    This is a mockup of a site, it does not contain all the information of a site
    """

    def __init__(self, site: str, name: str, visited: bool = False):
        self.name = name
        self.site = site
        self._is_visited = visited

    @property
    def is_visited(self):
        return self._is_visited
