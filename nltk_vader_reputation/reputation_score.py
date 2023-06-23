import pandas as pd
import networkx as nx

# Read the Bitcoin Twitter dataset into a pandas DataFrame
df = pd.read_csv('bitcoin_twitter.csv')

# Create an empty directed graph
G = nx.DiGraph()

# Add edges to the graph based on the user relationships in the dataset
for index, row in df.iterrows():
    user_name = row['user_name']
    user_followers = row['user_followers']
    user_verified = row['user_verified']
    G.add_edge(user_name, user_name, weight=user_followers)  # Self-edge with weight as user_followers
    if user_verified:
        G.nodes[user_name]['verified'] = True

# Set initial reputation score for all nodes as 1.0
for node in G.nodes:
    G.nodes[node]['reputation'] = 1.0

# Calculate reputation scores using the reputation_calculation function from the GitHub link
def reputation_calculation(G, damping_factor=0.85, max_iterations=100):
    for _ in range(max_iterations):
        convergence = True
        for node in G.nodes:
            reputation_score = 0.0
            for neighbor in G.predecessors(node):
                edge_weight = G.edges[neighbor, node]['weight']
                neighbor_reputation = G.nodes[neighbor]['reputation']
                reputation_score += neighbor_reputation * edge_weight
            if 'verified' in G.nodes[node] and G.nodes[node]['verified']:
                reputation_score += neighbor_reputation * 1.1  # Add Fij = 1.1 if user_verified is True
            reputation_score = damping_factor * reputation_score
            if abs(G.nodes[node]['reputation'] - reputation_score) > 0.0001:  # Convergence check
                convergence = False
            G.nodes[node]['reputation'] = reputation_score

        # Normalize the reputation scores using Min-Max scaling
        min_score = min(G.nodes[node]['reputation'] for node in G.nodes)
        max_score = max(G.nodes[node]['reputation'] for node in G.nodes)

        for node in G.nodes:
            reputation_score = G.nodes[node]['reputation']
            normalized_score = (reputation_score - min_score) / (max_score - min_score)
            G.nodes[node]['reputation'] = normalized_score + 1  # Add base value of 1 to reputation score

        if convergence:
            break

    return G

# Call the reputation_calculation function to calculate reputation scores
reputation_graph = reputation_calculation(G)

# Extract the reputation scores from the graph
reputation_dict = {node: reputation_graph.nodes[node]['reputation'] for node in reputation_graph.nodes}

# Create a DataFrame of user_name and reputation scores
reputation_df = pd.DataFrame(reputation_dict.items(), columns=['user_name', 'reputation'])

# Save the reputation DataFrame to a CSV file
reputation_df.to_csv('reputation_scores.csv', index=False)
