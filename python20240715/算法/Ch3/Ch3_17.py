count = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for x in range(1,7):
                if i < j and j < k and k < x:
                    count += 1
                    print(f"count:{count} : {i} {j} {k} {x}")
