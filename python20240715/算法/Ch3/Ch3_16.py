for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if k == j or k == i:
                continue
            for x in range(1,5):
                if x == k or x == j or x == i:
                    continue
                print(f"{i}{j}{k}{x}")
