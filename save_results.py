import csv

def save_results_to_csv(ip_counts, most_accessed, suspicious_activity):
    """
    Save analysis results to a CSV file.
    """
    try:
        with open("log_analysis_results.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            
            # Write Requests per IP
            writer.writerow(["IP Address", "Request Count"])
            writer.writerows(ip_counts)
            
            # Write Most Accessed Endpoint
            writer.writerow([])
            writer.writerow(["Most Frequently Accessed Endpoint"])
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow(most_accessed)
            
            # Write Suspicious Activity
            writer.writerow([])
            writer.writerow(["Suspicious Activity Detected"])
            writer.writerow(["IP Address", "Failed Login Attempts"])
            writer.writerows(suspicious_activity.items())
        
        # print("Results successfully saved to 'log_analysis_results.csv'.")
    
    except PermissionError:
        print("Error: Permission denied. Unable to write to 'log_analysis_results.csv'.")
    except FileNotFoundError:
        print("Error: The file path for 'log_analysis_results.csv' is invalid.")
    except Exception as e:
        print(f"An unexpected error occurred while saving to the CSV file: {e}")

# Test block (optional)
if __name__ == "__main__":
    ip_counts = [("192.168.1.1", 234), ("203.0.113.5", 187)]
    most_accessed = ("/home", 403)
    suspicious_activity = {"192.168.1.100": 56, "203.0.113.34": 12}
    save_results_to_csv(ip_counts, most_accessed, suspicious_activity)
