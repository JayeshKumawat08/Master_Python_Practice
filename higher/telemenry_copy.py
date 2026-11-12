raw_audit_log = {
    "store_location": "Bengaluru_Hub",
    "transactions": [1200, -450, 3400, -100, 5000]
}

def generate_clean_report(audit_data):
    # Create a safe working copy so we don't ruin the raw audit log
    report_data = audit_data.copy()
    
    # Replace negative numbers with 0
    for i in range(len(report_data["transactions"])):
        if report_data["transactions"][i] < 0:
            report_data["transactions"][i] = 0
            
    return report_data

cleaned_report = generate_clean_report(raw_audit_log)
print("Original Audit Log:", raw_audit_log["transactions"])
print("Cleaned Report:    ", cleaned_report["transactions"])