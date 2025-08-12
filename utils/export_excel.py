def export_to_excel(df, filename="relatorio.xlsx"):
    df.to_excel(filename, index=False, engine="openpyxl")
    return filename