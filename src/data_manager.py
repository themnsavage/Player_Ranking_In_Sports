import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Data_Manager:
    def __init__(self, file=None):
        self._data_set = self._clean_data_set(
            pd.read_csv(file, encoding="latin1", delimiter=";")
        )

    def get_data_set_columns(self):
        return self._data_set.columns

    def get_data_set_head(self):
        return self._data_set.head()

    def get_data_set(self):
        return self._data_set

    def _clean_data_set(self, data):
        # filter data set
        columns_to_select = ["Name", "HR", "RBI", "BA"]
        clean_data_set = data[columns_to_select]
        # handle duplicates
        clean_data_set = clean_data_set.drop_duplicates(subset=["Name"])
        # handle missing values
        clean_data_set = clean_data_set.dropna()

        return clean_data_set

    def score_players(self):
        weights = {
            "HR": 4,
            "RBI": 3,
            "BA": 6,
        }

        # Calculate weighted scores
        for stat in weights:
            self._data_set[f"{stat}_weighted"] = self._data_set[stat] * weights[stat]

        # Sum weighted scores to get a total performance score
        self._data_set["Total_Score"] = self._data_set[
            [f"{stat}_weighted" for stat in weights]
        ].sum(axis=1)

        # Rank players by total score
        self._data_set = self._data_set.sort_values(by="Total_Score", ascending=False)

    def graph_data_set(self):
        print("made it")
        columns_to_select = ["Name", "HR", "RBI", "BA", "Total_Score"]
        graph_df = self._data_set[columns_to_select]
        graph_df = graph_df.set_index("Name")
        # Create the heatmap
        plt.figure(figsize=(10, 10))
        sns.heatmap(graph_df.head(), annot=True, cmap="coolwarm", fmt=".2f")

        # save image
        plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")
