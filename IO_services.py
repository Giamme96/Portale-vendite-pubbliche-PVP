import pandas as pd

def compute_final_dfs(dfs_list : list) -> list:
    '''
    Compose the final output list, concat all the dfs in axis=0, return a list of dfs
    '''

    computed_dfs_list = []
    for macro_df in dfs_list:
        computed_dfs_list.append(pd.concat(macro_df, axis=0))

    return computed_dfs_list

def export_cumulative_excel(dfs_list : list) -> None:
    '''
    Export all the dfs in a Excel file, under Output folder
    '''
    sheet_name_list_annunci = ["Annunci", "Annuncio", "Allegati", "Eventi_significativi", "Pubblicità", "Soggetti", "Beni", "Allegati_bene", "Dati_catastali"]

    with pd.ExcelWriter("Output\Estrazione_pvp.xlsx") as writer:
        
        for df, sheet in zip(dfs_list, sheet_name_list_annunci):
            df.to_excel(writer, sheet_name=sheet, index=False)