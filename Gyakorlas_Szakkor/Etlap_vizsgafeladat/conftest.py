def pytest_collection_modifyitems(config, items):
    for item in items:
        points = item.get_closest_marker("points")
        if points:
            item.user_properties.append(("points", points.args[0]))

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Summarize total points after all tests run."""
    total_points = 0
    earned_points = 0

    for report in terminalreporter.stats.get("passed", []):
        for prop in report.user_properties:
            if prop[0] == "points":
                earned_points += prop[1]
                total_points += prop[1]

    for report in terminalreporter.stats.get("failed", []):
        for prop in report.user_properties:
            if prop[0] == "points":
                total_points += prop[1]

    terminalreporter.write("\n===== Test Score Summary =====\n")
    terminalreporter.write(f"Total Earned Points: {earned_points}/{total_points}\n")
