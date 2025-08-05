import tkinter as tk
from tkinter import ttk, font
import math
import random
from datetime import datetime


class SophisticatedCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✨ Cute Calculator Pro ✨")
        self.root.geometry("420x700")
        self.root.resizable(False, False)

        # Calculator state
        self.expression = ""
        self.history = []
        self.memory_value = 0
        self.theme_index = 0

        # Cute themes with proper hex colors
        self.themes = [
            {"name": "Cotton Candy", "bg": "#FFE4E6", "accent": "#FF69B4", "text": "#4A4A4A", "button": "#FFB6E1"},
            {"name": "Ocean Dream", "bg": "#E0F6FF", "accent": "#4169E1", "text": "#2F4F4F", "button": "#87CEEB"},
            {"name": "Sunset Vibes", "bg": "#FFF0E6", "accent": "#FF6347", "text": "#8B4513", "button": "#FFE4B5"},
            {"name": "Forest Magic", "bg": "#F0FFF0", "accent": "#32CD32", "text": "#2E8B57", "button": "#98FB98"},
            {"name": "Galaxy Night", "bg": "#2D1B69", "accent": "#E94560", "text": "#F5F5F5", "button": "#4A4A7C"}
        ]

        # Cute messages for different operations
        self.cute_messages = [
            "Calculating cuteness... 🎀",
            "Math magic in progress! ✨",
            "Numbers are dancing! 💃",
            "Computing with love! 💖",
            "Sparkles and equations! ⭐",
            "Crunching numbers! 🍪",
            "Mathematical wizardry! 🧙‍♀️"
        ]

        # Success messages
        self.success_messages = [
            "Perfect! ✨", "Nailed it! 🎯", "Math genius! 🧠",
            "Beautiful! 💖", "Fantastic! 🌟", "Amazing! 🎉"
        ]

        # Apply initial theme
        self.current_theme = self.themes[self.theme_index]
        self.root.configure(bg=self.current_theme["bg"])

        # Create UI
        self.create_title_bar()
        self.create_display()
        self.create_buttons()
        self.create_footer()

        # Bind events
        self.bind_keyboard()

        # Initialize stats
        self.calc_count = 0
        self.update_footer()

    def create_title_bar(self):
        """Create a custom title bar with theme switcher"""
        title_frame = tk.Frame(self.root, bg=self.current_theme["button"], height=50, relief='raised', bd=2)
        title_frame.pack(fill=tk.X, padx=5, pady=5)
        title_frame.pack_propagate(False)

        # App title with cute styling
        title_label = tk.Label(title_frame,
                               text="✨ Cute Calculator Pro ✨",
                               font=('Comic Sans MS', 16, 'bold'),
                               fg=self.current_theme["accent"],
                               bg=self.current_theme["button"])
        title_label.pack(side=tk.LEFT, padx=15, pady=10)

        # Theme button
        self.theme_btn = tk.Button(title_frame,
                                   text=f"🎨 {self.current_theme['name']}",
                                   font=('Arial', 9, 'bold'),
                                   bg=self.current_theme["accent"],
                                   fg='white',
                                   bd=0,
                                   padx=12,
                                   pady=5,
                                   command=self.switch_theme,
                                   cursor='hand2',
                                   relief='raised')
        self.theme_btn.pack(side=tk.RIGHT, padx=10, pady=10)

        # Memory indicator
        self.memory_label = tk.Label(title_frame,
                                     text="💾 M: 0",
                                     font=('Arial', 10, 'bold'),
                                     fg=self.current_theme["text"],
                                     bg=self.current_theme["button"])
        self.memory_label.pack(side=tk.RIGHT, padx=10, pady=10)

    def create_display(self):
        """Create the sophisticated display area"""
        # Main display container
        display_frame = tk.Frame(self.root, bg='white', relief='sunken', bd=3)
        display_frame.pack(fill=tk.X, padx=10, pady=5)

        # Status message area
        status_frame = tk.Frame(display_frame, bg='#F8F9FA', height=25)
        status_frame.pack(fill=tk.X, padx=5, pady=(5, 0))
        status_frame.pack_propagate(False)

        self.status_var = tk.StringVar()
        self.status_var.set("Ready to calculate! 🎀")

        self.status_label = tk.Label(status_frame,
                                     textvariable=self.status_var,
                                     font=('Arial', 10, 'italic'),
                                     fg=self.current_theme["accent"],
                                     bg='#F8F9FA')
        self.status_label.pack(pady=3)

        # History display
        history_frame = tk.Frame(display_frame, bg='#E8F4FD', height=30)
        history_frame.pack(fill=tk.X, padx=5, pady=2)
        history_frame.pack_propagate(False)

        self.history_var = tk.StringVar()
        self.history_label = tk.Label(history_frame,
                                      textvariable=self.history_var,
                                      font=('Consolas', 11),
                                      fg='#4169E1',
                                      bg='#E8F4FD',
                                      anchor='e')
        self.history_label.pack(fill=tk.X, padx=10, pady=5)

        # Main calculation display
        calc_frame = tk.Frame(display_frame, bg='#FAFAFA', height=60)
        calc_frame.pack(fill=tk.X, padx=5, pady=2)
        calc_frame.pack_propagate(False)

        self.input_var = tk.StringVar()
        self.input_var.set("0")

        # Create custom font for display
        display_font = font.Font(family='Consolas', size=24, weight='bold')

        self.main_display = tk.Label(calc_frame,
                                     textvariable=self.input_var,
                                     font=display_font,
                                     fg=self.current_theme["text"],
                                     bg='#FAFAFA',
                                     anchor='e')
        self.main_display.pack(fill=tk.BOTH, padx=15, pady=10)

        # Options frame
        options_frame = tk.Frame(display_frame, bg='white', height=30)
        options_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        options_frame.pack_propagate(False)

        self.sci_mode = tk.BooleanVar()
        sci_check = tk.Checkbutton(options_frame,
                                   text="🔬 Scientific Mode",
                                   variable=self.sci_mode,
                                   font=('Arial', 9),
                                   fg=self.current_theme["text"],
                                   bg='white',
                                   selectcolor=self.current_theme["button"],
                                   activebackground='white')
        sci_check.pack(side=tk.LEFT, padx=10, pady=5)

        # Add cute animation indicator
        self.animation_label = tk.Label(options_frame,
                                        text="",
                                        font=('Arial', 12),
                                        fg=self.current_theme["accent"],
                                        bg='white')
        self.animation_label.pack(side=tk.RIGHT, padx=10, pady=5)

    def create_buttons(self):
        """Create the sophisticated button layout"""
        # Button container with padding
        button_container = tk.Frame(self.root, bg=self.current_theme["bg"])
        button_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Configure grid weights
        for i in range(7):
            button_container.grid_rowconfigure(i, weight=1, minsize=55)
        for i in range(5):
            button_container.grid_columnconfigure(i, weight=1, minsize=75)

        # Enhanced button configuration with better organization
        button_configs = [
            # Row 0: Memory functions
            [('MC', '#FF69B4', self.memory_clear, '🗑️', 'Clear memory'),
             ('MR', '#FF69B4', self.memory_recall, '📥', 'Recall memory'),
             ('M+', '#FF69B4', self.memory_add, '➕', 'Add to memory'),
             ('M-', '#FF69B4', self.memory_subtract, '➖', 'Subtract from memory'),
             ('sin', '#9370DB', lambda: self.trig_function('sin'), '📐', 'Sine function')],

            # Row 1: Advanced functions
            [('cos', '#9370DB', lambda: self.trig_function('cos'), '📐', 'Cosine function'),
             ('tan', '#9370DB', lambda: self.trig_function('tan'), '📐', 'Tangent function'),
             ('log', '#9370DB', lambda: self.scientific_function('log'), '📊', 'Logarithm base 10'),
             ('ln', '#9370DB', lambda: self.scientific_function('ln'), '📈', 'Natural logarithm'),
             ('!', '#9370DB', self.factorial, '❗', 'Factorial')],

            # Row 2: Basic functions
            [('C', '#FFA500', self.clear, '🧹', 'Clear all'),
             ('⌫', '#FFA500', self.backspace, '⬅️', 'Backspace'),
             ('%', '#FFA500', self.percentage, '💯', 'Percentage'),
             ('÷', '#FF6347', lambda: self.press('/'), '➗', 'Division'),
             ('√', '#32CD32', self.square_root, '✨', 'Square root')],

            # Row 3: Numbers 7-9
            [('7', '#87CEEB', lambda: self.press('7'), '7️⃣', 'Seven'),
             ('8', '#87CEEB', lambda: self.press('8'), '8️⃣', 'Eight'),
             ('9', '#87CEEB', lambda: self.press('9'), '9️⃣', 'Nine'),
             ('×', '#FF6347', lambda: self.press('*'), '✖️', 'Multiplication'),
             ('x²', '#32CD32', self.square, '²️⃣', 'Square')],

            # Row 4: Numbers 4-6
            [('4', '#87CEEB', lambda: self.press('4'), '4️⃣', 'Four'),
             ('5', '#87CEEB', lambda: self.press('5'), '5️⃣', 'Five'),
             ('6', '#87CEEB', lambda: self.press('6'), '6️⃣', 'Six'),
             ('−', '#FF6347', lambda: self.press('-'), '➖', 'Subtraction'),
             ('xʸ', '#32CD32', lambda: self.press('**'), '🔢', 'Power')],

            # Row 5: Numbers 1-3
            [('1', '#87CEEB', lambda: self.press('1'), '1️⃣', 'One'),
             ('2', '#87CEEB', lambda: self.press('2'), '2️⃣', 'Two'),
             ('3', '#87CEEB', lambda: self.press('3'), '3️⃣', 'Three'),
             ('+', '#FF6347', lambda: self.press('+'), '➕', 'Addition'),
             ('π', '#32CD32', lambda: self.press_constant('pi'), '🥧', 'Pi constant')],

            # Row 6: Bottom row
            [('±', '#98FB98', self.sign_change, '🔄', 'Change sign'),
             ('0', '#87CEEB', lambda: self.press('0'), '0️⃣', 'Zero'),
             ('.', '#87CEEB', lambda: self.press('.'), '⚫', 'Decimal point'),
             ('=', '#00CED1', self.calculate, '🎯', 'Calculate result'),
             ('e', '#32CD32', lambda: self.press_constant('e'), '📏', 'Euler constant')]
        ]

        # Create buttons with enhanced styling
        self.buttons = []
        for row_idx, row in enumerate(button_configs):
            button_row = []
            for col_idx, (text, color, command, emoji, tooltip) in enumerate(row):
                # Create button with modern styling
                btn = tk.Button(button_container,
                                text=f"{emoji}\n{text}",
                                font=('Arial', 9, 'bold'),
                                bg=color,
                                fg='white',
                                bd=2,
                                relief='raised',
                                command=command,
                                cursor='hand2',
                                activebackground=self.lighten_color(color),
                                activeforeground='white')

                btn.grid(row=row_idx, column=col_idx, sticky='nsew', padx=1, pady=1)

                # Add hover effects
                btn.bind('<Enter>', lambda e, b=btn, c=color: self.on_button_hover(b, c))
                btn.bind('<Leave>', lambda e, b=btn, c=color: self.on_button_leave(b, c))

                # Add tooltip effect (simplified)
                btn.bind('<Button-1>', lambda e, msg=tooltip: self.show_button_feedback(msg))

                button_row.append(btn)
            self.buttons.append(button_row)

    def create_footer(self):
        """Create footer with statistics and cute info"""
        footer_frame = tk.Frame(self.root, bg=self.current_theme["button"], height=35, relief='raised', bd=1)
        footer_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        footer_frame.pack_propagate(False)

        self.footer_var = tk.StringVar()

        footer_label = tk.Label(footer_frame,
                                textvariable=self.footer_var,
                                font=('Arial', 10, 'bold'),
                                fg=self.current_theme["text"],
                                bg=self.current_theme["button"])
        footer_label.pack(pady=8)

        # Add time display
        self.update_time()

    def update_time(self):
        """Update time display"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.root.after(1000, self.update_time)

    def update_footer(self):
        """Update footer with stats"""
        self.footer_var.set(f"🎀 Calculations: {self.calc_count} | Ready for math magic! ✨")

    def lighten_color(self, color):
        """Create a lighter version of a color for hover effects"""
        # Simple color lightening - convert hex to RGB, lighten, convert back
        color = color.lstrip('#')
        if len(color) == 6:
            try:
                rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
                lighter_rgb = tuple(min(255, int(c * 1.3)) for c in rgb)
                return f"#{lighter_rgb[0]:02x}{lighter_rgb[1]:02x}{lighter_rgb[2]:02x}"
            except:
                return color
        return color

    def on_button_hover(self, button, original_color):
        """Enhanced hover effect"""
        lighter_color = self.lighten_color(original_color)
        button.configure(bg=lighter_color, relief='raised', bd=3)

        # Add subtle animation
        self.animation_label.config(text="✨")

    def on_button_leave(self, button, original_color):
        """Reset button after hover"""
        button.configure(bg=original_color, relief='raised', bd=2)
        self.animation_label.config(text="")

    def show_button_feedback(self, message):
        """Show feedback when button is pressed"""
        original_status = self.status_var.get()
        self.status_var.set(f"Pressed: {message} 🎯")
        self.root.after(800, lambda: self.status_var.set(original_status))

    def switch_theme(self):
        """Switch between themes with smooth transition"""
        self.theme_index = (self.theme_index + 1) % len(self.themes)
        self.current_theme = self.themes[self.theme_index]

        # Update all components with new theme
        self.root.configure(bg=self.current_theme["bg"])
        self.theme_btn.config(text=f"🎨 {self.current_theme['name']}")

        # Show theme change message
        self.status_var.set(f"Switched to {self.current_theme['name']} theme! 🎨✨")
        self.root.after(2500, lambda: self.status_var.set("Ready to calculate! 🎀"))

    def press(self, value):
        """Enhanced input handling with cute feedback"""
        if self.input_var.get() == "0" and value.isdigit():
            self.expression = ""

        self.expression += str(value)
        self.update_display()

        # Show random cute message occasionally
        if random.random() < 0.15:  # 15% chance
            message = random.choice(self.cute_messages)
            self.status_var.set(message)
            self.root.after(1200, lambda: self.status_var.set("Ready to calculate! 🎀"))

    def press_constant(self, constant):
        """Add mathematical constants"""
        constants = {'pi': math.pi, 'e': math.e}
        value = str(constants[constant])

        if self.input_var.get() == "0":
            self.expression = ""

        self.expression += value
        self.update_display()
        self.status_var.set(f"Added {constant}! 🔢✨")
        self.root.after(1500, lambda: self.status_var.set("Ready to calculate! 🎀"))

    def calculate(self):
        """Enhanced calculation with celebration"""
        if not self.expression:
            return

        try:
            # Evaluate the expression
            result = eval(self.expression)

            # Format result based on scientific mode
            if self.sci_mode.get() and (abs(result) >= 1e6 or (abs(result) < 1e-3 and result != 0)):
                formatted_result = f"{result:.3e}"
            else:
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 10)
                formatted_result = str(result)

            # Update displays
            self.history_var.set(f"{self.expression} = {formatted_result}")
            self.input_var.set(formatted_result)
            self.expression = str(result)

            # Update statistics
            self.calc_count += 1
            self.update_footer()

            # Show success message
            success_msg = random.choice(self.success_messages)
            self.status_var.set(success_msg)
            self.root.after(2000, lambda: self.status_var.set("Ready for more math! 🎀"))

        except ZeroDivisionError:
            self.show_error("Oops! Can't divide by zero! 🙈")
        except Exception:
            self.show_error("Something went wrong! 😅")

    def clear(self):
        """Clear everything with cute animation"""
        self.expression = ""
        self.input_var.set("0")
        self.history_var.set("")
        self.status_var.set("All clean and sparkly! 🧹✨")
        self.root.after(1500, lambda: self.status_var.set("Ready to calculate! 🎀"))

    def backspace(self):
        """Remove last character"""
        if self.expression:
            self.expression = self.expression[:-1]
            self.update_display()
            if random.random() < 0.3:
                self.status_var.set("Fixed that for you! ⬅️")

    def percentage(self):
        """Calculate percentage"""
        try:
            current_value = eval(self.expression) if self.expression else 0
            result = current_value / 100
            self.expression = str(result)
            self.update_display()
            self.status_var.set("Percentage magic! 💯✨")
        except:
            self.show_error("Need a number for percentage! 💯")

    def sign_change(self):
        """Change the sign of current number"""
        try:
            if self.expression:
                current_value = eval(self.expression)
                self.expression = str(-current_value)
                self.update_display()
                self.status_var.set("Sign flipped! 🔄")
        except:
            if self.expression.startswith('-'):
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
            self.update_display()

    def square_root(self):
        """Calculate square root"""
        try:
            current_value = eval(self.expression) if self.expression else 0
            if current_value < 0:
                self.show_error("Can't √ negative numbers! 😅")
                return

            result = math.sqrt(current_value)
            self.history_var.set(f"√{current_value} = {result}")
            self.expression = str(result)
            self.update_display()
            self.status_var.set("Square root sparkles! ✨")
        except:
            self.show_error("Need a number for square root! ✨")

    def square(self):
        """Calculate square"""
        try:
            current_value = eval(self.expression) if self.expression else 0
            result = current_value ** 2
            self.history_var.set(f"{current_value}² = {result}")
            self.expression = str(result)
            self.update_display()
            self.status_var.set("Squared it perfectly! ²")
        except:
            self.show_error("Need a number to square! ²")

    def factorial(self):
        """Calculate factorial"""
        try:
            num = int(eval(self.expression))
            if num < 0:
                self.show_error("Factorial needs positive numbers! 😊")
                return
            if num > 20:
                self.show_error("That's too big for factorial! 😵")
                return

            result = math.factorial(num)
            self.history_var.set(f"{num}! = {result}")
            self.input_var.set(str(result))
            self.expression = str(result)
            self.status_var.set("Factorial magic! ❗✨")
        except:
            self.show_error("Factorial needs whole numbers! 🤔")

    def trig_function(self, func):
        """Trigonometric functions"""
        try:
            value = eval(self.expression) if self.expression else 0
            funcs = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan
            }

            # Convert to radians for calculation
            result = funcs[func](math.radians(value))
            result = round(result, 10)  # Avoid floating point errors

            self.history_var.set(f"{func}({value}°) = {result}")
            self.input_var.set(str(result))
            self.expression = str(result)
            self.status_var.set(f"Trigonometry magic! 📐✨")
        except:
            self.show_error(f"Need a number for {func}! 📐")

    def scientific_function(self, func):
        """Scientific functions (log, ln)"""
        try:
            value = eval(self.expression) if self.expression else 0
            if value <= 0:
                self.show_error(f"{func.upper()} needs positive numbers! 📊")
                return

            if func == 'log':
                result = math.log10(value)
            elif func == 'ln':
                result = math.log(value)

            result = round(result, 10)
            self.history_var.set(f"{func}({value}) = {result}")
            self.input_var.set(str(result))
            self.expression = str(result)
            self.status_var.set("Science power! 🔬✨")
        except:
            self.show_error(f"Error in {func} calculation! 🧪")

    def memory_clear(self):
        """Clear memory"""
        self.memory_value = 0
        self.memory_label.config(text="💾 M: 0")
        self.status_var.set("Memory cleared! 🗑️")

    def memory_recall(self):
        """Recall from memory"""
        self.expression = str(self.memory_value)
        self.input_var.set(str(self.memory_value))
        self.status_var.set("Memory recalled! 📥")

    def memory_add(self):
        """Add to memory"""
        try:
            current_value = eval(self.expression) if self.expression else 0
            self.memory_value += current_value
            self.memory_label.config(text=f"💾 M: {self.memory_value}")
            self.status_var.set("Added to memory! ➕")
        except:
            self.show_error("Can't add to memory! 😅")

    def memory_subtract(self):
        """Subtract from memory"""
        try:
            current_value = eval(self.expression) if self.expression else 0
            self.memory_value -= current_value
            self.memory_label.config(text=f"💾 M: {self.memory_value}")
            self.status_var.set("Subtracted from memory! ➖")
        except:
            self.show_error("Can't subtract from memory! 😅")

    def update_display(self):
        """Update the main display"""
        if self.expression == "":
            self.input_var.set("0")
        else:
            # Format display nicely
            display_expr = self.expression.replace('*', '×').replace('/', '÷')
            if display_expr.startswith('-'):
                display_expr = '−' + display_expr[1:]
            self.input_var.set(display_expr)

    def show_error(self, message):
        """Show error with cute styling"""
        self.input_var.set(message)
        self.expression = ""
        # Auto-clear error after 3 seconds
        self.root.after(3000, lambda: (
            self.input_var.set("0"),
            self.status_var.set("Ready to try again! 🎀")
        ))

    def bind_keyboard(self):
        """Bind keyboard shortcuts"""
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()

    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key.isdigit() or key in '+-*/.':
            self.press(key)
        elif key == '\r' or key == '=':
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape':
            self.clear()
        elif key == 't':  # Secret theme switcher
            self.switch_theme()

    def run(self):
        """Start the calculator"""
        self.root.mainloop()


# Create and run the calculator
if __name__ == "__main__":
    calculator = SophisticatedCalculator()
    calculator.run()