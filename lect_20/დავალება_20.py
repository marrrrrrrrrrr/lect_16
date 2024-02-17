'''
1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList  კლასი რომლის კონსტრუქტორი მიიღებს Value პარამეტრს.
2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)
3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)
4. პითონის Stack.py ფაილში შექმენილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)

'''


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)



  def append(self, value):
    if not self.head:
      self.head = Node(value)
    else:
      current_node = self.head

      while current_node.next:
        current_node = current_node.next
      
      current_node.next = Node(value)
  
  
  def remove(self):
    if not self.head:
        raise ValueError("Linked list is empty")

    elif not self.head.next:
        self.head = None
    else:
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None


  def print_elements(self):
    if not self.head:
        print("Linked list is empty")
        return

    current_node = self.head

    while current_node:
      if current_node.next:
        print(f"{current_node.value}", end=' -> ')
      else:
        print(f"{current_node.value}")


      current_node = current_node.next



linked_list_1 = LinkedList(1)
linked_list_1.append(2)
linked_list_1.append(3)
linked_list_1.append(4)
linked_list_1.print_elements()

print("\nRemoving the last element:")    
linked_list_1.remove()
linked_list_1.print_elements()

print("\nAdding more elements:")
linked_list_1.append(5)
linked_list_1.append(6)
linked_list_1.append(7)
linked_list_1.print_elements()

print("\nRemoving last two elements:") 
linked_list_1.remove()
linked_list_1.remove()
linked_list_1.print_elements()

print("\nRemoving all elements:")
linked_list_1.remove()
linked_list_1.remove()
linked_list_1.remove()
linked_list_1.remove()
linked_list_1.print_elements()