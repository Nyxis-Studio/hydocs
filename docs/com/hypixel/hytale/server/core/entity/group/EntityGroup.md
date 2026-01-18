# EntityGroup

## Overview
- Documentation for `EntityGroup`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.group`.

## Constructors
- `EntityGroup()`
  - Creates a `EntityGroup` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getLeaderRef()`
  - Executes `getLeaderRef` behavior.
- `setLeaderRef(@Nonnull Ref<EntityStore> leaderRef)`
  - Executes `setLeaderRef` behavior.
- `add(@Nonnull Ref<EntityStore> reference)`
  - Executes `add` behavior.
- `remove(@Nonnull Ref<EntityStore> reference)`
  - Executes `remove` behavior.
- `getFirst()`
  - Executes `getFirst` behavior.
- `getMemberList()`
  - Executes `getMemberList` behavior.
- `size()`
  - Executes `size` behavior.
- `isDissolved()`
  - Executes `isDissolved` behavior.
- `setDissolved(boolean dissolved)`
  - Executes `setDissolved` behavior.
- `clear()`
  - Executes `clear` behavior.
- `isMember(Ref<EntityStore> reference)`
  - Executes `isMember` behavior.
- `forEachMemberExcludingLeader(@Nonnull TriConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T arg)`
  - Executes `forEachMemberExcludingLeader` behavior.
- `forEachMemberExcludingSelf(@Nonnull TriConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T arg)`
  - Executes `forEachMemberExcludingSelf` behavior.
- `forEachMember(@Nonnull TriConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T arg)`
  - Executes `forEachMember` behavior.
- `forEachMember(@Nonnull TriConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T arg, Ref<EntityStore> excludeReference)`
  - Executes `forEachMember` behavior.
- `forEachMemberExcludingLeader(@Nonnull QuadConsumer<Ref<EntityStore>, Ref<EntityStore>, T, V> consumer, Ref<EntityStore> sender, T t, V v)`
  - Executes `forEachMemberExcludingLeader` behavior.
- `forEachMemberExcludingSelf(@Nonnull QuadConsumer<Ref<EntityStore>, Ref<EntityStore>, T, V> consumer, Ref<EntityStore> sender, T t, V v)`
  - Executes `forEachMemberExcludingSelf` behavior.
- `forEachMember(@Nonnull QuadConsumer<Ref<EntityStore>, Ref<EntityStore>, T, V> consumer, Ref<EntityStore> sender, T t, V v)`
  - Executes `forEachMember` behavior.
- `forEachMember(@Nonnull QuadConsumer<Ref<EntityStore>, Ref<EntityStore>, T, V> consumer, Ref<EntityStore> sender, T t, V v, Ref<EntityStore> excludeReference)`
  - Executes `forEachMember` behavior.
- `forEachMemberExcludingLeader(@Nonnull IntTriObjectConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T t, int value)`
  - Executes `forEachMemberExcludingLeader` behavior.
- `forEachMemberExcludingSelf(@Nonnull IntTriObjectConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, @Nonnull Ref<EntityStore> sender, T t, int value)`
  - Executes `forEachMemberExcludingSelf` behavior.
- `forEachMember(@Nonnull IntTriObjectConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T t, int value)`
  - Executes `forEachMember` behavior.
- `forEachMember(@Nonnull IntTriObjectConsumer<Ref<EntityStore>, Ref<EntityStore>, T> consumer, Ref<EntityStore> sender, T t, int value, Ref<EntityStore> excludeReference)`
  - Executes `forEachMember` behavior.
- `forEachMember(@Nonnull IntBiObjectConsumer<Ref<EntityStore>, T> consumer, T t)`
  - Executes `forEachMember` behavior.
- `testMembers(@Nonnull Predicate<Ref<EntityStore>> predicate, boolean skipLeader)`
  - Executes `testMembers` behavior.
- `clone()`
  - Executes `clone` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
