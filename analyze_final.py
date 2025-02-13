import pandas as pd


def main():

    df = pd.read_csv("output_done.csv")

    dei = df[df["kind"] == "DEI"]
    scientific = df[df["kind"] == "Scientific"]

    scientific.dropna(subset=["award_amount"], inplace=True)

    print(f"Number of DEI grants: {len(dei)}")
    print(f"Number of scientific grants: {len(scientific)}")

    xd = {
        "DEI median award amount": dei["award_amount"].median(),
        "scientific median award amount": scientific["award_amount"].astype(float).median(),
        "DEI mean award amount": dei["award_amount"].mean(),
        "scientific mean award amount": scientific["award_amount"].astype(float).mean(),
        "DEI total award amount": dei["award_amount"].sum(),
        "scientific total award amount": scientific["award_amount"].sum(),
        "Global total award amount": df["award_amount"].sum(),
    }

    print(xd)


if __name__ == "__main__":
    main()
