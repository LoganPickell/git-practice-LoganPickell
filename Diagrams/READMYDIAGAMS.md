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

```mermaid
flowchart TD
    %% Start Point
    A[Start] --> B[User Logs In]

    %% Role Decision
    B --> C{User Role?}
    C -->|Admin| D[Admin Dashboard]
    C -->|User| E[User Dashboard]

    %% User Dashboard Actions
    E --> F[Manage Decks]
    F -->|View| F1[View Cards in Deck]
    F -->|Create/Edit/Remove| F2[Modify Deck]
    E --> K[Request New Card]

    %% Admin Actions
    D --> N[Manage Users]
    D --> M[Admin Approval Process]

    %% Card Request linked to Admin Approval
    K --> M

    %% Approval Decision
    M --> M1{Approval Decision}
    M1 -->|Approve| O[Card Added to Database]
    M1 -->|Reject| P[Card Denied & Reviewed]

    %% End Point
    O --> V[End]
    P --> V
    F1 --> V
    F2 --> V
    N --> V

    %% Styling
    style A fill:#b3e0ff,stroke:#0066cc,stroke-width:2px, color:000000
    style B fill:#ffcccb,stroke:#cc3333,stroke-width:2px, color:000000
    style C fill:#ffffcc,stroke:#ffcc00,stroke-width:2px, color:000000
    style E fill:#d9f7ff,stroke:#3399ff,stroke-width:2px, color:000000
    style F fill:#e6f7ff,stroke:#3399ff,stroke-width:2px, color:000000
    style D fill:#ffccff,stroke:#9933cc,stroke-width:2px, color:000000
    style N fill:#f7ccff,stroke:#cc66cc,stroke-width:2px, color:000000
    style M fill:#d9f7d9,stroke:#66cc66,stroke-width:2px, color:000000
    style M1 fill:#ffff99,stroke:#ffcc00,stroke-width:2px, color:000000
    style O fill:#c9f7c9,stroke:#66cc66,stroke-width:2px, color:000000
    style P fill:#f7c9c9,stroke:#cc6666,stroke-width:2px, color:000000
    style V fill:#f2f2f2,stroke:#cccccc,stroke-width:2px, color:000000

    %% Role-Based Styling with classDef
    classDef user fill:#d9f7ff,stroke:#3399ff,stroke-width:2px;
    classDef admin fill:#ffccff,stroke:#9933cc,stroke-width:2px;

    %% Apply role-based classes explicitly
    class E,F1,F2,K user; 
    class D,N,M admin;     

```

---

## System Architecture Diagram

## API Endpoints Table