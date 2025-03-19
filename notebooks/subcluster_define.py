import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Dictionary of clusters
clusters = {
    'Cluster_0': ['ANH82019.1'],
    'Cluster_1': ['Burkholderia_xenovorans_YP_557005'],
    'Cluster_2': ['Neosartorya_fischeri_XP_001266691'],
    'Cluster_3': ['YP_432621.1_SAM-dependent_methyltransferase'],
    'Cluster_4': ['Algoriphagus_sp._ZP_01720187'],
    'Cluster_5': ['ZP_00987534.1_COG0500_SAM-dependent_methyltransferases'],
    'Cluster_6': ['Anaeromyxobacter_dehalogenans_YP_466408'],
    'Cluster_7': ['Polaribacter_irgensii_ZP_01117536'],
    'Cluster_8': ['3LCC_A'],
    'Cluster_9': ['YP_522685.1_thiopurine_S-methyltransferase']
}

notebook_filename = "SubCluster_histo_v2.ipynb"  # Change this to your actual notebook filename

# Load the notebook
with open(notebook_filename, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Identify the first cell
first_cell = notebook.cells[0]

# Iterate through each cluster and update parameters
for i, (cluster, seeds) in enumerate(clusters.items()):
    cluster_number = i
    seed_name = seeds[0]  # Assuming one seed per cluster
    
    # Update first cell content
    new_first_cell_content = f"""
cluster_number = {cluster_number}
seed_name = '{seed_name}'
""".strip()
    
    first_cell.source = new_first_cell_content
    
    # Save the updated notebook
    temp_notebook_filename = f"temp_notebook_{i}.ipynb"
    with open(temp_notebook_filename, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    
    # Execute the notebook
    with open(temp_notebook_filename, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': './'}})
    
    print(f"Execution complete for {cluster} (Cluster Number: {cluster_number}, Seed Name: {seed_name})")
