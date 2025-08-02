# Prelytics - AI-Powered Business Intelligence Platform

![Prelytics Dashboard](https://img.shields.io/badge/Status-Production%20Ready-success)
![AI Integration](https://img.shields.io/badge/AI-Google%20Gemini-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-lightgrey)

## 🚀 Overview

Prelytics is a comprehensive business intelligence platform that analyzes companies using a sophisticated multi-agent AI architecture. The platform combines web scraping, financial data analysis, competitor research, and AI-powered insights to generate detailed business intelligence reports through an impressive web-based dashboard.

## ✨ Key Features

### 📊 **Multi-Agent Analysis System**
- **Client Intelligence Agent**: Extracts company profiles and leadership information
- **Financial Insight Agent**: Analyzes public financial data using Yahoo Finance
- **Operational Signal Agent**: Gathers operational insights and technology stack
- **Competitor Analysis Agent**: Identifies competitive landscape
- **Product Analysis Agent**: Matches client needs to service offerings

### 🎯 **AI-Powered Intelligence**
- Google Gemini integration for advanced text analysis
- Structured prompts for consistent output formatting
- Real-time financial data processing
- Automated report generation

### 💼 **Professional Dashboard**
- Modern responsive UI with dark/light theme support
- Interactive financial charts using Plotly.js
- Tabbed content organization for easy navigation
- Export functionality (PDF, Text, Data formats)
- Real-time progress tracking

## 🏗️ Architecture

```
Prelytics/
├── agents/                     # AI Analysis Agents
│   ├── client_intelligence.py  # Company profile extraction
│   ├── financial_insight.py    # Financial data analysis
│   ├── operational_signal.py   # Operations insights
│   ├── competitor_analysis.py  # Competitive landscape
│   └── product_analysis.py     # Product-market fit
├── utils/                      # Core Utilities
│   ├── data_sources.py         # Data collection utilities
│   ├── nlp_tools.py           # NLP processing functions
│   └── scraping.py            # Web scraping tools
├── templates/                  # Frontend Templates
│   └── index.html             # Main dashboard interface
├── static/                     # Static Assets
│   ├── css/style.css          # Custom styling
│   ├── js/app.js              # Main application logic
│   └── js/charts.js           # Chart configurations
├── outputs/                    # Generated Reports
└── reports/                    # Report Storage
```

## 🔧 Technology Stack

### Backend
- **Flask**: Web application framework
- **Google Gemini**: AI analysis and text processing
- **Yahoo Finance API**: Financial data integration
- **BeautifulSoup**: Web scraping and content extraction
- **Pandas**: Data manipulation and analysis

### Frontend
- **Bootstrap 5**: Responsive design framework
- **Plotly.js**: Interactive data visualization
- **Chart.js**: Financial chart generation
- **Font Awesome**: Icon library

### Data Sources
- Company websites (automated scraping)
- Yahoo Finance (real-time stock data)
- LinkedIn Jobs (operational signals)
- Public financial databases

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google Gemini API key
- Internet connection for data collection

### Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set your Google Gemini API key as `GEMINI_API_KEY`
4. Run the application: `gunicorn --bind 0.0.0.0:5000 main:app`

### Usage
1. Navigate to the dashboard interface
2. Enter company name and website URL
3. Configure analysis parameters
4. Start the analysis process
5. Review comprehensive results across multiple tabs
6. Export reports in preferred format

## 📈 Analysis Capabilities

### Financial Intelligence
- Revenue trends and growth analysis
- Profitability metrics evaluation
- Financial health indicators
- Risk assessment and opportunities
- SWOT analysis generation

### Operational Insights
- Technology stack identification
- Talent acquisition patterns
- Strategic initiative tracking
- Operational efficiency assessment

### Competitive Analysis
- Market positioning evaluation
- Competitor service offerings
- Strength/weakness analysis
- Strategic differentiation opportunities

### Client Intelligence
- Company profile extraction
- Leadership team identification
- Business model analysis
- Customer segmentation insights

## 🎨 Dashboard Features

### Modern Interface
- Clean, professional design
- Responsive layout for all devices
- Dark/light theme switching
- Interactive data visualizations

### Export Options
- **PDF Reports**: Comprehensive formatted documents
- **Text Export**: Plain text summaries
- **Data Export**: Structured JSON/CSV formats

### Real-time Processing
- Live progress tracking
- Dynamic content loading
- Error handling and recovery
- Graceful fallback mechanisms

## 🔒 Security & Privacy

- Secure API key management
- No sensitive data storage
- HTTPS-ready configuration
- Privacy-compliant data collection

## 📝 Sample Reports

The platform generates comprehensive reports including:
- Executive summaries
- Financial performance analysis
- Competitive landscape overview
- Strategic recommendations
- Market opportunity assessment

## 🤝 Contributing

This platform is designed for professional business intelligence use cases. The modular architecture allows for easy extension and customization.

## 📞 Support

For technical issues or feature requests, please refer to the documentation or contact the development team.

---

**Prelytics** - Transforming business intelligence through AI-powered analysis