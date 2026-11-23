import logging
import pandas as pd

def transform_weather_data(raw_json: dict, city: str) -> pd.DataFrame:
    records = []
    daily_forecasts = raw_json.get("weather", [])

    for day in daily_forecasts:
        date_str = day.get("date")
        for slot in day.get("hourly", []):
            #Convert "0", "300", "1200" into "00:00", "03:00", "12:00"
            raw_time = slot.get("time", "0").zfill(4)
            formatted_time = f"{raw_time[:2]}:{raw_time[2:]}"
            
            records.append({
                "recorded_at": pd.to_datetime(f"{date_str} {formatted_time}"),
                "city": city,
                "temperature_c": float(slot.get("tempC")),
                "humidity_pct": int(slot.get("humidity")),
                "wind_speed_kmh": float(slot.get("windspeedKmph")),
                "weather_desc": slot.get("weatherDesc", [{}])[0].get("value", "Unknown")
            })

    df = pd.DataFrame(records)

    #Data Cleaning and Quality Checks
    df.dropna(subset=["recorded_at", "temperature_c"], inplace=True)
    df.drop_duplicates(subset=["recorded_at", "city"], inplace=True)
    df["ingested_at"] = pd.Timestamp.utcnow()

    if df.empty:
        raise ValueError("Transformation resulted in an empty DataFrame.")

    logging.info(f"Transformed {len(df)} clean weather records for {city}.")
    return df
