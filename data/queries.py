import pandas as pd
from data.db_connection import get_connection



def get_vehicle_data(camera_name, start_time, end_time):
    query = """
    SELECT CameraName as Camera, Time as 'Data/Hora', Type, SUM(Value) AS Count
    FROM CitilogMeasures
    WHERE CameraName = ?
      AND Time BETWEEN ? AND ?
      AND Type IN ('C1', 'C2', 'C3')
    GROUP BY CameraName, Time, Type    
    ORDER BY Time;
    """

    conn = get_connection()
    df = pd.read_sql(query, conn, params=(camera_name, start_time, end_time))
    conn.close()
    return df

def get_camera_list():
    query = """
        SELECT DISTINCT CameraName 
        FROM CitilogMeasures 
        ORDER BY CameraName;
    """

    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df['CameraName'].tolist()