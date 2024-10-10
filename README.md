# Coffee Machine Simulation

This Python script simulates the functionality of a coffee machine, allowing users to select drinks, check resources, and process payments. It utilizes predefined classes for menu management, coffee making, and handling money transactions.

## Features
- **Drink Selection**: Users can choose from the available menu items.
- **Resource Management**: The machine checks if there are enough ingredients to make the selected drink.
- **Payment Processing**: The machine handles payment for each drink selected.
- **Reports**: Users can request a report showing the remaining resources and total money collected.

## How It Works

1. **Menu Management**:  
   The `Menu` class manages the list of available drinks and their prices.
   
2. **Coffee Maker**:  
   The `CoffeeMaker` class handles the resources (water, coffee, milk) and prepares drinks.
   
3. **Money Handling**:  
   The `MoneyMachine` class processes payments and keeps track of the total amount collected.

4. **User Input**:  
   The user can interact with the machine by entering drink choices or commands such as "report" (to show resources) or "off" (to turn off the machine).

## Classes Used

- `Menu`: Manages available drinks.
- `MenuItem`: Represents a specific drink on the menu.
- `CoffeeMaker`: Manages resources and handles the making of drinks.
- `MoneyMachine`: Handles payment transactions.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/coffee-machine-simulator.git
   cd coffee-machine-simulator
   ```

2. **Install Dependencies**:
   This code assumes you have the `menu.py`, `coffee_maker.py`, and `money_machine.py` files, which define the necessary classes.

3. **Run the Script**:
   ```bash
   python main.py
   ```

## User Commands

- **Drink Selection**:  
   The user can choose a drink by typing its name (e.g., "latte", "espresso").
   
- **Check Resources**:  
   Type `report` to get a report on the remaining resources and total money collected.
   
- **Turn Off Machine**:  
   Type `off` to shut down the coffee machine.

## Example Usage

```text
What would you like? (espresso/latte/cappuccino)
> latte
Insert coins:
> 2
Enjoy your latte!

What would you like? (espresso/latte/cappuccino)
> report
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $2.50
```

## Future Enhancements
- Add more drink options to the menu.
- Implement a GUI for better user interaction.
- Add support for customization (e.g., extra shots of espresso, milk options).

## License
This project is licensed under the MIT License.