import tkinter as tk

class PaymentReceiptGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment Receipt Generator")
        

        # Variables to store input values
        self.customer_name_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.payment_method_var = tk.StringVar()

        # Create and pack widgets
        tk.Label(root, text="Customer Name:").pack(pady=5)
        tk.Entry(root, textvariable=self.customer_name_var).pack(pady=5)

        tk.Label(root, text="Amount:").pack(pady=5)
        tk.Entry(root, textvariable=self.amount_var).pack(pady=5)

        tk.Label(root, text="Payment Method:").pack(pady=5)
        tk.Entry(root, textvariable=self.payment_method_var).pack(pady=5)

        tk.Button(root, text="Generate Receipt", command=self.generate_receipt).pack(pady=10)

    def generate_receipt(self):
        customer_name = self.customer_name_var.get()
        amount = self.amount_var.get()
        payment_method = self.payment_method_var.get()

        receipt_text = f"Receipt\n\nCustomer Name: {customer_name}\nAmount: ${amount:.2f}\nPayment Method: {payment_method}"

        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Payment Receipt")

        receipt_label = tk.Label(receipt_window, text=receipt_text, font=("Arial", 12))
        receipt_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    receipt_generator = PaymentReceiptGenerator(root)
    root.mainloop()
