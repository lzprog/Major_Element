import time

def major_choice(vet, begin, finish):
    start_time = time.time()  # início da cronometragem da parte

    # Caso base
    if begin == finish:
        end_time = time.time()
        print(f"Tempo [{begin}:{finish}]: {end_time - start_time:.6f}s (base)")
        return vet[begin]

    if begin < finish:
        mid = (finish + begin) // 2

        left = major_choice(vet, begin, mid)
        right = major_choice(vet, mid + 1, finish)

        if left == right:
            end_time = time.time()
            print(f"Tempo [{begin}:{finish}]: {end_time - start_time:.6f}s (mesmo candidato: {left})")
            return left

        count_right = 0
        count_left = 0
        for i in range(begin, finish + 1):
            if vet[i] == left:
                count_left += 1
        for i in range(begin, finish + 1):
            if vet[i] == right:
                count_right += 1  

        end_time = time.time()
        print(f"Tempo [{begin}:{finish}]: {end_time - start_time:.6f}s (left: {count_left}, right: {count_right})")

        if count_left > (finish - begin + 1) // 2:
            return left
        elif count_right > (finish - begin + 1) // 2:
            return right
        else:
            return None

#teste
vetor = [1, 2, 1, 1, 3, 1, 4, 1]
start_total = time.time()
result = major_choice(vetor, 0, len(vetor)-1)
end_total = time.time()

print(f"\nResultado final: {result}")
print(f"Tempo total de execução: {end_total - start_total:.6f}s")
