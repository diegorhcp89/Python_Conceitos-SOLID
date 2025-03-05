# Python_Conceitos-SOLID

# Projeto de Estruturas de Código em Python

## Descrição
Este repositório contém diversas implementações em Python demonstrando os princípios do SOLID, aplicados a diferentes cenários de desenvolvimento de software.

## Princípios SOLID Aplicados

### 1. **Single Responsibility Principle (SRP)**
Cada classe no projeto tem uma única responsabilidade:
- `Process`: Gerencia o cadastro de usuários.
- `Company`: Gerencia a execução de diferentes tipos de funcionários.
- `ClientService`: Responsável por enviar notificações.

### 2. **Open/Closed Principle (OCP)**
As classes podem ser estendidas sem modificar seu código original:
- A classe `Animal` pode ser estendida por `Felino` e `Leao`.
- `NotificatorInterface` permite adicionar novos métodos de notificação sem modificar `ClientService`.

### 3. **Liskov Substitution Principle (LSP)**
Subtipos podem substituir seus tipos base sem alterar o comportamento esperado:
- `Leao` e `Felino` herdam de `Animal` e podem ser usados na classe `Pessoa` sem modificar sua implementação.
- `NotificatorEmail` e `NotificatorSMS` seguem a mesma interface, garantindo que `ClientService` possa utilizá-los sem distinção.

### 4. **Interface Segregation Principle (ISP)**
Cada interface possui apenas os métodos necessários para sua funcionalidade específica:
- `DocumentPDF`, `DocumentTXT` e `DocumentExcel` implementam apenas os métodos relevantes, evitando interfaces inchadas.

### 5. **Dependency Inversion Principle (DIP)**
Módulos de alto nível não dependem de módulos de baixo nível, mas de abstrações:
- `ClientService` depende da abstração `NotificatorInterface`, permitindo flexibilidade na adição de novos notificadores sem alterar seu código.

## Tecnologias Utilizadas
- Python 3
- Programação Orientada a Objetos
- Padrões de Design (Abstração, Injeção de Dependência, Polimorfismo)

## Como Executar
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-repositorio.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd seu-repositorio
   ```
3. Execute os scripts conforme necessário:
   ```sh
   python3 nome_do_arquivo.py
   ```

## Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorias e sugestões.

## Licença
Este projeto está sob a licença MIT.

