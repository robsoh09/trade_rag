def check_columns(expected_set, captured_set):
    """
    Check whether the captured DataFrame columns match the expected columns.
    Returns a status plus missing and extra columns.
    """

    missing_cols = list(expected_set - captured_set) #detect missing columns and return as list / column type output 
    extra_cols = list(captured_set - expected_set)

    is_valid = len(missing_cols) == 0 and len(extra_cols) == 0 #defaults to True 
    #if len(missing_cols) == 0 and len(extra_cols) == 0 
    #    is_valid = True 
    #else: 
    #    is_valid = False

    return is_valid, missing_cols, extra_cols

