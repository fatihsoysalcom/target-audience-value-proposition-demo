import json

def analyze_target_audience(product_description):
    """Analyzes a product description to identify potential target audiences and their needs."""
    # In a real-world scenario, this would involve more sophisticated NLP or data analysis.
    # For this example, we'll use simple keyword matching.
    analysis = {
        "target_audiences": [],
        "value_propositions": []
    }

    # Keywords related to developers and their common pain points
    developer_keywords = ["code", "developer", "software", "api", "script", "bug", "debug", "deploy", "automate"]
    # Keywords related to small business owners and their needs
    small_business_keywords = ["sales", "customer", "marketing", "growth", "efficiency", "cost", "time", "manage"]

    # Check for developer-centric features
    if any(keyword in product_description.lower() for keyword in developer_keywords):
        analysis["target_audiences"].append("Software Developers")
        analysis["value_propositions"].append("Streamline coding workflows, automate repetitive tasks, or simplify complex development processes.")

    # Check for small business-centric features
    if any(keyword in product_description.lower() for keyword in small_business_keywords):
        analysis["target_audiences"].append("Small Business Owners")
        analysis["value_propositions"].append("Increase sales, improve customer engagement, save time and money, or gain better business insights.")

    # If no specific keywords, assume a general audience
    if not analysis["target_audiences"]:
        analysis["target_audiences"].append("General Users")
        analysis["value_propositions"].append("Provides a useful solution to a common problem.")

    return analysis

if __name__ == "__main__":
    # Example product description from the article context
    product_description_1 = "A tool that helps developers automate repetitive coding tasks and debug faster."
    product_description_2 = "A platform to help small businesses manage their online sales and marketing efforts efficiently."
    product_description_3 = "An application for managing personal finances."

    print(f"Analyzing: '{product_description_1}'")
    analysis_1 = analyze_target_audience(product_description_1)
    print(json.dumps(analysis_1, indent=2))
    print("\n" + "-" * 30 + "\n")

    print(f"Analyzing: '{product_description_2}'")
    analysis_2 = analyze_target_audience(product_description_2)
    print(json.dumps(analysis_2, indent=2))
    print("\n" + "-" * 30 + "\n")

    print(f"Analyzing: '{product_description_3}'")
    analysis_3 = analyze_target_audience(product_description_3)
    print(json.dumps(analysis_3, indent=2))
