import csv

def save_to_file(jobs):
    with open("./file.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["No", "공고제목", "회사", "지역", "link"])

        for index, job in enumerate(jobs): 
            csv_writer.writerow(
                [index + 1, 
                job["title"], 
                job["company"], 
                job["location"], 
                job["link"]])