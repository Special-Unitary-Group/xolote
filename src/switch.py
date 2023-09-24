def prompt_templates(argument: str) -> str:
    switcher = {
        "test": """
            The following content are academic papers.
            In a list, order the paper titles (exluding the ones in the references section) of the content in [{contents}] based by its correlation to [{query}].
            Give me the list with no further explanation.
            """,
        "default": """
            You are an expert academic researcher who enjoys helping other researchers, like myself.
            The following contents are currently the most relevant to my research:
            
            {contents}

            Based on the previous information, please help me with this: {query}

            Please answer with the same text from the paper without paraphrasing or generating new text unless explicitly requested.
            """,
        "ranking": """
            Based on the following contents:

            {contents}

            Give me a list of the provided papers ranked by relevance according to {query}.
            """,
        "summarize": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to summarize their contents individually by relevance according to {query}.
            """,
        "explain": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to explain their purposes, what they do and what they're about in individually in easy-to-understand terms by relevance according to {query}. Note that they are complex articles so please consider educational purposes and layman's terms.
            """,
        "compare": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to compare them describing in detail their differences, similarities and correlations by relevance according to {query}.
            """,
    }

    return switcher.get(argument, "nothing")
