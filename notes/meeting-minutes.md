# (Week 3)
- Role allocation
- Rough scenario
- Assigned:
  - Use cases (Jonathan)
  - GUI prototypes (Bob)
  - DevOps project/workflow set up (Oliver)

# Tuesday 14 Feb (Week 4)
- JJs Lab comments:
  - See Chesman and daniels, UML components, Chapter 4
    - Hotel reservation example
      - components and interfaces
      - use cases/requirements
  - Find examples online, choose best
  - Performance with 1000's of users, chain of hotels
- Discussion of scenario
- Using Python, Flask as web framework, SQL

# Friday 16 Feb (Week 4)
- Set goal on the issues board for next meeting
- Refined scenario
  #### Scenario: Hotel booking system

    - Role based (Actors)
      - Customer, managers, clerks, etc
    - Book room (see use cases)
      - Check if available
      - Offer an alternative
      - Assign room numbers
      - Special requirements for a user
      - Transactions
    - Cancel booking
    - Modify booking
    - Self service/reception

    - Multiple hotels (chain)
    - Shared DB, separated as schemas
      - Possible to move one or more schemas to another server/DB
        - Store DB info in configuration for each hotel
    - Backend separate from frontend
      - (Python) API exposed to frontend component
      - REST API exposed for other clients e.g. POS
      - MVC
    - JSON config
      - DB endpoint
      - Hotel config
        - Defaults
          - Room layouts
          - etc
      - 'Builds' the hotel(s) from a template

# Tuesday 21 Feb (Week 5)
Assigned tasks for sections 7 and 8


# Thursday 23 Feb (Week 5)
Discussion on candidate classes
