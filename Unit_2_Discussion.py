damage = 100
#variable is used before the function started
print(f"Player has {damage} base damage")
critMultiplier = 2.0


# Define a function to calculate damage with critical hits
def dealCritDamage(critMultiplier, damageDealt):
    # LOCAL VARIABLE
    totalDamage = damageDealt
    totalDamage = damageDealt * critMultiplier
    return totalDamage

# Call the function
damage = dealCritDamage(2.0, 100)

# Calling final damage after crit calculation
print(f"Player has inflicted {damage} Crit Damage")  # This will result in a NameError