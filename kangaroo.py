class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        result = "Kangaroo pouch contents:\n"
        for item in self.pouch_contents:
            result += f"  {str(item)}\n"
        return result.strip()


def main():
    kanga = Kangaroo()
    roo = Kangaroo()

    kanga.put_in_pouch("wallet")
    kanga.put_in_pouch("keys")
    kanga.put_in_pouch(roo)

    print("Kanga:")
    print(kanga)
    print("\nRoo:")
    print(roo)


if __name__ == "__main__":
    main()
