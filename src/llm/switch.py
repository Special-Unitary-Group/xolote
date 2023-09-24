def prompt_templates(argument):
    switcher = {

        "Test": """
            The following content are academic papers.
            In a list, order the paper titles (exluding the ones in the references section) of the content in [{contents}] based by its correlation to [{query}].
            Give me the list with no further explanation.
            """,

        "Default": """
            You are an expert academic researcher that enjoys helping other researchers, like myself.
            Based on the following content from research papers that I am familiar with and I know are related to my question: 
            {contents}
            {query}
            """,
        "Ranking": """
            Based on the following contents:

            {contents}

            Give me a list of the provided papers ranked by relevance according to {query}.
            """,
        "Summarize": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to summarize their contents individually by relevance according to {query}.
                    """,
        "Explain": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to explain their purposes, what they do and what they're about in individually in easy-to-understand terms by relevance according to {query}. Note that they are complex articles so please consider educational purposes and layman's terms.
                    """,
        "Compare": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to compare them describing in detail their differences, similarities and correlations by relevance according to {query}.
                    """
    }
    return switcher.get(argument, "nothing")