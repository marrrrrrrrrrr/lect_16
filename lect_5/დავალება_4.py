'''
1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

'''

st = input("Input string: ")
encoded_st = st.encode()
print(f"UTF-8 encoded representation of {st} is {encoded_st}")



'''
2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები.
ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'.
თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

'''

st = (input("Input string: ").strip().lower() + 'Python').replace('python', 'Python')
print(st)



'''
3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

'''

st = input("Input string: ")
st = st[:len(st)//2]
print(st)



'''
5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

'''

st = input("Input string: ")
encoded_st = st.encode('UTF-16')
print(f"UTF-16 encoded representation of {st} is {encoded_st}")
decoded_st = encoded_st.decode('UTF-16')
print(f"Decoded representation of {encoded_st} is {decoded_st}")