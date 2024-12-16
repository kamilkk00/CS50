import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    probabilities = {}
    linked_pages = corpus[page]

    if len(linked_pages) == 0:
        for other_page in corpus:
            probabilities[other_page] = 1 / len(corpus)
        return probabilities

    total_pages = len(corpus)
    for other_page in corpus:
        if other_page in linked_pages:
            probabilities[other_page] = (damping_factor / len(linked_pages)) + ((1 - damping_factor) / total_pages)
        else:
            probabilities[other_page] = (1 - damping_factor) / total_pages

    return probabilities    


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    rank = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))

    for i in range(n):
        probabilites = transition_model(corpus, current_page, damping_factor)

        next_page = random.choices(
            population = list(probabilites.keys()),
            weights = list(probabilites.values()),
            k = 1
        )[0]

        rank[next_page] += 1
        current_page = next_page

    for page in rank:
        rank[page] /= n

    return rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    pages_count = len(corpus)
    page_rank = {page: 1 / pages_count for page in corpus}

    while True:
        new_page_rank = {}
        for page in corpus:
            randome = (1 - damping_factor) / pages_count
            sum = 0 
            for linking_page in corpus:
                if len(corpus[linking_page]) == 0:
                    sum += page_rank[linking_page] / pages_count
                elif page in corpus[linking_page]:
                    sum += page_rank[linking_page] / len(corpus[linking_page])
        
            new_page_rank[page] = randome + damping_factor * sum

        if all(abs(new_page_rank[page] - page_rank[page]) < 0.001 for page in corpus ):
            break 

        page_rank = new_page_rank

    return page_rank

if __name__ == "__main__":
    main()
