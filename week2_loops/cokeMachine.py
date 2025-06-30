# Coke Machine — Simulates a vending machine that accepts coins and returns change after reaching 50 cents.

def main():
    amount = 50
    

    while amount > 0:
        
        print(f"Amount due: {amount}")
        coin = int(input("Insert coin: "))
        
        if coin == 25 or coin == 10 or coin == 5:
            amount -= coin
    
    print(f"Change owed: {0-amount}")
        




main()