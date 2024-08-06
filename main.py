import IO_services as IO
from bulk_request_services import run_bulk_request
from specific_annuncio_request_services import run_cycle_annuncio_in_annunci

#Set key params
request_annunci_size : int = 50

df_annunci = run_bulk_request(request_annunci_size)

dfs_annunci_list, dfs_esperimenti_list = run_cycle_annuncio_in_annunci(df_annunci)

computed_dfs_list = IO.compute_final_dfs(dfs_annunci_list, dfs_esperimenti_list)
dfs_output_list = [df_annunci] + computed_dfs_list

IO.export_cumulative_excel(dfs_output_list)


print("End")