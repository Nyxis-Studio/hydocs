# RandomExtra

## Overview
- Documentation for `RandomExtra`.
- Declared as a class in `com.hypixel.hytale.math.random`.

## Constructors
- `RandomExtra()`
  - Creates a `RandomExtra` instance.

## Methods
- `randomBinomial()`
  - Executes `randomBinomial` behavior.
- `randomRange(@Nonnull double[] range)`
  - Executes `randomRange` behavior.
- `randomRange(double from, double to)`
  - Executes `randomRange` behavior.
- `randomRange(@Nonnull float[] range)`
  - Executes `randomRange` behavior.
- `randomRange(float from, float to)`
  - Executes `randomRange` behavior.
- `randomRange(int bound)`
  - Executes `randomRange` behavior.
- `randomRange(@Nonnull int[] range)`
  - Executes `randomRange` behavior.
- `randomRange(int from, int to)`
  - Executes `randomRange` behavior.
- `randomRange(long from, long to)`
  - Executes `randomRange` behavior.
- `randomDuration(@Nonnull Duration from, @Nonnull Duration to)`
  - Executes `randomDuration` behavior.
- `randomBoolean()`
  - Executes `randomBoolean` behavior.
- `randomElement(@Nonnull List<T> collection)`
  - Executes `randomElement` behavior.
- `jitter(@Nonnull Vector3d vec, double maxRange)`
  - Executes `jitter` behavior.
- `randomWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull ToDoubleFunction<T> weight)`
  - Executes `randomWeightedElement` behavior.
- `randomWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull ToDoubleFunction<T> weight, double sumWeights)`
  - Executes `randomWeightedElement` behavior.
- `randomIntWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull ToIntFunction<T> weight)`
  - Executes `randomIntWeightedElement` behavior.
- `randomIntWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull ToIntFunction<T> weight, int sumWeights)`
  - Executes `randomIntWeightedElement` behavior.
- `randomWeightedElementFiltered(@Nonnull Collection<? extends T> elements, @Nonnull Predicate<T> filter, @Nonnull ToIntFunction<T> weight)`
  - Executes `randomWeightedElementFiltered` behavior.
- `randomWeightedElementFiltered(@Nonnull Collection<? extends T> elements, @Nonnull Predicate<T> filter, @Nonnull ToIntFunction<T> weight, int sumWeights)`
  - Executes `randomWeightedElementFiltered` behavior.
- `randomWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull Predicate<T> filter, @Nonnull ToDoubleFunction<T> weight)`
  - Executes `randomWeightedElement` behavior.
- `randomWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull Predicate<T> filter, @Nonnull ToDoubleFunction<T> weight, double sumWeights)`
  - Executes `randomWeightedElement` behavior.
- `randomWeightedElement(@Nonnull Collection<? extends T> elements, @Nonnull BiPredicate<T, U> filter, @Nonnull ToDoubleBiFunction<T, U> weight, double sumWeights, U meta)`
  - Executes `randomWeightedElement` behavior.
- `reservoirSample(@Nonnull List<T> input, @Nonnull Predicate<T> matcher, int count, @Nonnull List<T> picked)`
  - Executes `reservoirSample` behavior.
- `reservoirSample(@Nonnull S input, @Nonnull TriFunction<E, G, H, F> filter, int count, @Nonnull T picked, G g, H h)`
  - Executes `reservoirSample` behavior.
- `reservoirSample(E element, int count, @Nonnull T picked)`
  - Executes `reservoirSample` behavior.
- `pickWeightedIndex(@Nonnull double[] weights)`
  - Executes `pickWeightedIndex` behavior.

## Notes
- No additional notes.
