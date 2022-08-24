"""
File for storing references to datasets.
"""
from typing import List

from openmapflow.datasets import geowiki_landcover_2017
from openmapflow.labeled_dataset import LabeledDataset, create_datasets

from openmapflow.labeled_dataset_custom import CustomLabeledDataset
from openmapflow.raw_labels import RawLabels

datasets: List[LabeledDataset] = [
    geowiki_landcover_2017,
    CustomLabeledDataset(
       dataset="Kenya_Western_2020",
       country="Kenya",
       raw_labels=(
           RawLabels(
               filename="ceo-Kenya-Western-Feb-2020---Feb-2021-(Set-1)-sample-data-2022-08-24.csv",
               class_prob=lambda df: (df["Does this pixel contain active cropland?"] == "Crop"),
               start_year=2020,
               train_val_test=(0.0, 0.5, 0.5),
               latitude_col="lat",
               longitude_col="lon",
           ),
           RawLabels(
               filename="ceo-Kenya-Western-Feb-2020---Feb-2021-(Set-2)-sample-data-2022-08-24.csv",
               class_prob=lambda df: (df["Does this pixel contain active cropland?"] == "Crop"),
               start_year=2020,
               train_val_test=(0.0, 0.5, 0.5),
               latitude_col="lat",
               longitude_col="lon",
           ),
       ),
   ),

]

if __name__ == "__main__":
    create_datasets(datasets)
