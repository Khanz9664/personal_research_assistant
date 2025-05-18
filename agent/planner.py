def should_continue(task_results):
    """
    Determines whether the process should continue based on the number of task results.

    Parameters:
        task_results (list): A list containing the results of completed tasks.

    Returns:
        bool: True if fewer than 3 results exist (indicating more work is needed),
              False otherwise.
    """
    return len(task_results) < 3

