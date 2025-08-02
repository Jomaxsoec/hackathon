from agents import client_intelligence
from agents import financial_insight
from agents import operational_signal
from agents import competitor_analysis
from agents import product_analysis
from utils.error_handler import generate_fallback_content
import logging

class CoordinatorAgent:
    def __init__(self, name, url):
        print(f"[DEBUG] CoordinatorAgent initialized with {name}, {url}")
        self.name = name
        self.url = url

    def run_workflow(self):
        print(f"\n[CoordinatorAgent] Starting intelligence generation for: {self.name}")

        # Initialize results with fallbacks
        results = {}
        
        # 1. Client Intelligence
        try:
            client_data = client_intelligence.extract_profile(self.name, self.url)
            results['client'] = client_data if client_data else generate_fallback_content(self.name, "client")
        except Exception as e:
            print(f"[CoordinatorAgent] Client intelligence failed: {e}")
            results['client'] = generate_fallback_content(self.name, "client")

        # 2. Financial Insight (Tabular + SWOT + CAGR)
        try:
            financial_data = financial_insight.analyze_financials(self.name)
            results['financial'] = financial_data if financial_data else generate_fallback_content(self.name, "financial")
        except Exception as e:
            print(f"[CoordinatorAgent] Financial analysis failed: {e}")
            results['financial'] = generate_fallback_content(self.name, "financial")

        # 3. Operational Signals
        try:
            ops_data = operational_signal.extract_operational_signals(self.name, self.url)
            results['operational'] = ops_data if ops_data else generate_fallback_content(self.name, "operational")
        except Exception as e:
            print(f"[CoordinatorAgent] Operational analysis failed: {e}")
            results['operational'] = generate_fallback_content(self.name, "operational")

        # 4. Competitor Analysis
        try:
            competitor_report = competitor_analysis.extract_competitor_analysis(self.name)
            results['competitor'] = competitor_report if competitor_report else generate_fallback_content(self.name, "competitor")
        except Exception as e:
            print(f"[CoordinatorAgent] Competitor analysis failed: {e}")
            results['competitor'] = generate_fallback_content(self.name, "competitor")

        # 5. Key Decision Makers
        try:
            leadership = client_intelligence.extract_leadership_names(self.url)
            results['leadership'] = leadership if leadership else f"Leadership analysis for {self.name} requires additional processing time."
        except Exception as e:
            print(f"[CoordinatorAgent] Leadership extraction failed: {e}")
            results['leadership'] = f"Leadership information for {self.name} will be available shortly."

        # 6. Product Analysis
        try:
            product_report = product_analysis.analyze_client(self.name, self.url)
            results['product'] = product_report if product_report else generate_fallback_content(self.name, "product")
        except Exception as e:
            print(f"[CoordinatorAgent] Product analysis failed: {e}")
            results['product'] = generate_fallback_content(self.name, "product")

        # 6. Final Report Sections
        report = []
        report.append("==== CLIENT INTELLIGENCE REPORT ====")
        report.append(client_data or "[No client intelligence available]")

        # Decision Makers Summary
        report.append("\n==== KEY DECISION MAKERS ====")
        report.append(leadership or "[No leadership data available]")

        report.append("\n==== FINANCIAL INSIGHTS ====")
        report.append(financial_data or "[No financial data found]")

        report.append("\n==== OPERATIONAL SIGNALS ====")
        report.append(ops_data or "[No operational signals found]")

        report.append("\n==== COMPETITOR ANALYSIS ====")
        report.append(competitor_report or "[No competitor report found]")

        report.append("\n==== PRODUCT ANALYSIS ====")
        report.append(product_report or "[No product analysis found]")

        # 7. Combine and display report
        final_report = "\n".join(report)

        print("\n" + "=" * 80)
        print("               PRELYTICS BUSINESS INTELLIGENCE REPORT")
        print("=" * 80)
        print(final_report)
        print("=" * 80)
        print("[SUCCESS] Report generation complete")

        return final_report
