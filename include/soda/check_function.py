# include/soda/check_function.py

def run_soda_scan(project_root, scan_name, checks_subpath=None):
    """
    Function to run a Soda scan.
    
    Args:
        project_root (str): Root directory of the project.
        scan_name (str): Name of the Soda scan to execute.
        checks_subpath (str, optional): Subpath within the 'checks' directory for specific checks.
    
    Returns:
        int: Result code indicating success (0) or failure (non-zero).
        
    Raises:
        ValueError: If Soda scan execution fails.
    """
    from soda.scan import Scan

    print("Running Soda Scan ...")
    
    # Paths and configurations
    config_file = f"{project_root}/soda/configuration.yml"
    checks_path = f"{project_root}/soda/checks"
    
    if checks_subpath:
        checks_path += f"/{checks_subpath}"
    
    # Define the data source name
    data_source = "online_retail"
    
    # Initialize Soda scan
    scan = Scan()
    scan.set_verbose()
    scan.add_configuration_yaml_file(config_file)
    scan.set_data_source_name(data_source)
    scan.add_sodacl_yaml_files(checks_path)
    scan.set_scan_definition_name(scan_name)
    
    # Execute Soda scan
    result = scan.execute()
    print(scan.get_logs_text())
    
    # Check scan result
    if result != 0:
        raise ValueError('Soda Scan failed')
    
    return result