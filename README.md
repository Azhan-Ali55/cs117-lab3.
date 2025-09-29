# **Assembly Reflection:**

## **Question 1:** What did you notice about registers and instructions?

**Answer:** There are many things I noticed about registers and instructions in assembly, most prominent worth mentioning are

### **REGISTERS:**

1. mov al, 12 --> Puts 12 in 8-bit AL.
2. mov bl, 13 --> Puts 13 in 8-bit BL.
3. mul bl --> Multiplies AL \* BL.
4. ESI --> Holds the digit count.

### **INSTRUCTIONS:**

1. movzx eax, ax --> Extend result in AX into EAX.
2. add dl, '0' --> Converts remainder (0–9) into ASCII digit.
3. mul bl --> Multiplies AL \* BL.

## **Question 2:** How is coding in Assembly different from Python?

**Answer:** There are a lot of differences between Python and Assembly, because they are both completely different languages. The following are the most prominent

**Assembly** is a low level language which means it is a lot harder due to it being closer to computer language than to human language. It is also very cryptic
and one small mistake can crash the whole program. One advantage of using Assembly is that it is extremely fast due to it being very close to hardware of the computer.

**Python** is a high level language which means it is closer to human language and is therefore a lot easier to understand as humans. It is very close to english and therefore
is a lot easier to understand and than debug.Obviously, one disadvantage of this is that it is much slower than Assembly, because it is not close to the hardware of the computer.

## **Python Reflection:**

### **Question 1:** Why is Python easier/faster for building the same project?

**Answer:** Python is easier than Assembly because you just say one instruction and python handles all the low level details.On the other hand you have to tell Assembly each and every tiny detail for it to work which means writing a lot of code. Assembly doesn't have built in fuctions, whereas python has buillt in functions which makes life so much easier, for example print(), loops, functions and much more

### **Question 2:** Which features of Python help abstraction (variables, functions, loops)?

**Answer:** Variables, Functions, And Loops all help in abstraction. For example in python you do not need to declare variables you just say x = 10. For functions you just create groups and using def and reuse it. For loops we use For and While loops and then Python handles the rest of the work

| Feature          | Assembly Example | Python Example | Notes                                                          |
| ---------------- | ---------------- | -------------- | -------------------------------------------------------------- |
| Variable storage | Register (EAX)   | `x = 5`        | Python handles variable types and memory automatically         |
| Printing output  | `INT 21h`        | `print()`      | Python has built in functions, so no system calls needed       |
| Arithmetic       | `ADD AX, BX`     | `x + y`        | Python uses operators directly no register managment is needed |
