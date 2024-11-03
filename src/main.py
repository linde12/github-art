from datetime import datetime, timedelta
from subprocess import call
from PIL import Image


def commit_date(date: datetime):
    date_str = date.strftime("%a %b %d %I:%M %Y +0700")
    call(["git", "add", "file.txt"])
    call(["git", "commit", "-m", "github art", "--date", date_str])


def modify_file(s: str):
    with open("file.txt", "w") as f:
        f.write(s)


def main():
    now = datetime.now()
    monday = now - timedelta(days=now.weekday())
    # lets put it somewhere in the center, ignore leaps
    start_date = monday - timedelta(weeks=42, days=1)

    pixels = []
    with Image.open("image.png") as img:
        width, height = img.size

        for x in range(width):
            for y in range(height):
                print(img.getpixel((x, y)))
                _r, g, _b, _a = img.getpixel((x, y))  # type: ignore

                if not g:
                    pixels.append((x, y, 0))
                    continue

                pixels.append((x, y, g))

    for i, pixel in enumerate(pixels):
        x, y, g = pixel
        date = start_date + timedelta(days=i)
        if not g:
            continue

        for c in range(int(g / 10) * 2):
            modify_file(str(i + c))
            commit_date(date)


if __name__ == "__main__":
    main()
