import random

# Function to generate a random game character name

def generate_character_name():
    prefixes = ['Brave', 'Cunning', 'Wise', 'Fierce']
    suffixes = ['Knight', 'Mage', 'Warrior', 'Rogue']
    return random.choice(prefixes) + ' ' + random.choice(suffixes)

# Function to calculate damage dealt in a game

def calculate_damage(base_damage, critical_hit=False,
                     damage_multiplier=1.0):
    if critical_hit:
        return base_damage * 2 * damage_multiplier
    return base_damage * damage_multiplier

# Function to check if a player has enough resources

def has_sufficient_resources(player_resources, required_resources):
    for resource, amount in required_resources.items():
        if player_resources.get(resource, 0) < amount:
            return False
    return True

# Function to log player actions

def log_action(player_name, action):
    print(f'{player_name} performed action: {action}')