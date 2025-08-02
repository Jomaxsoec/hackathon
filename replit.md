# Prelytics - Business Intelligence Platform

## Overview

Prelytics is a comprehensive business intelligence platform that analyzes companies using a multi-agent architecture. The system combines web scraping, financial data analysis, competitor research, and AI-powered insights to generate detailed business intelligence reports. The platform features a Flask web application with a modern frontend interface that allows users to input company information and receive structured analysis reports covering client intelligence, financial insights, operational signals, and competitive landscape.

**Latest Status (August 2, 2025)**: Platform is fully operational with robust error handling, financial chart generation, and enhanced UI. Successfully processing real company data from multiple sources including web scraping, Yahoo Finance API, and Google Gemini AI analysis.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Improvements (August 2, 2025)

### Error Handling & Reliability
- ✅ Implemented comprehensive error handling with fallback mechanisms
- ✅ Added retry logic with exponential backoff for API calls
- ✅ Created robust fallback content system when AI services are temporarily unavailable
- ✅ Fixed JSON parsing errors with proper response validation

### Financial Analysis Features
- ✅ Added real-time financial chart generation using Yahoo Finance data
- ✅ Implemented multiple chart types: stock price trends, trading volume, financial breakdowns, revenue trends
- ✅ Created interactive charts with Chart.js integration
- ✅ Added comprehensive financial metrics extraction (14+ data points)

### User Interface Enhancements
- ✅ Updated to latest Plotly CDN (v2.26.0) for improved performance
- ✅ Enhanced chart styling with hover effects and responsive design
- ✅ Improved error messaging and loading states
- ✅ Added comprehensive documentation and professional README

### Data Integrity Improvements
- ✅ Verified authentic data sources (Yahoo Finance, company websites, Google Gemini)
- ✅ Implemented proper data validation and error states
- ✅ Added clear indicators when data is unavailable vs. processing

## System Architecture

### Frontend Architecture
- **Framework**: HTML/CSS/JavaScript with Bootstrap 5 for responsive design
- **Visualization**: Chart.js and Plotly.js for interactive financial charts and data visualization
- **Theming**: Dark/light theme support with CSS custom properties
- **Layout**: Responsive sidebar configuration panel with main content area for displaying analysis results

### Backend Architecture
- **Framework**: Flask web application with CORS support for API access
- **Agent Pattern**: Coordinator agent that orchestrates multiple specialized analysis agents
- **Modular Design**: Separate agents for different analysis types (client intelligence, financial insight, operational signals, competitor analysis, product analysis)
- **API Design**: RESTful endpoint structure with JSON responses

### Agent System Components
1. **CoordinatorAgent**: Orchestrates the entire analysis workflow and combines results from all specialized agents
2. **ClientIntelligenceAgent**: Extracts company profiles and leadership information from websites
3. **FinancialInsightAgent**: Analyzes public financial data using Yahoo Finance API for stock market data
4. **OperationalSignalAgent**: Gathers operational insights including job postings and technology stack information
5. **CompetitorAnalysisAgent**: Identifies and analyzes competitive landscape
6. **ProductAnalysisAgent**: Matches client needs to service offerings

### Data Processing Pipeline
- **Web Scraping**: BeautifulSoup-based scraping with multiple page targeting (about, services, leadership pages)
- **NLP Processing**: Google Gemini AI integration for text analysis and summarization
- **Financial Data**: Yahoo Finance integration for real-time stock and financial metrics
- **Report Generation**: Structured report compilation with section-based organization

### AI Integration
- **Primary AI Service**: Google Gemini (gemini-1.5-flash model) for text analysis and summarization
- **Prompt Engineering**: Structured prompts for consistent output formatting using bullet points
- **Error Handling**: Graceful fallback mechanisms when AI services are unavailable

## External Dependencies

### AI and NLP Services
- **Google Gemini API**: Primary AI service for text analysis, summarization, and insight generation
- **google-generativeai**: Python client library for Gemini API integration

### Financial Data Sources
- **Yahoo Finance (yfinance)**: Stock market data, financial metrics, and company information
- **Pandas**: Data manipulation and analysis for financial calculations

### Web Scraping and Data Collection
- **Requests**: HTTP client for web scraping and API calls
- **BeautifulSoup4**: HTML parsing and content extraction
- **LinkedIn Jobs**: Operational signal gathering (job posting analysis)

### Frontend Libraries
- **Bootstrap 5**: CSS framework for responsive design
- **Chart.js**: Interactive chart generation for financial visualizations
- **Plotly.js**: Advanced data visualization and interactive plots
- **Font Awesome**: Icon library for UI elements

### Python Framework and Utilities
- **Flask**: Web application framework
- **Flask-CORS**: Cross-origin resource sharing support
- **datetime**: Timestamp generation for reports
- **json**: Data serialization and API responses

### Development and Deployment
- **os**: Environment variable management for API keys
- **tqdm**: Progress bars for long-running operations
- **matplotlib/seaborn**: Additional visualization libraries for data analysis

### Report Generation
- **Custom text formatting**: Structured report generation with section headers
- **File I/O**: Local file storage for generated reports
- **JSON serialization**: API response formatting and data exchange