import numpy as np

class PageRankEngine:
    def __init__(self, num_pages, damping_factor=0.85):
        self.N = num_pages
        # The damping factor (d) prevents Spider Traps and Dead Ends via random teleportation
        self.d = damping_factor
        
    def calculate_ranks(self, transition_matrix, iterations=20):
        # 1. Initialize everyone with an equal probability (1/N)
        current_ranks = np.ones(self.N) / self.N
        
        # 2. The Teleportation Matrix (1 - d) probability of jumping anywhere randomly
        teleport_matrix = np.ones((self.N, self.N)) / self.N
        
        # 3. The Google Matrix Formula
        google_matrix = (self.d * transition_matrix) + ((1 - self.d) * teleport_matrix)
        
        # 4. Power Iteration: Multiply the ranks by the matrix until they stabilize
        print("--- Starting Power Iteration ---")
        for i in range(iterations):
            current_ranks = np.dot(current_ranks, google_matrix)
            
        return current_ranks

# --- Execution Shield ---
if __name__ == "__main__":
    # The 3x3 Transition Matrix based on our University Scenario
    # Rows must sum to 1 (Row-normalized)
    M = np.array([
        [0.0,  0.5,  0.5],  # Home links to Library(50%) and Canvas(50%)
        [0.0,  0.0,  1.0],  # Library links ONLY to Canvas(100%)
        [0.5,  0.5,  0.0]   # Canvas links to Home(50%) and Library(50%)
    ])
    
    engine = PageRankEngine(num_pages=3, damping_factor=0.85)
    final_scores = engine.calculate_ranks(M, iterations=20)
    
    print("\n✅ Final PageRank Centrality Scores:")
    print(f"Home Page:   {final_scores[0]*100:.2f}%")
    print(f"Library:     {final_scores[1]*100:.2f}%")
    print(f"Canvas:      {final_scores[2]*100:.2f}%")