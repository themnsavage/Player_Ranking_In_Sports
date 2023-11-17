from data_manager import Data_Manager


def main():
    file = "2022 MLB Player Stats - Batting.csv"
    data_manager = Data_Manager(file=file)
    data_manager.score_players()
    data_manager.graph_data_set()


if __name__ == "__main__":
    main()
