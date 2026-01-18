# Registry

## Overview
- Documentation for `Registry`.
- Declared as a class in `com.hypixel.hytale.registry`.

## Constructors
- `Registry(@Nonnull List<BooleanConsumer> registrations, @Nonnull BooleanSupplier precondition, String preconditionMessage, @Nonnull RegistrationWrapFunction<T> wrappingFunction)`
  - Creates a `Registry` instance.

## Methods
- `checkPrecondition()`
  - Executes `checkPrecondition` behavior.
- `isEnabled()`
  - Executes `isEnabled` behavior.
- `enable()`
  - Executes `enable` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `register(@Nonnull T registration)`
  - Executes `register` behavior.
- `getRegistrations()`
  - Executes `getRegistrations` behavior.
- `toString()`
  - Executes `toString` behavior.
- `wrap(T var1, BooleanSupplier var2, Runnable var3)`
  - Executes `wrap` behavior.

## Notes
- No additional notes.
