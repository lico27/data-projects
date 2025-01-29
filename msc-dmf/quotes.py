import csv

# Open the text file and CSV file
with open("quotes.txt", "r") as txt_file, open("quotes.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in txt_file:
        # Split the line into columns
        row = line.strip().split("|")
        csv_writer.writerow(row)

print("Conversion complete: data.csv created.")
