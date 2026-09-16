#LAB 5 PART F
""" def create_report(title, *sections, **metadata):
    return {
        "title": title,
        "sections": sections,
        "metadata": metadata
    }

def count_words(*sections):
    total_words = 0
    for sec in sections:
        words = sec["content"].split()
        total_words += len(words)
    return total_words

def summarize_report(report):
    title = report["title"]
    author = report["metadata"].get("author", "unkown")
    last_edited = str(report["metadata"].get("last_edited", "unkown"))
    total_words = count_words(*report["sections"])
    
    out = f"DOCUMENT: {title}\n"
    out += f"AUTHOR: {author}\n"
    out += f"LAST EDITED: {last_edited[:4]}-{last_edited[4:6]}-{last_edited[6:8]}\n"
    out += f"TOTAL WORDS: {total_words}\n"
    out += "--- SECTIONS ---\n"
    
    for sec in report["sections"]:
        out += f"* {sec['heading']}. Snippet: ...{sec['content'][15:45]}...\n"
        
    return out

my_report = create_report(
    "Hidden in plain sight",
    {"heading": "Intro", "content": "Michel Foucault once wrote 'Visibility is a trap'"},
    {"heading": "Abstract", "content": "In this Master thesis I will expand on research"},
    author="Alve", 
    last_edited=20260413
)

my_report2 = create_report(
    "Hidden in plain sight",
    {"heading": "Intro", "content": "Michel Foucault once wrote 'Visibility is a trap'"},
    {"heading": "Abstract", "content": "In this Master thesis I will expand on research"},
    author="Alve"
)

my_report3 = create_report(
    "Hidden in plain sight",
    {"heading": "Intro", "content": "Michel Foucault once wrote 'Visibility is a trap'"},
    {"heading": "Abstract", "content": "In this Master thesis I will expand on research"}, 
    last_edited=20260413
)


print(summarize_report(my_report))
print(summarize_report(my_report2))
print(summarize_report(my_report3))

 """