import pandas as pd

DEVICES = [
    {"device_id":1,"device_name":"Android Phone","operating_system":"Android","device_category":"Mobile"},
    {"device_id":2,"device_name":"iPhone","operating_system":"iOS","device_category":"Mobile"},
    {"device_id":3,"device_name":"Android Tablet","operating_system":"Android","device_category":"Tablet"},
    {"device_id":4,"device_name":"iPad","operating_system":"iPadOS","device_category":"Tablet"},
    {"device_id":5,"device_name":"Windows Laptop","operating_system":"Windows","device_category":"Laptop"},
    {"device_id":6,"device_name":"MacBook","operating_system":"macOS","device_category":"Laptop"},
    {"device_id":7,"device_name":"Smart TV","operating_system":"Android TV","device_category":"TV"},
    {"device_id":8,"device_name":"Apple TV","operating_system":"tvOS","device_category":"TV"},
    {"device_id":9,"device_name":"Chromecast","operating_system":"Android TV","device_category":"Streaming Device"},
    {"device_id":10,"device_name":"Web Browser","operating_system":"Browser","device_category":"Web"}
]

if __name__ == "__main__":

    df = pd.DataFrame(DEVICES)

    print(df)

    df.to_csv("02_data/dim_devices.csv", index=False)

    print("\nDevices Generated Successfully!")