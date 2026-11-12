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

import copy

raw_audit_log = {
    "store_location": "Bengaluru_Hub",
    "transactions": [1200, -450, 3400, -100, 5000]
}

def generate_clean_report(audit_data):
    # 1. The Fix: Deep Copy guarantees complete memory isolation for nested data
    report_data = copy.deepcopy(audit_data)
    
    # 2. The Top 1% Upgrade: A List Comprehension
    # Reads as: "Give me 0 if the transaction is less than 0, otherwise give me the transaction, for every transaction in the list."
    report_data["transactions"] = [0 if x < 0 else x for x in report_data["transactions"]]
            
    return report_data

cleaned_report = generate_clean_report(raw_audit_log)

print("Original Audit Log:", raw_audit_log["transactions"])
# Output: [1200, -450, 3400, -100, 5000] (Perfectly safe!)

print("Cleaned Report:    ", cleaned_report["transactions"])
# Output: [1200, 0, 3400, 0, 5000] (Cleaned successfully!)