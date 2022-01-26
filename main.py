import pandas as pd
import vehicleProfile

def main():
    print("Main starting!")
    df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv")
    profile1 = vehicleProfile.VehicleProfile('08KY12345', '16-01-22', df)
    print(profile1)

if __name__ == "__main__":
    main()