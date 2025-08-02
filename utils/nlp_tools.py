import os
from google import genai
from google.genai import types

def get_model():
    """Get the Gemini client for text generation"""
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

def summarize_company_info(company_name, raw_text):
    """Summarize company information using Gemini with fallback"""
    prompt = f"""
    Analyze this text about {company_name} and provide a structured summary with the following information:
    
    • What the company does
    • Who their typical customers are  
    • What technologies or platforms they rely on
    • Strategic priorities or focus areas
    • 3 likely decision-makers (job titles + department) based on what they do
    
    Use clean bullet points with • symbols. Avoid using ** or * for formatting.
    
    Text to analyze: {raw_text[:4000]}
    """
    
    print("[NLP] Sending company info for summarization...")
    
    # Try multiple times with fallback
    for attempt in range(3):
        try:
            client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.3,
                    max_output_tokens=2048
                )
            )
            if response.text and response.text.strip():
                return response.text.strip()
        except Exception as e:
            print(f"[NLP] Attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                import time
                time.sleep(2)  # Wait before retry
    
    # Fallback to basic analysis
    return f"""
    • Company: {company_name}
    • Business focus: Based on website content, appears to be in the professional services sector
    • Customer base: Analysis requires manual review of scraped content
    • Technology stack: Unable to determine from available data
    • Strategic priorities: Requires further investigation
    • Decision makers: CEO, CTO, VP of Operations (estimated based on company size)
    
    Note: AI analysis temporarily unavailable. Please try again or contact support.
    """

def summarize_financials(company_name, financial_json):
    """Analyze financial data using Gemini"""
    prompt = f"""
    Analyze this financial data for {company_name} and provide insights:
    
    {financial_json}
    
    Provide a financial briefing with key insights about:
    • Revenue trends and growth
    • Profitability metrics
    • Financial health indicators
    • Risk factors and red flags
    • Opportunities and strengths
    
    Use clean bullet points with • symbols. Avoid using ** or * for formatting.
    """
    
    print("[NLP] Sending financial data for analysis...")
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text if response.text else "No response received"
    except Exception as e:
        print(f"[NLP] Error during financial analysis: {e}")
        return f"Error during AI processing: {str(e)}"

def generate_swot_analysis(company_name, financial_data):
    """Generate SWOT analysis using Gemini"""
    prompt = f"""
    Create a SWOT analysis for {company_name} based on this financial data:
    
    {financial_data}
    
    Provide a structured SWOT analysis with:
    Strengths:
    Weaknesses:
    Opportunities:
    Threats:
    
    Use clean bullet points with - symbols. Avoid using ** or * for formatting.
    """
    
    print("[NLP] Generating SWOT analysis...")
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text if response.text else "No response received"
    except Exception as e:
        print(f"[NLP] Error during SWOT analysis: {e}")
        return f"Error during AI processing: {str(e)}"

def compute_cagr(company_name, financial_data):
    """Compute CAGR using Gemini"""
    prompt = f"""
    Calculate the Compound Annual Growth Rate (CAGR) for {company_name} based on this financial data:
    
    {financial_data}
    
    If sufficient data is available, provide the CAGR calculation. If not, indicate "Not Available".
    """
    
    print("[NLP] Computing CAGR...")
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text if response.text else "CAGR (Revenue): Not Available"
    except Exception as e:
        print(f"[NLP] Error during CAGR calculation: {e}")
        return "CAGR (Revenue): Not Available"

def summarize_operations(company_name, signals: dict):
    """Summarize operational signals using Gemini"""
    prompt = f"""
    Help me understand how {company_name} operates based on this data.
    
    Analyze the following operational signals and provide insights about:
    • What kind of talent are they looking for?
    • What is their technical direction?
    • What initiatives are they working on?
    • Where might they need help or be falling short?
    
    Use clean bullet points with • symbols. Avoid using ** or * for formatting.
    
    Data: {signals}
    """
    
    print("[NLP] Sending operational signals for summarization...")
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text if response.text else "No response received"
    except Exception as e:
        print(f"[NLP] Error during operations analysis: {e}")
        return f"Error during AI processing: {str(e)}"

def get_agilisium_competitors_for_client(client_name):
    """Analyze competitors for Agilisium using Gemini"""
    prompt = f"""
    You're working at Agilisium Consulting and your client is {client_name}.
    
    Analyze the competitive landscape and provide insights about:
    • Competitor 1: [Name]
    • Services offered to client: [Details]
    • Strengths: [List]
    • Weaknesses: [List]
    • How Agilisium can stand out: [Strategy]
    
    • Competitor 2: [Name]
    • Services offered to client: [Details]
    • Strengths: [List]
    • Weaknesses: [List]
    • How Agilisium can stand out: [Strategy]
    
    • Competitor 3: [Name]
    • Services offered to client: [Details]
    • Strengths: [List]
    • Weaknesses: [List]
    • How Agilisium can stand out: [Strategy]
    
    Focus on firms like McKinsey, Bain, BCG, Deloitte, Accenture, IQVIA etc.
    
    Use clean bullet points with • symbols. Avoid using ** or * for formatting.
    """
    
    print("[NLP] Analyzing competitors for Agilisium...")
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text if response.text else "No response received"
    except Exception as e:
        print(f"[NLP] Error during competitor analysis: {e}")
        return f"Error during AI processing: {str(e)}"

def generate_product_analysis(company_name, raw_text):
    """Generate product analysis using Gemini"""
    prompt = f"""
    Create a comprehensive product analysis for {company_name} based on this text:
    
    {raw_text[:4000]}
    
    Provide analysis covering:
    
    Client Strategy Memo
    
    📌 Client Opportunity Brief
    [Describe the client's business goals and opportunities]
    
    🧹 Agilisium Product Fit
    [Analyze which Agilisium services would be most relevant]
    
    ♟ Competitive Positioning
    [Describe competitive landscape and positioning strategy]
    
    🎯 Pitch Strategy
    [Outline strategy for first client interaction]
    
    Use clean bullet points with • symbols. Avoid using ** or * for formatting.
    """
    
    print("[NLP] Generating product analysis...")
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return response.text if response.text else "No response received"
    except Exception as e:
        print(f"[NLP] Error during product analysis: {e}")
        return f"Error during AI processing: {str(e)}"
