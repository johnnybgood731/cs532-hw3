from bs4 import BeautifulSoup
import math

keyword = "Virginia"
counter = 0
keyCounter = 0
countTo10 = 0
tf = [0.0] * 10
idf = [0.0] * 10
url = [""] * 10
fileNums = [7, 27, 44, 67, 109, 116, 123, 197, 199, 210]
idfDenominator = 775000000  # Number of Google search results for the keyword

for x in range(1000):
    try:
        with(open("C:\\Users\\Johnny\\Desktop\\html\\html" + str(x + 1) + ".html", 'r', encoding='utf-8')) as file:
            soup = BeautifulSoup(file.read())
            text = str(soup.get_text)
            if keyword in text:
                keyCounter += 1
                if x + 1 in fileNums:
                    idf[countTo10] = math.log2(55000000000 / idfDenominator)
                    with(open("C:\\Users\\Johnny\\Desktop\\links.txt", 'r')) as links:
                        for i, line in enumerate(links):
                            if i == x:
                                url[countTo10] = line[:len(line) - 1]
                                break
                    tf[countTo10] = text.count("Virginia") / int(input("How many words are in procHTML" + str(x + 1) +
                                                                 "? "))
                    countTo10 += 1
            with(open("C:\\Users\\Johnny\\Desktop\\processedHTML\\procHTML" + str(x + 1) + ".html", 'w')) as newFile:
                newFile.write(text)
    except UnicodeDecodeError:
        counter += 1
        continue
    except UnicodeEncodeError:
        counter += 1
        continue
    except FileNotFoundError:
        print("File " + str(x + 1) + " not found.")
        counter += 1
        continue

print("Total Errors: " + str(counter))
print("Total Documents Containing '" + keyword + "': " + str(keyCounter) + "\n")

for i in range(10):
    print(str(fileNums[i]) + ". tf = " + str(tf[i]) + ", idf = " + str(idf[i]) + ", tf-idf = " + str(tf[i] * idf[i]) +
          ", url = " + url[i])
