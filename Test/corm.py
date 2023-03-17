import requests
from bs4 import BeautifulSoup

def get_top_questions():
    url = "https://stackoverflow.com/questions?sort=votes"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #print("Top 10 questions on Stack Overflow: ")
    top_questions = []
    # Get the top 10 questions
    for question_summary in soup.find_all("div", class_="s-post-summary")[:10]:
        question = question_summary.find("a", class_="s-link").text
        top_questions.append(question)

    return top_questions

# Call the function to get the top 10 questions
if __name__ == "__main__":
    top_10_questions = get_top_questions()
    with open("top_questions.txt", "w") as f:
        # write top_10_questions to the file one question per line
        f.write("\n".join(top_10_questions))