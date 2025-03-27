for x in range(26):
    y = x + ord("A")
    l = chr(y)
    with open(f"{l}.txt", "w") as file:
        file.write(f"Just {l}.txt file")
    