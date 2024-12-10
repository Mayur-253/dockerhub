# app.py
def main():
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    print("Here is the list of fruits:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

if __name__ == "__main__":
    main()
