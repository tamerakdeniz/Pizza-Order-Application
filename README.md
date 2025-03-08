# 🍕 Pizza Order Application

A simple Python-based command-line interface for ordering pizzas with customizable toppings and sizes.

## 🎯 Features

- Choose pizza size (Small, Medium, Large)
- Add pepperoni topping option
- Extra cheese option
- Input validation
- Detailed order summary
- Price calculation based on selections

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/tamerakdeniz/Pizza-Order-Application.git

cd Pizza-Order-Application
```

2. Ensure you have Python installed (3.6 or higher)
```bash
python --version
```

## 🚀 Usage

Run the application:
```bash
python main.py
```

Follow the prompts to:
- Select pizza size (S/M/L)
- Choose pepperoni topping (Y/N)
- Add extra cheese (Y/N)

## 💰 Price List

Base Pizza Prices:
- Small (S): $15
- Medium (M): $20
- Large (L): $25

Additional Toppings:
- Pepperoni on Small: +$2
- Pepperoni on Medium/Large: +$3
- Extra Cheese: +$1

## 📝 Example Output

```
Welcome to Python Pizza Deliveries!
-----------------------------------
What size pizza do you want? (S/M/L): M
Do you want pepperoni? (Y/N): Y
Do you want extra cheese? (Y/N): Y

=== Order Summary ===
Size: Medium
Pepperoni: Yes
Extra Cheese: Yes
Total Bill: $24.00
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
