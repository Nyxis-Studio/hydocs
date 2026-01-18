# BuilderField

## Overview
- Documentation for `BuilderField`.
- Declared as a class in `com.hypixel.hytale.codec.builder`.

## Constructors
- `BuilderField(@Nonnull FieldBuilder<Type, FieldType, ?> builder)`
  - Creates a `BuilderField` instance.
- `BuilderField(@Nonnull KeyedCodec<FieldType> codec, TriConsumer<Type, FieldType, ExtraInfo> setter, BiFunction<Type, ExtraInfo, FieldType> getter, TriConsumer<Type, Type, ExtraInfo> inherit)`
  - Creates a `BuilderField` instance.
- `BuilderField(this)`
  - Creates a `BuilderField` instance.

## Methods
- `getCodec()`
  - Executes `getCodec` behavior.
- `getMinVersion()`
  - Executes `getMinVersion` behavior.
- `getMaxVersion()`
  - Executes `getMaxVersion` behavior.
- `getHighestSupportedVersion()`
  - Executes `getHighestSupportedVersion` behavior.
- `supportsVersion(int version)`
  - Executes `supportsVersion` behavior.
- `hasNonNullValidator()`
  - Executes `hasNonNullValidator` behavior.
- `getDocumentation()`
  - Executes `getDocumentation` behavior.
- `decode(BsonDocument document, Type t, @Nonnull ExtraInfo extraInfo)`
  - Executes `decode` behavior.
- `decodeAndInherit(BsonDocument document, Type t, @Nullable Type parent, @Nonnull ExtraInfo extraInfo)`
  - Executes `decodeAndInherit` behavior.
- `encode(@Nonnull BsonDocument document, Type t, @Nonnull ExtraInfo extraInfo)`
  - Executes `encode` behavior.
- `inherit(Type t, Type parent, ExtraInfo extraInfo)`
  - Executes `inherit` behavior.
- `decodeJson(@Nonnull RawJsonReader reader, Type t, @Nonnull ExtraInfo extraInfo)`
  - Executes `decodeJson` behavior.
- `decodeAndInheritJson(@Nonnull RawJsonReader reader, Type t, @Nullable Type parent, @Nonnull ExtraInfo extraInfo)`
  - Executes `decodeAndInheritJson` behavior.
- `setValue(Type t, @Nullable FieldType value, @Nonnull ExtraInfo extraInfo)`
  - Executes `setValue` behavior.
- `validate(Type t, @Nonnull ExtraInfo extraInfo)`
  - Executes `validate` behavior.
- `validateDefaults(Type t, @Nonnull ExtraInfo extraInfo, Set<Codec<?>> tested)`
  - Executes `validateDefaults` behavior.
- `validateValue(FieldType value, @Nonnull ExtraInfo extraInfo, @Nullable Predicate<Validator<? super FieldType>> filter)`
  - Executes `validateValue` behavior.
- `nullValidate(Type t, @Nonnull ValidationResults results, ExtraInfo extraInfo)`
  - Executes `nullValidate` behavior.
- `updateSchema(SchemaContext context, @Nonnull Schema target)`
  - Executes `updateSchema` behavior.
- `toString()`
  - Executes `toString` behavior.
- `addValidator(Validator<? super FieldType> validator)`
  - Executes `addValidator` behavior.
- `addValidator(LegacyValidator<? super FieldType> validator)`
  - Executes `addValidator` behavior.
- `addValidatorLate(final @Nonnull Supplier<LateValidator<? super FieldType>> validatorSupplier)`
  - Executes `addValidatorLate` behavior.
- `accept(FieldType fieldType, ValidationResults results)`
  - Executes `accept` behavior.
- `acceptLate(FieldType fieldType, ValidationResults results, ExtraInfo extraInfo)`
  - Executes `acceptLate` behavior.
- `updateSchema(SchemaContext context, Schema target)`
  - Executes `updateSchema` behavior.
- `setVersionRange(int minVersion, int maxVersion)`
  - Executes `setVersionRange` behavior.
- `documentation(String doc)`
  - Executes `documentation` behavior.
- `metadata(Metadata metadata)`
  - Executes `metadata` behavior.
- `add()`
  - Executes `add` behavior.

## Notes
- No additional notes.
