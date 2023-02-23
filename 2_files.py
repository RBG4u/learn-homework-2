
def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        with open('referat2.txt', 'w', encoding='utf-8') as f:
            f.write(f"{len(content)} - длина строки \n{len(content.split())} - количество слов в тексте \n{content.replace('.', '!')}")

if __name__ == "__main__":
    main()