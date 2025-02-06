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



```

---

## System Architecture Diagram

```mermaid
graph TB
    subgraph Frontend
        A[User Interface] --> B[Card Display]
        A --> C[Deck Management]
        A --> D[Card Submission]
        A -->|Authenticate User| E[Authentication Service]
    end

    subgraph Backend
        B -->|Fetch Cards| F[Database]
        C -->|Manage Decks| F
        D -->|Submit Card| F
    end


    subgraph AccessControl
        G[User Role: Regular User] -->|Access Cards, Manage Deck| A
        H[User Role: Admin] -->|Manage Cards| B
        H -->|Approve Card Submissions| D
    end


    E -->|User Data| F

    class A,B,C,D frontendClass;
    class F backendClass;
    class E,G,H databaseClass;
    class G,H accessControlClass;



```

## API Endpoints Table

| **Endpoint**                 | **HTTP Method** | **Description**                     | **Authentication/Authorization** |
|-----------------------------|-----------------|-------------------------------------|----------------------------------|
| `/api/cards`                | `GET`           | Fetch all cards                     | Public       |
| `/api/cards/{id}`           | `GET`           | Fetch card by ID                    | Public       |
| `/api/cards`                | `POST`          | Submit new card                     | Authenticated User (Submitter)  |
| `/api/cards/{id}`           | `PUT`           | Modify existing card                | Admin (Authorization required)  |
| `/api/cards/{id}`           | `DELETE`        | Delete a card                       | Admin (Authorization required)  |
| `/api/decks`                | `POST`          | Create a new deck                   | Authenticated User (Deck Creator) |
| `/api/decks/{id}`           | `GET`           | Fetch a specific deck               | Authenticated User (Deck Owner) |
| `/api/decks/{id}`           | `PUT`           | Modify a deck                       | Authenticated User (Deck Owner) |
| `/api/decks/{id}`           | `DELETE`        | Delete a deck                       | Authenticated User (Deck Owner) |
| `/api/auth/login`           | `POST`          | User login                          | Public (No authentication)      |
| `/api/auth/logout`          | `POST`          | User logout                         | Authenticated User (Logged-in)  |
