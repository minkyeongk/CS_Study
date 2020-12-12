# 파이썬은 라이브러리로 힙이 구현되어 있음
import heapq

# 리스트 생성 후에 그 리스트를 heapify 한다
# 최소힙 기본, 최대힙 해주려면 -곱해서 처리하고 나중에 뺄 때 다시 - 곱해주면 됨
# 힙 라이브러리의 메서드는 힙을 다 인자로 받는다
# 빈 리스트에 힙 규칙대로 삽입 삭제 > heaptify 안해도 된다
heap = [1, 2, 3, 4]
heapq.heapify(heap)

print(heap)
heapq.heappush(heap, 5)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappushpop(heap, 6))
print(heap)

for i in range(len(heap)):
    heap[i] = -heap[i]
heapq.heapify(heap)
print(heap)

# 힙 정렬: 힙에서 하나씩 뽑아서 넣어줌으로써 순서 정렬
result = []
for _ in range(len(heap)):
    result.append(heapq.heappop(heap))

print(result)



