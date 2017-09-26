def pay(wage, hours):
    if hours > 40:
        return (hours - 40) * wage * 1.5 + (40 * wage)
    return hours * wage

print(pay(10, 35))
print(pay(10, 45))
