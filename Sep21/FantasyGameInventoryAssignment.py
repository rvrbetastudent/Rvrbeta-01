from collections import Counter

def pluralize(item: str, count: int) -> str:
    """Return the pluralized form of an item name based on count."""
    if count > 1:
        if item.endswith('y') and not item.endswith('ey'):
            return item[:-1] + 'ies'
        return item + 's'
    return item

def display_inventory(inventory: dict[str, int]) -> None:
    """Print the inventory and total number of items."""
    print("Inventory:")
    for item, count in inventory.items():
        print(f"{count} {pluralize(item, count)}")
    print(f"Total number of items: {sum(inventory.values())}")

def add_to_inventory(inventory: dict[str, int], added_items: list[str]) -> None:
    """Add items from added_items to inventory."""
    loot_counts = Counter(added_items)
    for item, count in loot_counts.items():
        inventory[item] = inventory.get(item, 0) + count

def display_loot_summary(loot: list[str]) -> None:
    """Print a summary of loot gained."""
    loot_counts = Counter(loot)
    parts = [f"{count} {pluralize(item, count)}" for item, count in loot_counts.items()]
    print("Got " + " and ".join(parts) + "!")

def main() -> None:
    player = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    slime_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    display_loot_summary(slime_loot)
    add_to_inventory(player, slime_loot)
    display_inventory(player)

if __name__ == "__main__":
    main()