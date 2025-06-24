def simple_summarizer(news_list):
    combined = " ".join(news_list)
    sentences = combined.split('.')
    summary = '. '.join(sentences[:2]) + '.' if len(sentences) >= 2 else combined
    return summary
