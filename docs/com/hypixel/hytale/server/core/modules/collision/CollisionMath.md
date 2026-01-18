# CollisionMath

## Overview
- Documentation for `CollisionMath`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.collision`.

## Constructors
- `CollisionMath()`
  - Creates a `CollisionMath` instance.

## Methods
- `intersectVectorAABB(@Nonnull Vector3d pos, @Nonnull Vector3d vec, double x, double y, double z, @Nonnull Box box, @Nonnull Vector2d minMax)`
  - Executes `intersectVectorAABB` behavior.
- `intersectRayAABB(@Nonnull Vector3d pos, @Nonnull Vector3d ray, double x, double y, double z, @Nonnull Box box, @Nonnull Vector2d minMax)`
  - Executes `intersectRayAABB` behavior.
- `intersectRayAABB(@Nonnull Vector3d pos, @Nonnull Vector3d ray, double x, double y, double z, @Nonnull Box box)`
  - Executes `intersectRayAABB` behavior.
- `intersectVectorAABB(@Nonnull Vector3d pos, @Nonnull Vector3d vec, double x, double y, double z, double radius, double height, @Nonnull Vector2d minMax)`
  - Executes `intersectVectorAABB` behavior.
- `intersectRayAABB(@Nonnull Vector3d pos, @Nonnull Vector3d ray, double x, double y, double z, double radius, double height, @Nonnull Vector2d minMax)`
  - Executes `intersectRayAABB` behavior.
- `intersectSweptAABBs(@Nonnull Vector3d posP, @Nonnull Vector3d vP, @Nonnull Box p, @Nonnull Vector3d posQ, @Nonnull Box q, @Nonnull Vector2d minMax, @Nonnull Box temp)`
  - Executes `intersectSweptAABBs` behavior.
- `intersectSweptAABBs(@Nonnull Vector3d posP, @Nonnull Vector3d vP, @Nonnull Box p, double qx, double qy, double qz, @Nonnull Box q, @Nonnull Vector2d minMax, @Nonnull Box temp)`
  - Executes `intersectSweptAABBs` behavior.
- `intersect1D(double p, double s, double min, double max, @Nonnull Vector2d minMax)`
  - Executes `intersect1D` behavior.
- `isDisjoint(int code)`
  - Executes `isDisjoint` behavior.
- `isOverlapping(int code)`
  - Executes `isOverlapping` behavior.
- `isTouching(int code)`
  - Executes `isTouching` behavior.
- `intersectAABBs(@Nonnull Vector3d p, @Nonnull Box bbP, @Nonnull Vector3d q, @Nonnull Box bbQ)`
  - Executes `intersectAABBs` behavior.
- `intersectAABBs(double px, double py, double pz, @Nonnull Box bbP, double qx, double qy, double qz, @Nonnull Box bbQ)`
  - Executes `intersectAABBs` behavior.
- `intersect1D(double p, double pMin, double pMax, double q, double qMin, double qMax)`
  - Executes `intersect1D` behavior.
- `intersectAABBs(double px, double py, double pz, @Nonnull Box bbP, double qx, double qy, double qz, @Nonnull Box bbQ, double thickness)`
  - Executes `intersectAABBs` behavior.
- `intersect1D(double p, double pMin, double pMax, double q, double qMin, double qMax, double thickness)`
  - Executes `intersect1D` behavior.

## Notes
- No additional notes.
