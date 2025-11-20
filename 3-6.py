guest_list = ["Ann marie", "Saintt", "Nyx", "Edna"]

for guest in guest_list:
    print(f"Dear {guest}, I would be delighted if you could join me for dinner.")

print("\nGood news! I found a bigger dinner table, so more guests can be invited.\n")

guest_list.insert(0, "Nikola")
guest_list.insert(3, "Isaac")
guest_list.append("Abel")

for guest in guest_list:
    print(f"Dear {guest}, I would be delighted if you could join me for dinner.")