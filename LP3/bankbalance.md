Bro, this practical is about creating a **Bank Account Smart Contract using Solidity**. We'll implement all three operations: deposit, withdraw, and check balance, then deploy the contract on an Ethereum test network.

# **Practical: Bank Account Management Using Solidity**

## **1. Aim**

To write and deploy a Solidity smart contract on an Ethereum test network to perform the following banking operations:

1. Deposit money.
2. Withdraw money.
3. Display account balance.

## **2. Theory**

### **A. Smart Contract**

A smart contract is a self-executing program stored on a blockchain. It automatically executes predefined instructions when users interact with it.

In Ethereum, smart contracts are written using Solidity.

### **B. Deposit Money**

- The deposit function allows customers to deposit Ether into their bank account.
- It uses the `payable` keyword to accept Ether.
- The deposited amount is added to the customer's balance.

### **C. Withdraw Money**

- The withdrawal function allows customers to withdraw Ether.
- It checks whether sufficient balance is available.
- If sufficient balance exists, the requested amount is transferred to the customer.

### **D. Show Balance**

- The balance function displays the current balance of the customer.
- It uses the `view` keyword because it only reads data and does not modify blockchain storage.

## **3. Solidity Program**

Complete practical solution

```

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    // Store customer balance
    mapping(address => uint) public balances;

    // Deposit money
    function deposit() public payable {
        require(msg.value > 0, "Amount must be greater than zero");

        balances[msg.sender] += msg.value;
    }

    // Withdraw money
    function withdraw(uint amount) public {
        require(amount > 0, "Invalid amount");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        payable(msg.sender).transfer(amount);
    }

    // Show account balance
    function showBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}

```

## **4. Explanation of the Program**

| Statement                           | Purpose                                                    |
| ----------------------------------- | ---------------------------------------------------------- |
| `mapping(address => uint)`          | Stores the balance of each customer address.               |
| `msg.sender`                        | Represents the address of the person calling the function. |
| `msg.value`                         | Represents the amount of Ether sent with a transaction.    |
| `payable`                           | Allows a function to receive Ether.                        |
| `require()`                         | Checks a condition and stops execution if it is false.     |
| `balances[msg.sender] += msg.value` | Adds deposited money to the customer's balance.            |
| `balances[msg.sender] -= amount`    | Deducts the withdrawal amount.                             |
| `transfer()`                        | Transfers Ether to the customer's address.                 |
| `view`                              | Allows reading contract data without modifying it.         |

### **How does the program work?**

Suppose a customer deposits 5 ETH.

- Initial balance = 0 ETH
- Deposited amount = 5 ETH
- Updated balance = 5 ETH

Now suppose the customer withdraws 2 ETH.

- Previous balance = 5 ETH
- Withdrawal amount = 2 ETH
- Remaining balance = 3 ETH

The `showBalance()` function displays the remaining 3 ETH.

## **5. Deployment Procedure on Ethereum Test Network**

For this practical, you can use Remix IDE with an Ethereum test network such as Sepolia.

[Smart Contracts mit Solidity programmieren](https://images.openai.com/static-rsc-4/-r3h4Jpa-S25_mVJPIM9OrYOFdvLI-WBkRNyHIir3KyACxWNvcYzBjZnTjO5l_71JBjV_Q4mjCNF-3eCMa5PWR6BqrvDbXv2lvN5z2k3NzSo0B7TMjwI-NnHJQcrQSwR_YDYcmypKfdJh0qtIfj6Dn_n_9c4fJh7nzVHSiiRyXw?purpose=inline)

[Deploying Your Smart Contract to Testnet(Sepolia) Using Metamask | by Asjad Ahmed Khan | kalpstudio | Medium](https://images.openai.com/static-rsc-4/xT0bKrD1yE-pMiBMp5VCjoGbN1cE-O04I2aeouC7e4STK6VMwND2ZPUp2NSRFti3IlRsF6AkIB14qvXymReZE81BdZyuBvJq68rrrdRB7_IKxh6rR1W6YFa5W05m9NQcOimSHJ5PP0Ut-yQQ2JRkXf5tsJ1JENS9EALvnkFnFn8?purpose=inline)

[Filecoin Filrep Oracle: Obtain miner reputations on-chain | Midpoint Documentation](https://images.openai.com/static-rsc-4/8TpX1vpbCgBSTudtIQCTeDCb6Q1yUYBOcJal65dOMDyMJ1MGboMlVAQBVEHj7LKOYyrmIfa4kvMM7DbRu63i3BbcrqZYngqVJF6GoAus80CnSsIpDrLUjq0R7fjEFMCn3xVYXHKp5V6LYQMG9Vdegzr1XkVHcUxkZFqGr60QgWs?purpose=inline)

5

**Step 1: Open Remix IDE**

Visit [Remix IDE](https://remix.ethereum.org/?utm_source=chatgpt.com).

**Step 2: Create a Solidity file**

- Create a file named `BankAccount.sol`.
- Paste the above Solidity program.

**Step 3: Compile the contract**

- Open Solidity Compiler.
- Select compiler version 0.8.20.
- Click Compile BankAccount.sol.

**Step 4: Connect to the test network**

- Install and open MetaMask.
- Select the Sepolia test network.
- Obtain Sepolia test ETH from a testnet faucet.

**Step 5: Deploy the contract**

- Open Deploy & Run Transactions.
- Select Environment: Injected Provider - MetaMask.
- Ensure MetaMask is connected to Sepolia.
- Select `BankAccount`.
- Click Deploy.
- Confirm the transaction in MetaMask.

**Step 6: Perform banking operations**

1. Deposit: Enter an amount in the Value field, select Ether, and click `deposit`.
2. Withdraw: Enter the withdrawal amount in Wei in the `withdraw` input field.
3. Show Balance: Click `showBalance` to display the customer's balance in Wei.

Remember that the contract's balance is maintained separately for each customer's address.

## **6. Sample Output**

Suppose the following operations are performed:

| Operation       | Amount | Balance |
| --------------- | ------ | ------- |
| Initial balance | 0 ETH  | 0 ETH   |
| Deposit         | 5 ETH  | 5 ETH   |
| Deposit         | 3 ETH  | 8 ETH   |
| Withdraw        | 2 ETH  | 6 ETH   |
| Show balance    | —      | 6 ETH   |

Illustrative output. Actual results depend on the transactions performed.

## **7. Result**

Thus, a Solidity smart contract for managing a customer's bank account was successfully written and deployed on the Ethereum test network. The deposit, withdrawal, and balance enquiry operations were implemented and tested successfully.

## **8. Viva Questions**

**Q1. What is mapping in Solidity?**

Mapping is a key-value data structure used to store and retrieve values based on unique keys.

**Q2. What is&#x20;**`msg.sender`**?**

It represents the address of the account that calls the smart contract function.

**Q3. What is&#x20;**`msg.value`**?**

It represents the amount of Ether sent along with a payable function call.

**Q4. Why is the deposit function payable?**

Because it needs to accept Ether from the customer.

**Q5. What is the purpose of require()?**

It checks conditions and reverts the transaction if a condition is not satisfied.

**Q6. What happens if a customer withdraws more money than their balance?**

The transaction fails because the insufficient balance condition is not satisfied.

**Q7. What is Sepolia?**

Sepolia is an Ethereum test network used for testing and deploying smart contracts without spending real ETH.

**Q8. What is the difference between view and payable?**

- `view` allows reading blockchain data without modifying state.
- `payable` allows a function to receive Ether.

**Q9. Does showBalance() consume gas?**

When called externally as a read-only call, it does not require an on-chain transaction or gas payment.

**Q10. Why do we use a mapping for bank accounts?**

It allows us to maintain separate balances for multiple customer addresses.

**One thing to remember for your practical:** This is a basic educational banking contract, not a production-ready banking system. It demonstrates the three required operations and maintains balances separately for each Ethereum address.
