def search_in_file(filename, keyword):
    matches = []
    count = 0

    try:
        with open(filename, "r") as f:
            for line_no, line in enumerate(f, 1):
                if keyword.lower() in line.lower():
                    matches.append((line_no, line.strip()))
                    count += 1

        return matches, count

    except FileNotFoundError:
        return None, 0