import heapq
import random

def calculate(heap):
  res_ar = []
  result = 0
  heapq.heapify(heap)
  while len(heap) > 1:
    elem1 = heapq.heappop(heap)
    elem2 = heapq.heappop(heap)
    sum = elem1 + elem2
    res_ar.append(sum)
    heapq.heappush(heap, sum)
    print("heap", heap)
  print("\nResults array", res_ar)
 
  for i in res_ar:
    result += i
  return result

def main():
  nums = [random.randint(1, 20) for _ in range(10)]
  nums = [3,6,12,19,19]
  print ("\n\nStart array:", nums, '\n')

  print("\nResult: ", calculate(nums), '\n')

if __name__ == "__main__":
    main()