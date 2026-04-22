import tkinter as tk
import random


class ColorPuzzlePro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Switch")
        self.root.geometry("350x500")
        self.root.configure(bg="#f0f3f5")

        self.size = 3
        self.colors = ["#3498db", "#e67e22"]  # Blue and Orange
        self.buttons = []
        self.moves = 0
        self.game_active = True

        self.setup_ui()
        self.setup_game()
        self.root.mainloop()

    def setup_ui(self):
        # Title and Instructions
        self.label = tk.Label(self.root, text="Match All Colors!",
                              font=("Helvetica", 16, "bold"), bg="#f0f3f5", fg="#2c3e50")
        self.label.pack(pady=15)

        # Move Counter
        self.move_label = tk.Label(self.root, text="Moves: 0",
                                   font=("Helvetica", 12), bg="#f0f3f5", fg="#7f8c8d")
        self.move_label.pack()

        # The Game Grid
        self.grid_frame = tk.Frame(self.root, bg="#bdc3c7", padx=5, pady=5)
        self.grid_frame.pack(pady=20)

        for r in range(self.size):
            row = []
            for c in range(self.size):
                btn = tk.Button(self.grid_frame, width=6, height=3, relief="flat",
                                command=lambda r=r, c=c: self.handle_click(r, c))
                btn.grid(row=r, column=c, padx=3, pady=3)
                row.append(btn)
            self.buttons.append(row)

        # Reset Button
        tk.Button(self.root, text="Restart Game", font=("Helvetica", 10, "bold"),
                  bg="#2ecc71", fg="white", relief="flat", padx=20,
                  command=self.setup_game).pack(pady=10)

    def setup_game(self):
        """Resets the board to a solvable scrambled state."""
        self.moves = 0
        self.game_active = True
        self.move_label.config(text="Moves: 0")
        self.label.config(text="Match All Colors!", fg="#2c3e50")

        # Reset all to first color
        for row in self.buttons:
            for b in row:
                b.config(bg=self.colors[0], state="normal")

        # Scramble the board with 5 random valid moves
        for _ in range(5):
            self.toggle_colors(random.randint(0, 2), random.randint(0, 2))

    def handle_click(self, r, c):
        """User interaction logic."""
        if not self.game_active:
            return

        self.moves += 1
        self.move_label.config(text=f"Moves: {self.moves}")
        self.toggle_colors(r, c)
        self.check_win()

    def toggle_colors(self, r, c):
        """The core 'plus-sign' switch logic."""
        for dr, dc in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                btn = self.buttons[nr][nc]
                new_col = self.colors[1] if btn.cget("bg") == self.colors[0] else self.colors[0]
                btn.config(bg=new_col)

    def check_win(self):
        """Checks if all buttons match the top-left button."""
        target = self.buttons[0][0].cget("bg")
        if all(b.cget("bg") == target for row in self.buttons for b in row):
            self.game_active = False
            self.label.config(text="🎉 YOU WIN!", fg="#27ae60")
            # Briefly disable buttons to signify the end
            for row in self.buttons:
                for b in row: b.config(state="disabled")


if __name__ == "__main__":
    ColorPuzzlePro()