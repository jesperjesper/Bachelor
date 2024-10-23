import json
import pytest

@pytest.fixture(scope="module")
def log_data():
    #Fixture to load log data from a JSON file.
    log_file_path = "logs/clean_logs.json"
    with open(log_file_path, "r") as f:
        return json.load(f)

def test_log_entry_presence(log_data): 
    #Test to verify the presence of a log entry with specific details.
    # Expected details in the log entry, excluding the timestamp (for testing reasons)
    expected_entry = {
        "alert": "Suspicious activity detected - Testing123 Message on Port 9999",
        "source_ip": "10.229.1.255",
        "source_port": 20,
        "destination_ip": "10.5.0.9",
        "destination_port": 9999
    }

    # Iterate over each entry in the loaded log data
    for entry in log_data:
        # Check if the current entry matches all the expected details
        if all(entry.get(key) == value for key, value in expected_entry.items()):
            break  # A matching entry was found, exit the loop
    else:
        # If no matching entry was found after checking all entries, fail the test
        pytest.fail("No log entry matches the specified criteria.")
