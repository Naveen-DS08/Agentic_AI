# Financial Agent - Agentic AI

This project leverages the power of Agentic AI to create a sophisticated financial assistant capable of gathering comprehensive stock market information and performing web searches. By combining specialized AI agents, it can extract real-time stock data, analyst recommendations, company fundamentals, and the latest news, presenting it in a structured and easy-to-understand format.

## ✨ Features

* **Intelligent Web Search:** Utilizes an AI-powered web search agent to find relevant information from the internet.

* **Comprehensive Financial Data:** Extracts a wide range of financial data for any given stock ticker, including:

    * Current Stock Prices

    * Analyst Recommendations

    * Company Fundamentals

    * Latest Company News

    * General Company Information

* **Multi-Agent Collaboration:** A team of AI agents works together to fulfill complex queries, ensuring accurate and detailed responses.

* **Structured Output:** Presents data in tables for better readability and analysis.

* **Source Attribution:** Provides sources for all extracted information.

## 🚀 Getting Started

Follow these steps to set up and run the Financial Agent on your local machine.

### Prerequisites

* Python 3.8+

* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```
    git clone [https://github.com/Naveen-DS08/Agentic_AI.git](https://github.com/Naveen-DS08/Agentic_AI.git)
    cd Financial_Analyst
    ```

  
2.  **Create a virtual environment (recommended):**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```
    pip install -r requirements.txt
    ```

    *(Note: You'll need to create a `requirements.txt` file containing `phi-agent`, `python-dotenv`, `yfinance`, and `duckduckgo-search`. See "Project Structure" for details.)*

### Environment Variables

This project requires an API key for Groq to access the large language models.

1.  **Obtain a Groq API Key:**

    * Visit the [Groq website](https://console.groq.com/keys) and sign up or log in.

    * Generate a new API key.

2.  **Create a `.env` file:**
    In the root directory of your project, create a file named `.env` and add your Groq API key:

    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```

    Replace `"your_groq_api_key_here"` with the actual API key you obtained from Groq.

## 📂 Project Structure

Your project directory should look something like this:

```
Financial_Analyst/
├── .env
├── financial_agent.py
├── requirements.txt
└── README.md
```

**`requirements.txt`**
```
phi-agent
python-dotenv
yfinance
duckduckgo-search
```

## 💡 Usage

To run the Financial Agent, execute the `financial_agent.py` script. The script is configured to answer a specific query, but you can easily modify it to ask different questions about various stocks.

1.  **Run the script:**

    ```
    python financial_agent.py
    ```

2.  **Example Query:**
    The current `financial_agent.py` is set to ask: `"Summarize analyst recommendation and share the latest news for NVDA"`. You can change `"NVDA"` to any other stock ticker (e.g., `"AAPL"`, `"MSFT"`, `"GOOGL"`) or modify the query entirely to get different types of financial information.

    The agent will then process the request, utilize its web search and financial tools, and print the summarized information directly to your console, including sources and data presented in tables.

## 🛣️ Future Enhancements

* **Interactive User Interface (UI):** Develop a web-based or desktop UI to allow users to easily input queries and view results in a more interactive and visually appealing manner.

* **Advanced Analysis:** Integrate more sophisticated financial analysis tools and models.

* **Portfolio Tracking:** Add functionality to track and analyze personal stock portfolios.

* **Alerts and Notifications:** Implement real-time alerts for significant news or price movements.

