from text_file_search_tool.main import search_in_file

def main():
    filename = input("Enter file name: ")
    keyword = input("Enter keyword to search: ")

    matches, count = search_in_file(filename, keyword)

    if matches is None:
        print("File not found")
        return

    if count == 0:
        print("No matches found")
    else:
        print("\nMatches found:\n")
        for line_no, line in matches:
            print(f"Line {line_no}: {line}")

        print(f"\nTotal matches: {count}")


if __name__ == "__main__":
    main()