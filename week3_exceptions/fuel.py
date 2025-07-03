# Fuel Gauge — Prompts for a fraction and displays the fuel level as a percentage or as E/F for empty/full.

def main():
    capacity = 105
    while True:
        try:
            numText, denoText = input("Fraction: ").strip().split("/")
            if "." in numText or "." in denoText:
                raise ValueError
            numerator = int(numText)
            denominator = int(denoText)
            capacity = int((numerator / denominator)*100)
            if capacity > 100:
                raise ValueError
            
        except (ValueError, ZeroDivisionError) :
            continue
        if capacity <= 1:
            print("E")
        elif capacity == 100:
            print("F")
        elif 1 < capacity < 100:    
            print(f"{capacity}%")
        break
    

if __name__ == "__main__":
    main()