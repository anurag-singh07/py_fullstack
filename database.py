import pandas as pd
import os

FILE = "data.csv"

def load_data():
    # file exist check
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["name", "price", "source", "link"])
        df.to_csv(FILE, index=False)
        return df

    try:
        # SAFE CSV READ (fix parser error)
        df = pd.read_csv(FILE, engine="python", on_bad_lines="skip")
        return df

    except Exception as e:
        print("CSV Load Error:", e)

        # fallback empty df (app crash nahi hoga)
        return pd.DataFrame(columns=["name", "price", "source", "link"])


def save_data(new_data):
    """
    new_data = dict format:
    {
        "name": "",
        "price": "",
        "source": "",
        "link": ""
    }
    """
    df = load_data()
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    # clean save
    df.to_csv(FILE, index=False)