def clean_df(attack, threshold_rows, threshold_columns):
 
    umbral_filas = len(attack.columns) * threshold_rows
    umbral_columnas = len(attack) * threshold_columns
    
    attack = attack.dropna(axis=0, thresh=umbral_filas)

    attack = attack.dropna(axis=1, thresh=umbral_columnas)

    return attack