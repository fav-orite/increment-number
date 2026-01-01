import re

def extract_first_number(text):
    match = re.search(r'-?\d+', text)
    return int(match.group()) if match else None

def increment_first_number(text):
    def replace_func(match):
        return str(int(match.group()) + 1)
    
    #Only the first occurrence should be changed
    return re.sub(r'-?\d+', replace_func, text, count=1)

#Iteration amount can be adjusted here
maxiteration = 100

def numberchange():
    print("#" * 100)
    print("                                         Enter text block")
    print("                           The first detected number will be incremented by", maxiteration)
    print("#" * 100)

    outputs = []
    current_text = ""
    iteration_count = 0

    
    try:
        while iteration_count < maxiteration:
            if not current_text:
                user_input = input("> ")
                current_text = user_input
            else:
                first_number = extract_first_number(current_text)
                if first_number is not None:
                    new_text = increment_first_number(current_text)
                    current_text = new_text
                    outputs.append(new_text)
                    print(f"Result: {new_text}")
                else:
                    #No valid number
                    outputs.append(current_text)
                    print(f"No valid numbers found in {current_text}")

            iteration_count += 1

    except KeyboardInterrupt:
        print("\nInterrupted by user")

    #Save results
    with open('output.txt', 'w') as f:
        for output in outputs:
            f.write(output + '\n')

    print(f"\nSaved {len(outputs)} entries to output.txt")

if __name__ == "__main__":
    numberchange()