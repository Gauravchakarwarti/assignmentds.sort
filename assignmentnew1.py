# 1. Delete the elements in an linked list whose sum is equal to zero

# Solution:

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def delete_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    prefix_sum = 0
    sum_dict = {}

    while current:
        prefix_sum += current.value

        if prefix_sum in sum_dict:
           
            node = sum_dict[prefix_sum].next
            temp_sum = prefix_sum
            while node != current:
                temp_sum += node.value
                sum_dict.pop(temp_sum)
                node = node.next

          
            sum_dict[prefix_sum].next = current.next
        else:
            sum_dict[prefix_sum] = current

        current = current.next

    return dummy.next

def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


input_list = create_linked_list([-9, 9, 15, 5, -20, 7, -9])
result_list = delete_zero_sum_sublists(input_list)


while result_list:
    print(result_list.value, end=" -> ")
    result_list = result_list.next




#2. Reverse a linked list in groups of given size


# Solution:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_segment(start, end):
        prev = None
        current = start
        while current != end:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def get_kth_node(node, k):
        while k > 0 and node:
            node = node.next
            k -= 1
        return node

    if not head or k <= 1:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        group_end = get_kth_node(prev_group_end.next, k)
        if not group_end:
            break

        group_start = prev_group_end.next
        next_group_start = group_end.next

        group_end.next = None  

        
        prev_group_end.next = reverse_segment(group_start, group_end)
        group_start.next = next_group_start

       
        prev_group_end = group_start

    return dummy.next

if __name__ == "__main__":
   

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    k = 3
    new_head = reverse_k_group(head, k)

    
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next


#3. Merge a linked list into another linked list at alternate positions.


# Solution:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def merge_alternate(self, other_list):
        if not other_list.head:
            return

        current_self = self.head
        current_other = other_list.head

        while current_self and current_other:
            next_self = current_self.next
            next_other = current_other.next

            current_self.next = current_other
            current_other.next = next_self

            current_self = next_self
            current_other = next_other

        
        if current_other:
            current_self.next = current_other

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list2 = LinkedList()
    list2.append('A')
    list2.append('B')
    list2.append('C')
    list2.append('D')

    list1.merge_alternate(list2)

    list1.display()  


# 4. In an array, Count Pairs with given sum

# Solution:

def count_pairs_with_given_sum(arr, target_sum):
    num_freq = {}  
    count = 0

    for num in arr:
        required_sum = target_sum - num
        if required_sum in num_freq:
            count += num_freq[required_sum]

       
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1

    return count



if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    target_sum = 6
    result = count_pairs_with_given_sum(arr, target_sum)
    print(f"Number of pairs with sum {target_sum}: {result}")


# 5. Find duplicates in an array

# Solution:

def find_duplicates(arr):
    num_freq = {}  
    duplicates = []

    for num in arr:
        if num in num_freq:
            duplicates.append(num)
        else:
            num_freq[num] = 1

    return duplicates



if __name__ == "__main__":
    arr = [4, 3, 2, 7, 8, 2, 1, 4]
    duplicates = find_duplicates(arr)
    if duplicates:
        print("Duplicates found:", duplicates)
    else:
        print("No duplicates found.")


# 6. Find the Kth largest and Kth smallest number in an array

# Solution:

def find_kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k - 1]

def find_kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


if __name__ == "__main__":
    arr = [3, 1, 5, 4, 2, 6]
    k = 3

    kth_largest = find_kth_largest(arr, k)
    kth_smallest = find_kth_smallest(arr, k)

    print(f"{k}th largest number: {kth_largest}")
    print(f"{k}th smallest number: {kth_smallest}")


# 7. Move all the negative elements to one side of the array

# Solution:

def move_negatives_to_one_side(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1


if __name__ == "__main__":
    arr = [1, -2, -3, 4, -5, 6, -7]
    move_negatives_to_one_side(arr)
    print(arr) 


#8. Reverse a string using a stack data structure

# Solution:

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


if __name__ == "__main__":
    input_string = "Hello, World!"
    reversed_string = reverse_string(input_string)
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)


# 9. Evaluate a postfix expression using stack

# solution:

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def evaluate_postfix(expression):
    operators = set(['+', '-', '*', '/', '%'])  
    stack = Stack()

    for token in expression.split():
        if token not in operators:
            
            stack.push(int(token))
        else:
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '%':
                result = operand1 % operand2

            
            stack.push(result)

   
    return stack.peek()

:
if __name__ == "__main__":
    postfix_expression = "3 5 + 6 2 * -"
    result = evaluate_postfix(postfix_expression)
    print("Result:", result) 


# 10. Implement a queue using the stack data structure

# Solution:

class QueueUsingStack:
    def __init__(self):
        self.stack_enq = []  
        self.stack_deq = []  n

    def is_empty(self):
        return not self.stack_enq and not self.stack_deq

    def enqueue(self, item):
        self.stack_enq.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        if not self.stack_deq:
            while self.stack_enq:
                self.stack_deq.append(self.stack_enq.pop())

        return self.stack_deq.pop()

    def front(self):
        if self.is_empty():
            return None

        if not self.stack_deq:
            while self.stack_enq:
                self.stack_deq.append(self.stack_enq.pop())

        return self.stack_deq[-1]

    def size(self):
        return len(self.stack_enq) + len(self.stack_deq)



if __name__ == "__main__":
    queue = QueueUsingStack()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front of the queue:", queue.front())  
    print("Dequeue:", queue.dequeue())         
    print("Dequeue:", queue.dequeue())          

    queue.enqueue(4)
    print("Size of the queue:", queue.size())  
