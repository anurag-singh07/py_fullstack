import pandas as pd

class Analyzer:
    def __init__(self, db_manager):
        self.db = db_manager

    def get_dataframe(self):
        data = self.db.fetch_all()
        df = pd.DataFrame(data, columns=["id", "name", "price", "rating", "link"])

        # 🔥 IMPORTANT: convert to numeric (fix hidden bugs)
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

        return df

    def cheapest_product(self):
        df = self.get_dataframe()
        if df.empty:
            return {}
        row = df.loc[df["price"].idxmin()]
        return row.to_dict()

    def highest_rated(self):
        df = self.get_dataframe()
        if df.empty:
            return {}
        row = df.loc[df["rating"].idxmax()]
        return row.to_dict()

    def avg_price(self):
        df = self.get_dataframe()
        if df.empty:
            return 0
        return float(df["price"].mean())

    def top_5_cheapest(self):
        df = self.get_dataframe()
        if df.empty:
            return []
        return df.sort_values("price").head(5).to_dict(orient="records")
    #hello
    