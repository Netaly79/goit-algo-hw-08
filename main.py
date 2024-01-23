import heapq
import random

def calculate(heap):
  res_ar = []
  result = 0
  heapq.heapify(heap)
  sum = heapq.heappop(heap)
  while len(heap) > 0:
    elem = heapq.heappop(heap)
    sum += elem
    res_ar.append(sum)
  print("\nResults array", res_ar)
  for i in res_ar:
    result += i
  return result

def main():
  nums = [random.randint(1, 20) for _ in range(10)]
  print ("\n\nStart array:", nums)

  print("\nResult: ", calculate(nums), '\n')

if __name__ == "__main__":
    main()