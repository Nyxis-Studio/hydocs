# Guia de Referência para IA - Documentação Customizada Hytale

Este arquivo serve como referência rápida para LLMs ao criar documentação customizada para classes Hytale.

## 🎯 Formato Obrigatório

Toda documentação customizada DEVE seguir este formato exato:

```markdown
## Overview
[Descrição concisa da classe em 2-3 linhas explicando seu propósito]

## Field Descriptions
- `FIELD_NAME`: [Descrição útil do que este campo representa]

## Constructor Descriptions
- `ClassName(ParamType param)`: [O que este construtor faz]

## Method Descriptions
- `methodName(ParamType param)`: [Descrição útil do comportamento do método]

## Usage Notes
[Informações importantes sobre uso, padrões comuns, armadilhas]

## Examples
```java
// Exemplos práticos de código
```
```

## ✅ O QUE FAZER

### Overview
```markdown
## Overview
Classe central do servidor que gerencia o ciclo de vida do Hytale, incluindo inicialização, gerenciamento de plugins, barramento de eventos e procedimentos de desligamento. Atua como ponto de entrada principal para operações server-side.
```

### Field Descriptions
```markdown
## Field Descriptions
- `DEFAULT_PORT`: Porta de rede padrão usada pelo servidor Hytale para conexões de clientes (tipicamente 25565 para compatibilidade com protocolo Minecraft).
- `SCHEDULED_EXECUTOR`: Executor global para agendamento de tarefas assíncronas e operações periódicas. Compartilhado entre todos os componentes do servidor.
```

### Constructor Descriptions
```markdown
## Constructor Descriptions
- `HytaleServer()`: Cria uma nova instância com configuração padrão. Inicializa o event bus, plugin manager e todos os subsistemas principais.
- `HytaleServer(HytaleServerConfig config)`: Cria instância com configuração customizada. Use quando precisar sobrescrever configurações padrão como porta ou max players.
```

### Method Descriptions
```markdown
## Method Descriptions
- `get()`: Retorna a instância singleton do servidor. Thread-safe e garantido retornar instância não-nula após inicialização.
- `shutdownServer(ShutdownReason reason)`: Desliga o servidor com motivo específico. Triggers eventos de shutdown e procedimentos de cleanup. Bloqueia até conclusão.
- `getTPS()`: Retorna a taxa atual de ticks por segundo. Servidor saudável mantém próximo a 20 TPS. Valores baixos indicam lag.
```

### Usage Notes
```markdown
## Usage Notes
- Sempre use `HytaleServer.get()` para acessar a instância - nunca armazene sua própria referência
- Shutdown deve ser acionado através dos métodos `shutdownServer()` - nunca mate o processo diretamente
- O servidor segue ciclo de vida estrito: boot → setup → start → running → stop → shutdown
- Maior parte das operações deve ser executada na thread principal do servidor
```

### Examples
```markdown
## Examples
```java
// Obter instância do servidor
HytaleServer server = HytaleServer.get();

// Desligamento gracioso
server.shutdownServer(ShutdownReason.SHUTDOWN);

// Verificar estado antes de operações
if (server.isRunning()) {
    WorldManager worlds = server.getWorldManager();
}
```
```

## ❌ O QUE NÃO FAZER

### ❌ NÃO repetir informações estruturais
```markdown
# HytaleServer  ❌ ERRADO

## Declaration  ❌ ERRADO
public class HytaleServer

## Methods  ❌ ERRADO (deveria ser "Method Descriptions")
- public void shutdownServer()  ❌ ERRADO (não repita assinatura)
```

### ❌ NÃO usar descrições genéricas
```markdown
## Method Descriptions
- `save()`: Executa comportamento de save.  ❌ GENÉRICO DEMAIS
- `load()`: Carrega dados.  ❌ GENÉRICO DEMAIS
```

**✅ CORRETO:**
```markdown
## Method Descriptions
- `save()`: Persiste todos os dados do mundo para disco, incluindo chunks, entidades e dados de jogadores. Operação bloqueante que pode levar vários segundos para mundos grandes.
- `load()`: Carrega configuração do servidor de server.properties. Deve ser chamado antes de start(). Lança IOException se arquivo não existir.
```

### ❌ NÃO incluir detalhes de implementação
```markdown
- `calculate()`: Primeiro inicializa array com tamanho 10, depois itera usando for loop...  ❌ DETALHE DE IMPLEMENTAÇÃO
```

**✅ CORRETO:**
```markdown
- `calculate()`: Calcula a média ponderada dos valores fornecidos. Retorna NaN se array vazio. Complexidade: O(n).
```

## 🔍 Template Rápido para Copy-Paste

```markdown
## Overview
[Classe que faz X, responsável por Y. Usada para Z.]

## Field Descriptions
- `FIELD_NAME`: [O que representa e por que existe]

## Constructor Descriptions
- `ClassName()`: [O que inicializa e quando usar]

## Method Descriptions
- `methodName()`: [O que faz, quando chamar, o que retorna]

## Usage Notes
- [Padrão importante 1]
- [Armadilha comum a evitar]
- [Consideração de thread safety se relevante]

## Examples
```java
// Exemplo de uso comum
ClassName instance = new ClassName();
instance.methodName();
```
```

## 📋 Checklist Rápido

Antes de gerar documentação, verifique:

- [ ] Overview tem 2-3 linhas explicando o propósito REAL da classe
- [ ] Cada field tem descrição que explica O QUE representa
- [ ] Cada método tem descrição que explica O QUE FAZ e QUANDO USAR
- [ ] Não há repetição de assinaturas (já auto-geradas)
- [ ] Não há descrições genéricas tipo "Executa X behavior"
- [ ] Usage Notes inclui informações ÚTEIS (padrões, armadilhas, thread safety)
- [ ] Examples mostram código REAL e COMPLETO
- [ ] Nenhuma seção estrutural duplicada (## Declaration, ## Methods sem "Descriptions", etc.)

## 🎨 Padrões por Tipo de Classe

### Manager/Service Class
```markdown
## Overview
Gerencia [recurso] provendo [funcionalidade]. Responsável por [ciclo de vida].

## Method Descriptions
- `get[Resource]()`: Retorna [recurso]. Acesso singleton thread-safe.
- `register[Thing]()`: Registra [coisa] com [sistema]. Deve ser chamado durante [fase].
```

### Event Class
```markdown
## Overview
Disparado quando [condição]. Permite plugins [reagir/modificar/cancelar] [comportamento].

## Method Descriptions
- `isCancelled()`: Retorna true se evento foi cancelado por handler.
- `setCancelled(boolean)`: Cancela evento, prevenindo [comportamento padrão].
```

### Configuration Class
```markdown
## Overview
Container de configuração para [sistema]. Carregado de [fonte] e aplicado durante [fase].

## Field Descriptions
- `[option]`: Controla [o que]. Padrão: [valor]. Valores válidos: [range].
```

### Utility Class
```markdown
## Overview
Classe utilitária com operações de [categoria]. Todos métodos são static e thread-safe.

## Method Descriptions
- `[operation]()`: [O que faz]. Útil para [caso de uso]. Complexidade: O([x]).
```

## 💡 Exemplos de Descrições EXCELENTES

### Campo
```markdown
- `MAX_PLAYERS`: Número máximo de jogadores concorrentes permitidos no servidor. Pode ser configurado via server.properties. Valores típicos: 20-100 para servidores pequenos, 100-1000 para grandes.
```

### Método
```markdown
- `shutdownServer(ShutdownReason reason)`: Desliga o servidor graciosamente com código de motivo específico. Desconecta todos os jogadores, salva dados dos mundos, descarrega plugins em ordem reversa e fecha conexões de rede. Bloqueia até shutdown completo. O motivo é logado e pode ser usado por sistemas de monitoramento para distinguir entre shutdown normal, crash e outras causas de terminação.
```

### Overview
```markdown
## Overview
Classe central do servidor que gerencia o ciclo de vida completo do Hytale, incluindo sequência de boot, gerenciamento de plugins, coordenação do event bus e procedimentos de shutdown gracioso. Atua como ponto de entrada principal para todas operações server-side e mantém a instância singleton acessível através do codebase.
```

## 🚀 Workflow para LLM

1. **Ler a classe Java** para entender estrutura
2. **Identificar propósito** principal da classe
3. **Escrever Overview** explicando o "porquê" existe
4. **Para cada campo público**: explicar o que representa
5. **Para cada construtor**: explicar o que inicializa e quando usar
6. **Para cada método público**: explicar comportamento, parâmetros, retorno, side effects
7. **Adicionar Usage Notes** com padrões importantes e armadilhas
8. **Incluir Examples** mostrando casos de uso reais
9. **Verificar** que NÃO há duplicação estrutural
10. **Validar** que descrições são úteis, não genéricas

## 📖 Arquivo de Referência Completo

Veja `EXAMPLE_CUSTOM_DOCS.md` para um exemplo completo e detalhado com todos os campos preenchidos corretamente.

## ⚡ Resposta Rápida para LLM

**Quando solicitado a criar documentação customizada:**

1. Use APENAS seções: Overview, Field Descriptions, Constructor Descriptions, Method Descriptions, Usage Notes, Examples
2. NÃO inclua: título da classe (# ClassName), Declaration, Methods sem "Descriptions"
3. Foque no "porquê" e "quando", não apenas no "o que"
4. Seja específico e útil, evite genéricos
5. Inclua side effects, thread safety, performance quando relevante
6. Exemplos devem ser código real e executável
7. Siga o formato exato mostrado acima

**Arquivo final deve parecer com isto:**

```markdown
## Overview
[2-3 linhas específicas]

## Field Descriptions
- `FIELD`: [Descrição útil]

## Constructor Descriptions
- `Ctor(params)`: [O que faz]

## Method Descriptions
- `method(params)`: [Comportamento útil]

## Usage Notes
[Informações importantes]

## Examples
```java
// Código real
```
```
