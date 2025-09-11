

from collections import deque

def is_palindrome(word):
    # Step 1: Calculate length
    n = len(word)

    # Step 2: Create a deque
    dq = deque()

    # Step 3: Push characters into deque
    for ch in word:
        dq.append(ch)

    # Step 4, 5, 6: Compare characters from front and rear
    while len(dq) > 1:  # continue until deque size is 0 or 1
        front = dq.popleft()   # remove from front
        rear = dq.pop()        # remove from rear

        if front != rear:      # Step 7: check mismatch
            return False

    return True


# ----------- Driver Code -------------
word = input("Enter a string: ")

if is_palindrome(word):
    print(f" '{word}' is a Palindrome")
else:
    print(f" '{word}' is NOT a Palindrome")

