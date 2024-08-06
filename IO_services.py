import pandas as pd

def compute_final_dfs(*dfs_list : list) -> list:
    '''
    Compose the final output list, "concat" all the dfs in a list
    '''

    computed_dfs_list = []
    for df in dfs_list:
        computed_dfs_list.append(pd.concat(df, axis=0))

    return computed_dfs_list

def export_cumulative_excel(dfs_list : list) -> None:
    '''
    Export all the dfs in a Excel file, under Output folder
    '''
    sheet_name_list_annunci = ["A_Annunci", "A_Annuncio", "A_Allegati", "A_Eventi_significativi", "A_Pubblicità", "A_Soggetti", "A_Beni", "A_Allegati_bene", "A_Dati_catastali"]
    sheet_name_list_esperimenti = ["E_Esperimento", "E_Altri_siti", "E_Allegati", "E_Eventi_significativi", "E_Pubblicità", "E_Soggetti", "E_Beni", "E_Allegati_bene", "E_Dati_catastali"]

    sheet_name_list = sheet_name_list_annunci + sheet_name_list_esperimenti

    with pd.ExcelWriter("Output\Estrazione_pvp.xlsx") as writer:
        
        for df, sheet in zip(dfs_list, sheet_name_list):
            df.to_excel(writer, sheet_name=sheet, index=False)