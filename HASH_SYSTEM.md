# Sistema de Hash - Rastreamento de Mudanças

O sistema de hash do Hydocs permite rastrear mudanças nos arquivos fonte Java e evitar regeneração desnecessária de documentação.

## 📋 Como Funciona

### 1. Cálculo de Hash

Para cada arquivo Java processado, o sistema:
- Calcula um hash SHA256 do conteúdo do arquivo fonte
- Armazena este hash na classe `JavaClass`
- Salva o hash na documentação gerada
- Mantém um índice central de hashes em `hashes.json`

### 2. Detecção de Mudanças

Ao regenerar a documentação com `--skip-unchanged`:
- Carrega o índice de hashes da build anterior (`build/hashes.json`)
- Compara o hash atual de cada arquivo com o hash anterior
- Pula a geração se:
  - O hash não mudou (arquivo fonte idêntico)
  - A documentação já existe no disco

### 3. Arquivo de Índice

O arquivo `build/hashes.json` contém um mapeamento de:
```json
{
  "com.hypixel.hytale.Main": "3bf87abfd876785ff2e1589e8f64f3fb3625633b89eadf824e46082917137635",
  "com.hypixel.hytale.server.HytaleServer": "a9162add3c6cab43883af10b5f108cb954755c9329388dc211255d7783c14d53"
}
```

## 🚀 Uso

### Geração Normal (Regenera Tudo)

```bash
python3 hydocs.py --only-docs
```

Resultado:
```
✅ Generated 4851 files (skipped 0 unchanged, 0 changed).
```

### Geração Inteligente (Pula Não-Modificados)

```bash
python3 hydocs.py --only-docs --skip-unchanged
```

Resultado:
```
📋 Loaded 4851 previous file hashes...
✅ Generated 63 files (skipped 4788 unchanged, 63 changed).
```

**Benefícios:**
- ⚡ Até 99% mais rápido quando poucos arquivos mudaram
- 💾 Economiza I/O e processamento
- 📊 Estatísticas claras sobre o que foi modificado

## 📄 Metadados na Documentação

Cada arquivo de documentação inclui metadados de build:

```markdown
# ClassName

**Full Qualified Name:** `com.hypixel.hytale.package.ClassName`

**Type:** class

**Package:** `com.hypixel.hytale.package`

**File Location:** `com/hypixel/hytale/package/ClassName.md`

**Source Hash:** `3bf87abfd876785ff2e1589e8f64f3fb3625633b89eadf824e46082917137635`

**Generated At:** `2026-01-18T16:19:12.915419Z`

---
```

### Campos de Metadados

| Campo | Descrição | Formato |
|-------|-----------|---------|
| `Source Hash` | Hash SHA256 do arquivo fonte Java | Hex string (64 caracteres) |
| `Generated At` | Timestamp de quando a documentação foi gerada | ISO 8601 com timezone |

## 🔍 Casos de Uso

### 1. Desenvolvimento Iterativo

Ao fazer mudanças em algumas classes e regenerar:

```bash
# Modificou apenas 3 classes
python3 hydocs.py --only-docs --skip-unchanged
# Resultado: Generated 3 files (skipped 4848 unchanged, 3 changed)
```

### 2. Verificar Mudanças

Ver quais arquivos mudaram desde a última build:

```bash
# Compare hashes.json antes e depois
diff old-hashes.json build/hashes.json
```

### 3. CI/CD Otimizado

Em pipelines de CI, use `--skip-unchanged` para builds incrementais:

```bash
# Restaura hashes.json do cache
cp cache/hashes.json build/hashes.json

# Gera apenas arquivos modificados
python3 hydocs.py --only-docs --skip-unchanged

# Salva novo hashes.json para próximo build
cp build/hashes.json cache/hashes.json
```

### 4. Auditoria e Rastreamento

Use os hashes para:
- Verificar integridade dos arquivos fonte
- Rastrear quando cada classe foi modificada
- Detectar mudanças não documentadas

## 📊 Estatísticas

O sistema reporta 3 métricas:

```
✅ Generated 63 files (skipped 4788 unchanged, 63 changed).
```

- **Generated**: Arquivos de documentação efetivamente escritos
- **Skipped**: Arquivos pulados (hash idêntico + output existe)
- **Changed**: Arquivos com hash diferente (foram modificados)

**Nota:** `generated` = `changed` + (arquivos novos ou output faltando)

## 🎯 Performance

### Sem `--skip-unchanged`

```bash
python3 hydocs.py --only-docs
# Tempo: ~30 segundos
# Arquivos: 4851 gerados
```

### Com `--skip-unchanged` (poucos arquivos mudaram)

```bash
python3 hydocs.py --only-docs --skip-unchanged
# Tempo: ~2 segundos
# Arquivos: 63 gerados, 4788 pulados
```

**Melhoria:** ~93% mais rápido (30s → 2s)

## 🛠️ Implementação Técnica

### Algoritmo de Hash

```python
def calculate_file_hash(filepath: str) -> str:
    """Calculates SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()
```

**Por que SHA256?**
- Seguro contra colisões
- Rápido para arquivos pequenos
- Amplamente suportado
- Fácil de comparar e armazenar

### Estrutura de Dados

```python
class JavaClass:
    source_hash: str      # Hash SHA256 do arquivo fonte
    generated_at: str     # Timestamp ISO 8601
    # ... outros campos
```

### Índice de Hashes

```python
# build/hashes.json
{
  "full.class.Name": "hash_sha256_64_chars",
  ...
}
```

## ⚠️ Limitações

### 1. Mudanças no Template

Se você modificar o template de documentação (`generate_class_markdown()`), os hashes dos **fontes** não mudam, mas você ainda precisa regenerar tudo:

```bash
# Forçar regeneração completa
python3 hydocs.py --only-docs  # Sem --skip-unchanged
```

### 2. Custom Docs

Mudanças em `/docs/` não afetam os hashes dos arquivos fonte. Se você atualizar custom docs:

```bash
# Custom docs mudaram, regenerar afetados
# Opção 1: Regenerar tudo
python3 hydocs.py --only-docs

# Opção 2: Deletar docs afetados e regenerar com skip
rm build/com/hypixel/hytale/Main.md
python3 hydocs.py --only-docs --skip-unchanged
```

### 3. Arquivos Deletados

Se um arquivo Java for removido do source:
- O hash permanece em `hashes.json`
- A documentação antiga permanece em `/build/`
- Solução: Delete `/build/` e regenere completamente ocasionalmente

## 💡 Boas Práticas

### 1. Em Desenvolvimento Local

Use `--skip-unchanged` para iterações rápidas:
```bash
python3 hydocs.py --only-docs --skip-unchanged
```

### 2. Em CI/CD

Para builds de release, regenere tudo:
```bash
python3 hydocs.py --only-docs  # Sem --skip-unchanged
```

Para builds incrementais (PRs, commits):
```bash
python3 hydocs.py --only-docs --skip-unchanged
```

### 3. Limpeza Periódica

A cada versão major, limpe e regenere:
```bash
rm -rf build/
python3 hydocs.py --only-docs
```

### 4. Versionamento

Considere versionar o `hashes.json` em algumas situações:
```bash
cp build/hashes.json hashes-v1.0.0.json
```

## 🔧 Troubleshooting

### Hash Mismatch Inesperado

Se arquivos são regenerados inesperadamente:

```bash
# Verificar se o fonte mudou
sha256sum lib/src/com/hypixel/hytale/Main.java

# Comparar com hash salvo
grep "Main" build/hashes.json
```

### Performance Degradada

Se `--skip-unchanged` não está ajudando:

```bash
# Verificar quantos arquivos realmente mudaram
python3 hydocs.py --only-docs --skip-unchanged 2>&1 | grep "Generated"
# Se "changed" está alto, muitos arquivos realmente mudaram
```

### hashes.json Corrompido

Se o arquivo está corrompido:

```bash
# Deletar e regenerar
rm build/hashes.json
python3 hydocs.py --only-docs  # Cria novo hashes.json
```

## 📚 Exemplos Práticos

### Exemplo 1: Workflow Diário

```bash
# Segunda-feira: Build completo
python3 hydocs.py --file server.jar
# Generated 4851 files

# Terça-feira: Apenas algumas mudanças
python3 hydocs.py --only-docs --skip-unchanged
# Generated 12 files (skipped 4839 unchanged, 12 changed)

# Quarta-feira: Mudanças na custom docs
# Deletar afetados e regenerar
rm build/com/hypixel/hytale/Main.md
python3 hydocs.py --only-docs --skip-unchanged
# Generated 1 file (skipped 4850 unchanged, 1 changed)
```

### Exemplo 2: CI Pipeline

```yaml
# .github/workflows/docs.yml
- name: Restore hash cache
  uses: actions/cache@v3
  with:
    path: build/hashes.json
    key: hashes-${{ github.sha }}
    restore-keys: hashes-

- name: Generate docs (incremental)
  run: python3 hydocs.py --only-docs --skip-unchanged

- name: Save hash cache
  uses: actions/cache/save@v3
  with:
    path: build/hashes.json
    key: hashes-${{ github.sha }}
```

### Exemplo 3: Auditoria de Mudanças

```bash
# Salvar hashes antes
cp build/hashes.json hashes-before.json

# Fazer mudanças...
# Regenerar
python3 hydocs.py --only-docs

# Ver o que mudou
diff hashes-before.json build/hashes.json | grep "^[<>]" | wc -l
# Saída: 15 (15 classes modificadas)
```

## 🎓 Conclusão

O sistema de hash do Hydocs oferece:

✅ **Performance**: Até 99% mais rápido em builds incrementais
✅ **Rastreabilidade**: Sabe exatamente o que mudou e quando
✅ **Auditoria**: Hash SHA256 para verificação de integridade
✅ **Flexibilidade**: Use quando fizer sentido (`--skip-unchanged`)
✅ **Transparência**: Estatísticas claras sobre o processo

Use `--skip-unchanged` durante desenvolvimento para iterações rápidas, e regenere completamente para releases oficiais!
