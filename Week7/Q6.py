# Take input
packet_ids = list(map(int, input("Enter packet IDs separated by space: ").split()))

# Create empty lists
low_priority = []   # Even IDs
high_priority = []  # Odd IDs

# Separate IDs
for packet in packet_ids:
    if packet % 2 == 0:
        low_priority.append(packet)
    else:
        high_priority.append(packet)

# Display result
print("Low Priority (Even IDs):", low_priority)
print("High Priority (Odd IDs):", high_priority)