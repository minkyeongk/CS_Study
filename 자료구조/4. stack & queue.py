# 스택: append, pop 으로 구현, 사이즈로 is empty 확인
import queue

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
print(stack.pop())
print(stack)
print(len(stack))

# queue: 리스트로 구현 가능, queue 라이브러리도 있긴 함
q = []
q.append(1)
q.append(2)
q.append(3)

print(q.pop(0), len(q))

Q = queue.Queue()
Q.put(1)        # put 함수로 삽입
Q.put(2)
Q.put(3)

print(Q.get(), Q.qsize())   # get 함수로 삭제

# 원형큐 : 사실 파이썬은 리스트 길이가 정해지지 않아서 필요 없기는 함
# 원래 원형큐를 쓰는 이유는 정적 할당으로 사이즈가 정해져 있을 때 full이 아닌데도 rear가 맨 뒤에
# 위치해서 full이라고 잘못 여겨지는 부분을 해결하기 위함 > 공간을 효율적으로 재활용하기 위해
# (rear+1) % arraysize == front 라면 배열이 포화상태인걸로 판단
print("원형큐")
q = []
front = rear = 0

q.append(1)
rear += 1
q.append(2)
rear += 1
q.append(3)
rear += 1

print(front, rear)  # 이론 상으로 0번째는 비워놓으니까
print(q[front])
front+=1
print(front, rear)

# 연결리스트 큐: 연결리스트 형태로 head와 tail 노드를 가진 큐
# 노드 생성해서 tail에 이어줌
# 큐가 비었으면 head = tail, 아니면 tail에 next 연결 후 tail 이동  





