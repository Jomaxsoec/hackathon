from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from coordinator_agent import CoordinatorAgent
import json
import yfinance as yf
import pandas as pd
import datetime

app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        company_name = data.get('company_name')
        company_url = data.get('company_url')
        
        if not company_name or not company_url:
            return jsonify({'error': 'Company name and URL are required'}), 400
        
        print(f"[API] Starting analysis for {company_name} - {company_url}")
        
        # Run the analysis using the existing coordinator agent
        agent = CoordinatorAgent(company_name, company_url)
        results = agent.run_workflow()
        
        # Parse the results into sections
        sections = parse_results(results)
        
        # Add financial chart data
        financial_data = generate_financial_chart_data(company_name)
        
        return jsonify({
            'success': True,
            'data': sections,
            'financial_charts': financial_data,
            'raw_results': results
        })
        
    except Exception as e:
        print(f"[API] Error during analysis: {e}")
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

def parse_results(results):
    """Parse the results into structured sections"""
    sections = {}
    
    # Extract different sections
    if "==== CLIENT INTELLIGENCE REPORT ====" in results:
        start_idx = results.find("==== CLIENT INTELLIGENCE REPORT ====")
        end_idx = results.find("==== KEY DECISION MAKERS ====")
        if end_idx == -1:
            end_idx = results.find("==== FINANCIAL INSIGHTS ====")
        if end_idx != -1:
            client_content = results[start_idx + len("==== CLIENT INTELLIGENCE REPORT ===="):end_idx].strip()
            sections['client'] = format_section_content(client_content)
    
    if "==== KEY DECISION MAKERS ====" in results:
        start_idx = results.find("==== KEY DECISION MAKERS ====")
        end_idx = results.find("==== FINANCIAL INSIGHTS ====")
        if end_idx != -1:
            leadership_content = results[start_idx + len("==== KEY DECISION MAKERS ===="):end_idx].strip()
            sections['leadership'] = format_section_content(leadership_content)
    
    if "==== FINANCIAL INSIGHTS ====" in results:
        start_idx = results.find("==== FINANCIAL INSIGHTS ====")
        end_idx = results.find("==== OPERATIONAL SIGNALS ====")
        if end_idx != -1:
            financial_content = results[start_idx + len("==== FINANCIAL INSIGHTS ===="):end_idx].strip()
            sections['financial'] = format_section_content(financial_content)
    
    if "==== OPERATIONAL SIGNALS ====" in results:
        start_idx = results.find("==== OPERATIONAL SIGNALS ====")
        end_idx = results.find("==== COMPETITOR ANALYSIS ====")
        if end_idx != -1:
            operational_content = results[start_idx + len("==== OPERATIONAL SIGNALS ===="):end_idx].strip()
            sections['operational'] = format_section_content(operational_content)
    
    if "==== COMPETITOR ANALYSIS ====" in results:
        start_idx = results.find("==== COMPETITOR ANALYSIS ====")
        end_idx = results.find("==== PRODUCT ANALYSIS ====")
        if end_idx != -1:
            competitor_content = results[start_idx + len("==== COMPETITOR ANALYSIS ===="):end_idx].strip()
            sections['competitor'] = format_section_content(competitor_content)
    
    if "==== PRODUCT ANALYSIS ====" in results:
        start_idx = results.find("==== PRODUCT ANALYSIS ====")
        product_content = results[start_idx + len("==== PRODUCT ANALYSIS ===="):].strip()
        sections['product'] = format_section_content(product_content)
    
    return sections

def format_section_content(content):
    """Format content for HTML display"""
    if not content:
        return ""
    
    # Clean up formatting
    content = content.replace('**', '').replace('*', '')
    content = content.replace('-----', '').replace('----', '').replace('---', '').replace('--', '')
    
    # Split into lines and process
    lines = content.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            # Handle bullet points with proper indentation
            if line.startswith('•'):
                formatted_lines.append(f'<div class="bullet-point">{line[1:].strip()}</div>')
            elif line.startswith('-'):
                formatted_lines.append(f'<div class="bullet-point">{line[1:].strip()}</div>')
            # Handle section titles (all caps or with colons)
            elif line.isupper() or line.endswith(':'):
                formatted_lines.append(f'<div class="section-title">{line}</div>')
            # Handle subsection titles
            elif line.startswith('•') and ':' in line:
                formatted_lines.append(f'<div class="subsection-title">{line[1:].strip()}</div>')
            # Handle indented content (starts with spaces)
            elif line.startswith('   -'):
                formatted_lines.append(f'<div class="indented-bullet">{line[4:].strip()}</div>')
            # Regular text
            else:
                formatted_lines.append(f'<p style="margin: 8px 0; line-height: 1.6;">{line}</p>')
    
    return '\n'.join(formatted_lines)

def generate_financial_chart_data(company_name):
    """Generate financial chart data for visualization"""
    try:
        # Try to get financial data from Yahoo Finance
        ticker = yf.Ticker(company_name)
        
        # Get basic info
        info = ticker.info
        
        # Get historical data for the last year
        hist = ticker.history(period="1y")
        
        # Get quarterly financials
        quarterly = ticker.quarterly_financials
        
        # Prepare chart data
        charts = {}
        
        # Stock price chart
        if not hist.empty:
            charts['stock_price'] = {
                'labels': [date.strftime('%Y-%m-%d') for date in hist.index[-30:]],  # Last 30 days
                'datasets': [{
                    'label': 'Stock Price ($)',
                    'data': hist['Close'].tail(30).tolist(),
                    'borderColor': 'rgb(75, 192, 192)',
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'fill': True
                }]
            }
        
        # Volume chart
        if not hist.empty:
            charts['volume'] = {
                'labels': [date.strftime('%Y-%m-%d') for date in hist.index[-30:]],
                'datasets': [{
                    'label': 'Trading Volume',
                    'data': hist['Volume'].tail(30).tolist(),
                    'borderColor': 'rgb(255, 99, 132)',
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                    'fill': True
                }]
            }
        
        # Financial metrics pie chart
        if info:
            financial_metrics = {}
            if 'marketCap' in info and info['marketCap']:
                financial_metrics['Market Cap'] = info['marketCap']
            if 'totalRevenue' in info and info['totalRevenue']:
                financial_metrics['Revenue'] = info['totalRevenue']
            if 'totalDebt' in info and info['totalDebt']:
                financial_metrics['Total Debt'] = info['totalDebt']
            if 'totalCash' in info and info['totalCash']:
                financial_metrics['Cash'] = info['totalCash']
                
            if financial_metrics:
                charts['financial_breakdown'] = {
                    'labels': list(financial_metrics.keys()),
                    'datasets': [{
                        'label': 'Financial Metrics',
                        'data': list(financial_metrics.values()),
                        'backgroundColor': [
                            'rgba(54, 162, 235, 0.8)',
                            'rgba(255, 206, 86, 0.8)',
                            'rgba(255, 99, 132, 0.8)',
                            'rgba(75, 192, 192, 0.8)',
                            'rgba(153, 102, 255, 0.8)',
                            'rgba(255, 159, 64, 0.8)'
                        ]
                    }]
                }
        
        # Revenue trend (if quarterly data available)
        if not quarterly.empty and 'Total Revenue' in quarterly.index:
            revenue_data = quarterly.loc['Total Revenue'].dropna()
            if len(revenue_data) > 0:
                charts['revenue_trend'] = {
                    'labels': [col.strftime('%Y-Q%q') for col in revenue_data.index],
                    'datasets': [{
                        'label': 'Quarterly Revenue',
                        'data': revenue_data.tolist(),
                        'borderColor': 'rgb(54, 162, 235)',
                        'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                        'fill': True
                    }]
                }
        
        return charts
        
    except Exception as e:
        print(f"[Charts] Error generating financial charts: {e}")
        return {
            'error': f'Could not generate financial charts for {company_name}. Data may not be available.',
            'demo_chart': {
                'labels': ['Q1', 'Q2', 'Q3', 'Q4'],
                'datasets': [{
                    'label': 'Sample Revenue (Millions)',
                    'data': [100, 120, 135, 150],
                    'borderColor': 'rgb(75, 192, 192)',
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'fill': True
                }]
            }
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
