**Source Hash:** `3cd1234e9df836031e41734e2ee1e1da936f9592d720678c0f1a3ae8279e3fbd`

# BuilderField

## Overview

## Constructor Descriptions
- `BuilderField(@Nonnull FieldBuilder<Type, FieldType, ?> builder)`
  - Creates a `BuilderField` instance.
- `BuilderField(@Nonnull KeyedCodec<FieldType> codec, TriConsumer<Type, FieldType, ExtraInfo> setter, BiFunction<Type, ExtraInfo, FieldType> getter, TriConsumer<Type, Type, ExtraInfo> inherit)`
  - Creates a `BuilderField` instance.
- `BuilderField(this)`
  - Creates a `BuilderField` instance.

## Method Descriptions
- `getCodec()`: Add description.
  - Executes `getCodec` behavior.
- `getMinVersion()`: Add description.
  - Executes `getMinVersion` behavior.
- `getMaxVersion()`: Add description.
  - Executes `getMaxVersion` behavior.
- `getHighestSupportedVersion()`: Add description.
  - Executes `getHighestSupportedVersion` behavior.
- `supportsVersion(int version)`: Add description.
  - Executes `supportsVersion` behavior.
- `hasNonNullValidator()`: Add description.
  - Executes `hasNonNullValidator` behavior.
- `getDocumentation()`: Add description.
  - Executes `getDocumentation` behavior.
- `decode(BsonDocument document, Type t, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `decode` behavior.
- `decodeAndInherit(BsonDocument document, Type t, @Nullable Type parent, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `decodeAndInherit` behavior.
- `encode(@Nonnull BsonDocument document, Type t, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `encode` behavior.
- `inherit(Type t, Type parent, ExtraInfo extraInfo)`: Add description.
  - Executes `inherit` behavior.
- `decodeJson(@Nonnull RawJsonReader reader, Type t, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `decodeJson` behavior.
- `decodeAndInheritJson(@Nonnull RawJsonReader reader, Type t, @Nullable Type parent, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `decodeAndInheritJson` behavior.
- `setValue(Type t, @Nullable FieldType value, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `setValue` behavior.
- `validate(Type t, @Nonnull ExtraInfo extraInfo)`: Add description.
  - Executes `validate` behavior.
- `validateDefaults(Type t, @Nonnull ExtraInfo extraInfo, Set<Codec<?>> tested)`: Add description.
  - Executes `validateDefaults` behavior.
- `validateValue(FieldType value, @Nonnull ExtraInfo extraInfo, @Nullable Predicate<Validator<? super FieldType>> filter)`: Add description.
  - Executes `validateValue` behavior.
- `nullValidate(Type t, @Nonnull ValidationResults results, ExtraInfo extraInfo)`: Add description.
  - Executes `nullValidate` behavior.
- `updateSchema(SchemaContext context, @Nonnull Schema target)`: Add description.
  - Executes `updateSchema` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `addValidator(Validator<? super FieldType> validator)`: Add description.
  - Executes `addValidator` behavior.
- `addValidator(LegacyValidator<? super FieldType> validator)`: Add description.
  - Executes `addValidator` behavior.
- `addValidatorLate(final @Nonnull Supplier<LateValidator<? super FieldType>> validatorSupplier)`: Add description.
  - Executes `addValidatorLate` behavior.
- `accept(FieldType fieldType, ValidationResults results)`: Add description.
  - Executes `accept` behavior.
- `acceptLate(FieldType fieldType, ValidationResults results, ExtraInfo extraInfo)`: Add description.
  - Executes `acceptLate` behavior.
- `updateSchema(SchemaContext context, Schema target)`: Add description.
  - Executes `updateSchema` behavior.
- `setVersionRange(int minVersion, int maxVersion)`: Add description.
  - Executes `setVersionRange` behavior.
- `documentation(String doc)`: Add description.
  - Executes `documentation` behavior.
- `metadata(Metadata metadata)`: Add description.
  - Executes `metadata` behavior.
- `add()`: Add description.
  - Executes `add` behavior.

## Notes
- No additional notes.
