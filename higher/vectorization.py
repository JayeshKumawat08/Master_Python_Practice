import pandas as pd
import numpy as np
import time

def demonstrate_vectorization():
    # 1. Setup: Creating a massive simulated dataset (1 Million Rows)
    print("Generating 1,000,000 rows of transactional data...")
    df = pd.DataFrame({
        'customer_id': np.arange(1000000),
        'purchase_amount': np.random.uniform(10, 1000, 1000000),
        'account_age_years': np.random.randint(1, 10, 1000000)
    })

    # --- THE JUNIOR ANALYST WAY (Iteration / Apply) ---
    # Using .apply() acts like a hidden for-loop, processing row-by-row in native Python
    start_time = time.time()
    df['discount_slow'] = df.apply(
        lambda row: row['purchase_amount'] * 0.20 if row['account_age_years'] > 5 else 0, 
        axis=1
    )
    slow_time = time.time() - start_time

    # --- THE TOP 1% ML ENGINEER WAY (NumPy Vectorization) ---
    # np.where(condition, value_if_true, value_if_false) processes the whole array in C
    start_time = time.time()
    df['discount_fast'] = np.where(
        df['account_age_years'] > 5, 
        df['purchase_amount'] * 0.20, 
        0
    )
    fast_time = time.time() - start_time

    print(f"Junior .apply() Method took: {slow_time:.4f} seconds")
    print(f"Senior np.where() Method took: {fast_time:.4f} seconds")
    
    # In most environments, np.where is 100x to 400x faster than .apply()
    print(f"Performance Upgrade: Vectorization is {slow_time/fast_time:.1f}x faster!")

if __name__ == "__main__":
    demonstrate_vectorization()