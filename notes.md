- map(func, iterable) → applies a function to each item
- filter(func, iterable) → keeps items where function returns True
- lambda → quick, anonymous function: lambda x: x * 2

## static and class methods

| Method Type                | Has access to       | Can modify      | Typical Use                                |
| -------------------------- | ------------------- | --------------- | ------------------------------------------ |
| `instance method` (normal) | ✅ `self` (instance) | ✅ instance vars | Work with object-specific data             |
| `@classmethod`             | ✅ `cls` (class)     | ✅ class vars    | Class-level logic, factory methods         |
| `@staticmethod`            | ❌ neither           | ❌ nothing       | Utility/helper logic — no `self`, no `cls` |

✅ Static method → no self, no cls
✅ Class method → gets cls, not self
✅ Instance method → gets self (can also access class vars, but usually not modify them


## __str__ and __repr__
> When you `print(obj)`, Python first uses `__str__()`, if that’s missing it uses `__repr__()`, and if both are missing, it falls back to the default memory address from the base `object` class.

## Encapsulation

| Java/C++    | Python Equivalent | Notes                                         |
| ----------- | ----------------- | --------------------------------------------- |
| `public`    | `name`            | Default – fully accessible                    |
| `protected` | `_name`           | Convention – *“don’t touch unless you must”*  |
| `private`   | `__name`          | Triggers **name mangling** for access control |


🔍 Behind the Scenes (Name Mangling):
That __content is actually stored as:
> note._SecureNote__content
So you could access it like:
> print(note._SecureNote__content)  # 😈 But you shouldn't.
🧠 Recap:
Python doesn’t block access — it discourages it with conventions and name mangling.
Encapsulation helps prevent accidental changes and lets you add validation if needed later.

> Inheritance vs Composition
🧠 Mental Trick:
Is-A? ➡️ Use Inheritance
Has-A? ➡️ Use Composition

⚔️ Real-World Analogy:
🧱 You don’t build a house by saying:
"A house is a door, is a window, is a kitchen."

🚀 Instead, you say:
"A house has a door, has windows, has a kitchen."
Composition builds complex things out of simple, focused parts.

✅ Summary
Concept	Use when...
Inheritance	- One object is a type of another
Composition - One object uses/has another inside it

> Abstraction

In simple words:
Abstraction is hiding the internal details and showing only the essential parts to the outside world.
Just like:
You use a TV remote without knowing how the circuit works.

> Encapsulation vs Abstraction
✅ Encapsulation
→ Hides the data
→ Prevents direct access
→ Use __private_vars + getters/setters
→ Keeps your object’s internals safe from misuse

✅ Abstraction
→ Hides the implementation
→ Just says: “You must have this method”
→ Use ABC and @abstractmethod
→ Lets subclasses implement it their own way

| Concept           | Focus          | Hides           | Example                          |
| ----------------- | -------------- | --------------- | -------------------------------- |
| **Encapsulation** | *Protect data* | Data/Attributes | `__balance`, `get_balance()`     |
| **Abstraction**   | *Simplify use* | Implementation  | `@abstractmethod start_engine()` |

🔁 Real-life analogy to reinforce:
Encapsulation is like your phone locking with a passcode — you can’t mess with its insides without permission.

Abstraction is like a TV remote — it gives you buttons to press, but you don’t know or care how the electronics work inside.

