Bro, this is a Solidity practical examination question. I'll give you the complete practical: **theory, Solidity program, explanation, deployment procedure, and gas/transaction fee observation.**

We'll use **Remix IDE with the Ethereum Virtual Machine (JavaScript VM)** to write, compile, and deploy the smart contract. You don't need real ETH to practise deployment.

# Practical: Student Data Management Using Solidity

## 1. Aim

To write and deploy a Solidity smart contract to create and manage student data using the following constructs:

1. Structures (`struct`)
2. Arrays
3. Fallback function

Also, observe the gas consumption and transaction fee during smart contract deployment and execution.

## 2. Theory

### A. Introduction to Solidity

Solidity is a high-level, object-oriented programming language used to develop smart contracts on blockchain platforms such as Ethereum.

- It is statically typed.
- It supports inheritance, structures, arrays, and functions.
- Solidity programs are compiled into EVM bytecode.
- Smart contracts are deployed on the Ethereum blockchain.
- Once deployed, contract code cannot normally be modified.

### B. Structure (struct)

A structure is a user-defined data type that allows us to group multiple variables of different data types under a single name.

In this practical, we use a structure to store student information.

Example:

```
struct Student {
    uint rollNo;
    string name;
    uint marks;
}
```

Here:

- `rollNo` stores the student's roll number.
- `name` stores the student's name.
- `marks` stores the student's marks.

### C. Arrays

An array is a collection of elements of the same data type.

Solidity supports two major types of arrays:

1. Fixed-size arrays: Their size is declared in advance.
2. Dynamic arrays: Their size can increase or decrease during execution.

In this practical, we use a dynamic array to store multiple student records.

Example:

```
Student[] public students;
```

The `push()` function adds a new student record to the array.

### D. Fallback Function

A fallback function is a special function in Solidity that is executed when:

- A contract receives Ether without any matching `receive()` function.
- A function call does not match any existing function in the contract.

Syntax:

```
fallback() external payable {
    // Statements
}
```

Important points:

- It must be declared `external`.
- It does not have a function name.
- It cannot return any value.
- It can be declared `payable` to accept Ether.
- Only one fallback function can exist in a contract.

**Note:** If a contract has a `receive()` function, receiving empty-calldata Ether normally invokes `receive()` instead of `fallback()`.

---

## 3. Solidity Program

(Complete practical code)

```

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student details
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    // Dynamic array to store students
    Student[] public students;

    // Function to add student details
    function addStudent(
        uint _rollNo,
        string memory _name,
        uint _marks
    ) public {
        students.push(
            Student(_rollNo, _name, _marks)
        );
    }

    // Function to get student details
    function getStudent(uint _index)
        public
        view
        returns (uint, string memory, uint)
    {
        Student memory s = students[_index];

        return (s.rollNo, s.name, s.marks);
    }

    // Function to get total number of students
    function getStudentCount()
        public
        view
        returns (uint)
    {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }
}
```

## 4. Explanation of the Program

Let's understand what each part does.

| Code                        | Purpose                                                |
| --------------------------- | ------------------------------------------------------ |
| `pragma solidity ^0.8.20;`  | Specifies the Solidity compiler version.               |
| `contract StudentData`      | Declares the smart contract.                           |
| `struct Student`            | Creates a structure for student information.           |
| `Student[] public students` | Creates a dynamic array of student records.            |
| `addStudent()`              | Adds student details to the array.                     |
| `students.push()`           | Inserts a new student record.                          |
| `getStudent()`              | Retrieves student details using the array index.       |
| `getStudentCount()`         | Returns the total number of students.                  |
| `fallback()`                | Handles unmatched function calls and can accept Ether. |

### How does the program work?

Suppose we add three students:

| Roll No. | Name  | Marks |
| -------- | ----- | ----- |
| 1        | Rahul | 85    |
| 2        | Priya | 90    |
| 3        | Amit  | 78    |

The `addStudent()` function inserts these records into the dynamic array.

The `getStudent(0)` function retrieves the first student's details.

Remember: Solidity arrays use zero-based indexing.

Therefore:

- Index 0 → Rahul
- Index 1 → Priya
- Index 2 → Amit

---

## 5. Deployment Procedure Using Remix IDE

Follow these steps during your practical examination.

**Step 1: Open Remix IDE**

Visit Remix IDE.

**Step 2: Create a Solidity file**

1. Open the File Explorer.
2. Create a new file named `StudentData.sol`.
3. Paste the above Solidity program.

**Step 3: Compile the contract**

1. Open the Solidity Compiler tab.
2. Select compiler version `0.8.20` or a compatible 0.8.x version.
3. Click on Compile StudentData.sol.
4. Check that there are no compilation errors.

**Step 4: Deploy the contract**

1. Open the Deploy & Run Transactions tab.
2. Select Environment: `Remix VM (Cancun)` or another available Remix VM.
3. Select the `StudentData` contract.
4. Click Deploy.

The contract will appear under Deployed Contracts.

**Step 5: Add student details**

Expand the deployed contract.

Enter the following details in `addStudent`:

```
Roll No: 1
Name: Rahul
Marks: 85
```

Click the transaction button.

Repeat for other students.

**Step 6: Retrieve student details**

- Enter `0` in `getStudent`.
- Click the button.
- The output will display the first student's details.

Click `getStudentCount` to see the total number of records.

**Step 7: Test the fallback function**

To test the fallback function:

1. Select a different account if needed.
2. Enter a small amount of Ether in the Value field.
3. Select Wei as the unit.
4. Use the low-level transaction interface to send a transaction with unmatched function calldata to the deployed contract.

The fallback function will execute.

---

## 6. Gas and Transaction Fee

This is an important part of your practical because the question specifically asks you to observe gas values and transaction fees.

### What is Gas in Ethereum?

Gas is the unit used to measure the computational effort required to execute operations on the Ethereum network.

Examples:

- Deploying a smart contract consumes gas.
- Adding student information consumes gas.
- Updating blockchain storage consumes gas.
- Reading data using a `view` function generally does not require an on-chain transaction.

### What is Gas Price?

Gas price is the amount of Ether paid per unit of gas.

It is generally expressed in Gwei.

\\[ 1\text{ Gwei}=10^{-9}\text{ ETH} \\]

### Transaction Fee Formula

\\[ \text{Transaction Fee} = \text{Gas Used}\times\text{Effective Gas Price} \\]

For example:

Suppose:

- Gas Used = 50,000
- Gas Price = 20 Gwei

Then:

\\[ 50,000\times20=1,000,000\text{ Gwei} \\]\\[ \text{Fee}=0.001\text{ ETH} \\]

This is an illustrative calculation, not an actual measurement from your deployment.

### Observation Table

Record the actual values displayed in Remix after executing each operation.

| Operation           | Gas Used       | Transaction Fee |
| ------------------- | -------------- | --------------- |
| Contract Deployment | Record value   | Record value    |
| Add Student 1       | Record value   | Record value    |
| Add Student 2       | Record value   | Record value    |
| Add Student 3       | Record value   | Record value    |
| Fallback Execution  | Record value   | Record value    |
| Get Student         | No transaction | 0 ETH on-chain  |

**Important:** The exact gas values depend on compiler settings, storage contents, EVM version and execution environment. Do not write invented gas measurements in your practical journal.

In Remix VM, you can observe gas used and transaction details in the transaction log. It is a simulated blockchain environment, so the displayed ETH fees are not real-world payments.

---

## 7. Advantages of Using Smart Contracts

1. **Transparency:** Student records stored on the blockchain can be verified.
2. **Security:** Blockchain provides cryptographic protection.
3. **Decentralization:** Data is maintained by a distributed network.
4. **Immutability:** Deployed contract code and confirmed blockchain records cannot ordinarily be altered.
5. **Automation:** Smart contracts execute predefined operations automatically.

## 8. Result

Thus, a Solidity smart contract was successfully created and deployed to manage student information using structures, dynamic arrays, and a fallback function.

Student records were added and retrieved successfully. Gas consumption and transaction fee values were observed during contract deployment and execution.

---

## 9. Viva Questions and Answers

**Q1. What is Solidity?**

Solidity is a high-level programming language used to write smart contracts on Ethereum.

**Q2. What is a smart contract?**

A smart contract is a self-executing program deployed on a blockchain that automatically executes predefined instructions.

**Q3. What is a structure in Solidity?**

A structure is a user-defined data type that groups multiple variables of different data types.

**Q4. What is a dynamic array?**

A dynamic array is an array whose size can change during program execution.

**Q5. What is the purpose of `push()`?**

The `push()` function adds a new element to the end of a dynamic array.

**Q6. What is a fallback function?**

A fallback function is a special external function executed when a call does not match any existing function or when Ether is received without a suitable receive function.

**Q7. What is gas?**

Gas measures the computational effort required to execute operations on Ethereum.

**Q8. What is Gwei?**

Gwei is a denomination of Ether used to express gas prices.

**Q9. Can we modify deployed smart contracts?**

Generally, deployed contract code is immutable. Modifications require deploying a new contract or using an upgradeable contract design.

**Q10. Why does adding student data consume gas?**

Because adding student information modifies blockchain storage, which requires computational and storage resources.

---

## One important practical tip

Remember these three lines. They're the heart of this entire program:

```
struct Student {
    uint rollNo;
    string name;
    uint marks;
}

Student[] public students;

students.push(Student(_rollNo, _name, _marks));
```

If you understand these three, you've understood how the student records are structured and stored.

I'd also like to help you prepare the actual Remix deployment and transaction-observation workflow so you can confidently demonstrate it to your examiner.
