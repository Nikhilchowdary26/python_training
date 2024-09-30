from collections import deque

queue=deque([])
queue.append(1)
queue.append(2)
queue.appendleft(3)
print(queue)
queue.popleft()
print(queue)
queue.clear()
if not queue:
    print('Empty')