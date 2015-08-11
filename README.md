# FootyPlayerAPI
This project utilizes the Django REST framework to create a simple API about football (soccer) players

## Endpoints
### Players
  * GET `/players/`
    Returns a list of players in the database

    For example,
    ```json
    {
     [
      {
       id: 1,
       first_name: "Mesut",
       last_name: "Ozil",
       age: 25,
       club: "Arsenal F.C.",
       country: "Germany",
       position: "CAM",
       kit_number: 11
      },
      {
       id: 2,
       first_name: "Alexis",
       last_name: "Sanchez",
       age: 25,
       club: "Arsenal F.C.",
       country: "Chile",
       position: "LW",
       kit_number: 17
      }
     ]
    }
    ```

  * GET `/players/:id/`
    Returns a player based on the provided id
