guest_list = ["Ann marie", "Saintt", "Nyx", "Edna"]
for guest in guest_list:
    print(f"Dear {guest}, I would be delighted if you could join me for dinner.")
unable_to_attend = guest_list[1]
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner so;\n")

guest_list[1] = "Diva"

for guest in guest_list:
    print(f"Dear {guest}, I would be delighted if you could join me for dinner.")
