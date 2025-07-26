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