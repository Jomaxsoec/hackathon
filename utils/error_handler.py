"""
Error handling utilities for Prelytics platform
"""
import logging
import time
from functools import wraps

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def retry_with_backoff(max_retries=3, backoff_factor=2):
    """Decorator to retry functions with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    if attempt < max_retries - 1:
                        sleep_time = backoff_factor ** attempt
                        logger.info(f"Retrying in {sleep_time} seconds...")
                        time.sleep(sleep_time)
                    else:
                        logger.error(f"All {max_retries} attempts failed for {func.__name__}")
                        raise e
            return None
        return wrapper
    return decorator

def safe_ai_call(fallback_response="Analysis temporarily unavailable. Please try again."):
    """Decorator to safely handle AI API calls with fallback"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if result and result.strip():
                    return result
                else:
                    logger.warning(f"Empty response from {func.__name__}")
                    return fallback_response
            except Exception as e:
                logger.error(f"AI call failed in {func.__name__}: {e}")
                return fallback_response
        return wrapper
    return decorator

def generate_fallback_content(company_name, content_type="general"):
    """Generate basic fallback content when AI is unavailable"""
    fallback_templates = {
        "client": f"""
        • Company: {company_name}
        • Business Analysis: Comprehensive analysis requires AI processing
        • Target Customers: Information will be available when AI services resume
        • Technology Stack: Analysis pending
        • Strategic Priorities: Detailed insights coming soon
        • Decision Makers: CEO, CTO, VP Operations (estimated)
        
        Note: Full AI-powered analysis temporarily unavailable. Basic information provided.
        """,
        
        "financial": f"""
        • Financial Overview: {company_name} financial analysis requires real-time data processing
        • Revenue Trends: Analysis pending AI availability
        • Profitability: Comprehensive metrics will be generated when services resume
        • Financial Health: Detailed assessment coming soon
        • Investment Recommendations: Professional analysis in progress
        
        Note: Financial insights require AI processing. Please try again shortly.
        """,
        
        "operational": f"""
        • Operational Focus: {company_name} operations analysis in progress
        • Technology Adoption: Detailed insights pending
        • Talent Strategy: Analysis requires AI processing
        • Growth Initiatives: Comprehensive review coming soon
        • Efficiency Metrics: Advanced analysis temporarily unavailable
        
        Note: Operational signals analysis requires AI services.
        """,
        
        "competitor": f"""
        • Competitive Landscape: {company_name} competitor analysis requires AI processing
        • Market Position: Detailed positioning analysis pending
        • Competitor Strengths: Comprehensive evaluation coming soon
        • Market Opportunities: Strategic insights in progress
        • Differentiation Strategy: Advanced analysis temporarily unavailable
        
        Note: Competitive intelligence requires AI-powered analysis.
        """,
        
        "product": f"""
        • Product Analysis: {company_name} product-market fit evaluation in progress
        • Service Alignment: Detailed analysis requires AI processing
        • Market Opportunities: Comprehensive assessment pending
        • Strategic Recommendations: Professional insights coming soon
        • Implementation Strategy: Advanced planning temporarily unavailable
        
        Note: Product analysis requires AI-powered intelligence.
        """
    }
    
    return fallback_templates.get(content_type, fallback_templates["client"])