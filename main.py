from extraction import extract_data
import analyze
import pandas as pd
from visualize import pie_chart, grades_histogram, scores_bargram

headers = ["Esito", "Es1", "Es2", "Es3"]

data = extract_data("test.pdf", headers)
data = analyze.clean_data(data)

#calcolo della percentuale di promossi / bocciati
pie_chart(["Promossi", "Bocciati"], analyze.pass_rate(data))
grades_histogram(data)

exercises_scores = {}
exercises_scores["Es1"] = (data["Es1"].mean(), data["Es1"].max())
exercises_scores["Es2"] = (data["Es2"].mean(), data["Es2"].max())
exercises_scores["Es3"] = (data["Es3"].mean(), data["Es3"].max())
scores_bargram(exercises_scores)