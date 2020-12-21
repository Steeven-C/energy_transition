import pandas as pd

# Lecture du fichier excel avec limitation du nombre de ligne
df = pd.read_excel(
    "data/WorldEnergyBalancesHighlights_final.xlsx",
    sheet_name="TimeSeries_1971-2019",
    skiprows=1,
    usecols="A:BB",
    engine="openpyxl",
)
df = df[:6048]

# regroupement des données pour n'avoir qu'une seule fois chaque valeurs puis regroupement de ses valeurs dans un tableau
unique_products = df.Product.unique()
products = pd.DataFrame({"name": unique_products})

unique_flows = df.Flow.unique()
flows = pd.DataFrame({"name": unique_flows})
