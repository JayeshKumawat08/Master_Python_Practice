import sys

def heavy_list(limit):
    result = []
    for i in range(limit):
        result.append("Transaction_ID_{i}")
    return result

def transaction_stream(limit):
    current = 0
    while current < limit:
        yield f"Transaction_ID_{current}"
        current +=1

if __name__ == "__main__":
    limit = 100000

    print("\t\t\tMemory Profiling")
    heavy_data = heavy_list(limit)
    print(f"Memory used by standard List: {sys.getsizeof(heavy_data)} bytes")
    
    generator_data = transaction_stream(limit)
    print(f"Memory used by Generator:      {sys.getsizeof(generator_data)} bytes")
    
    print("\n\t\t\tProcessing the Stream")

    count = 0
    for transaction in transaction_stream(limit):
        print(f"Processing: {transaction}")
        count += 1
        if count == 5:
            break
            
    print("streaming successful.")