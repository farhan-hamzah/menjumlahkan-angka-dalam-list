nums = list(map(int, input("Masukan Array: ").split()))
hasil = 0
for i in range(len(nums)):
    hasil = hasil + nums[i]
print(hasil)