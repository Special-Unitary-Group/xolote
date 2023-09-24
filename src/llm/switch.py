def prompt_templates(argument):
    switcher = {
        "Default": """
            You are an expert academic researcher that enjoys helping other researchers, like myself.
            Based on the following content from research papers that I am familiar with and I know are related to my question: 
            
            """,
        "Ranking": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to rank the papers according to relevance in topic. I want the papers listed in order of rank and a brief explanation of why. Only consider the provided files, not the references in them
                    """,
        "Summarize": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to summarize their contents individually
                    """,
        "Explain": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to explain them individually in easy-to-understand terms.
                    """,
        "Compare": """
            I'll provide you a series of papers, here are their contents:

            {contents}

            Now, I need you to compare them.
                    """
    }
    return switcher.get(argument, "nothing")