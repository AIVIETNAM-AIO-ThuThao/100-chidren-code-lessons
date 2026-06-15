a = [1, 2, 3, [4, 5]]
b = a.copy()
b.append([11, 12])
print(b)
print(f"a là {a}\n")
b.append((11, 12))
print(f"{b} và a gốc là {a}\n")
b.append({11, 12})
print(f"{b} và a gốc là {a}\n")