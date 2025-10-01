from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import numpy as np


class RandomForestModelClass:
    def __init__(self):
        self.dataset = pd.DataFrame()
        pass

    def trainData(self, SOFTfile=None):
        if not SOFTfile:
            SOFTfile = "trainingData/GDS2771.soft"

        print(self.getData(SOFTfile))

    def getData(self, SOFTfile):
        dataset = pd.DataFrame()
        with open(SOFTfile, "r") as file:
            currline = file.readline().strip()

            while currline != "!dataset_table_begin":
                currline = file.readline().strip()
                if currline[0] == '!' and currline != "!dataset_table_begin":
                    equalsIndex = currline.split("=")
                    dataset[equalsIndex[0][1:]] = equalsIndex[1]

        return dataset


if __name__ == "__main__":
    Model = RandomForestModelClass()
    check = input("wanna train the data? Y/n  ")
    if check.lower() == "y":
        print(Model.trainData())
