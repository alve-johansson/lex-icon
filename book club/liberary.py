from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Bibliotekets böcker")

table.add_column("Titel", style="cyan", no_wrap=True)
table.add_column("Författare", style="magenta")
table.add_column("Kopior", justify="right", style="green")

table.add_row("Dune", "Frank Herbert", "3")
table.add_row("1984", "George Orwell", "1")

console.print(table)

""" 

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product 4) Change stock 0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)                    
        elif choice == "0":
            break
    conn.close()


main() """