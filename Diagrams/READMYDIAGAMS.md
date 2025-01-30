# <p align="center">Diagrams</p>

## Entity Relationship Diagram

```mermaid


erDiagram
    USER ||--o{ DECK : owns
    USER {
        string userId PK
        string username
        string role
    }

    DECK ||--o{ CARD : contains
    DECK {
        string deckId PK
        string deckName
        date creationDate
    }

    CARD {
        string cardId PK
        string pokemonName
        string type
        string rarity
        int attack
        int defense
    }

    ADMIN ||--o{ USER : manages
    ADMIN ||--o{ CARD : approves
    ADMIN {
        string adminId PK
        string adminName
    }

    "Approval-System" ||--o{ CARD : pendingApproval
    "Approval-System" {
        string approvalId PK
        string status
    }
    
    CARD ||--o{ "Approval-System" : requires

```

---

## User Flow Diagram
