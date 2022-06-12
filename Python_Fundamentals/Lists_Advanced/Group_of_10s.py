def sorter(nums):
    boundary = 10
    old_boundary = 0
    while True:
        list_of_numbers = []
        if max(nums) % 10 == 0:
            end_loop = (max(nums) // 10) * 10
        else:
            end_loop = (max(nums) // 10 + 1) * 10

        for number in nums:
            if old_boundary < number <= boundary:
                list_of_numbers.append(number)
                # nums.remove(number)
        print(f"Group of {boundary}\'s: {list_of_numbers}")
        old_boundary = boundary
        boundary += 10

        if old_boundary == end_loop:
            break


num_as_str = input().split(', ')
num_as_int = [int(i) for i in num_as_str]
sorter(num_as_int)
