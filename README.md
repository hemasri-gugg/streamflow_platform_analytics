# StreamFlow Platform Analytics

> **An end-to-end Business Intelligence & Data Analytics project developed for StreamFlow, a fictional subscription-based video streaming platform.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Google BigQuery](https://img.shields.io/badge/Google_BigQuery-Cloud-orange)
![SQL](https://img.shields.io/badge/SQL-Analytics-green)
![GitHub](https://img.shields.io/badge/GitHub-Version_Control-black)
![Status](https://img.shields.io/badge/Status-In_Development-success)

</p>

---

# Table of Contents

- Executive Summary
- About StreamFlow
- Industry Overview
- Business Challenges
- Business Objectives
- Project Overview
- Solution Architecture
- Technology Stack
- Data Architecture
- Project Workflow
- Analytical Modules
- Dashboard Portfolio
- Business Impact
- Repository Structure
- Project Roadmap
- Future Enhancements

---

# Executive Summary

The subscription video streaming industry has transformed the way audiences consume digital entertainment. Millions of customer interactions—including subscriptions, payment transactions, content consumption, marketing engagement, and customer support activities—are generated every day. As streaming platforms continue to grow, transforming this operational data into meaningful business intelligence becomes essential for informed decision-making.

**StreamFlow** is a fictional subscription-based video streaming platform created to simulate the operational environment of a modern streaming business. Like real-world streaming services, StreamFlow manages subscribers across multiple regions, offers a diverse content library, and continuously seeks to improve customer engagement, subscriber retention, and recurring revenue.

To support these business objectives, I developed **StreamFlow Platform Analytics**, an end-to-end Business Intelligence and Data Analytics project that demonstrates how modern cloud technologies can be used to design a scalable analytics ecosystem. The project simulates the complete analytics lifecycle—from synthetic data generation and cloud data warehousing to SQL-based business analysis and interactive executive dashboards.

Although StreamFlow is fictional, the business scenarios, analytical workflows, and technology stack closely resemble those used by modern subscription-based streaming companies.

---

# About StreamFlow

## The Platform

**StreamFlow** is a fictional subscription-based video streaming platform designed exclusively for this project.

The platform enables subscribers to stream movies, television series, documentaries, children's programming, and exclusive original productions across multiple devices through flexible monthly and annual subscription plans. To enhance customer experience, StreamFlow focuses on personalized recommendations, seamless streaming performance, and continuous expansion of its content catalog.

While fictional, the platform has been designed to reflect the business model, customer journey, and operational complexity commonly found in modern streaming services.

### Business Operations

Every day, StreamFlow generates operational data across multiple business functions, including:

- Customer registrations
- Subscription purchases
- Payment transactions
- Subscription renewals
- Subscription cancellations
- Content consumption
- Watch history
- Marketing campaign responses
- Customer support interactions

These operational datasets provide valuable business information; however, they originate from different systems and departments, making it difficult to obtain a unified view of organizational performance.

---

# Industry Overview

The Subscription Video-on-Demand (SVOD) industry is one of the fastest-growing sectors within digital entertainment. Organizations such as Netflix, Disney+, Amazon Prime Video, and Max rely heavily on Business Intelligence and advanced analytics to optimize customer experiences, improve recommendation systems, reduce subscriber churn, maximize recurring revenue, and evaluate content performance.

Modern streaming platforms continuously generate large volumes of transactional data across customer acquisition, subscription management, billing, content consumption, marketing campaigns, and customer support. Converting these diverse datasets into actionable business insights requires scalable cloud-based analytics platforms supported by dimensional data modeling, centralized data warehousing, and interactive reporting solutions.

StreamFlow was designed to replicate these industry characteristics, providing a realistic business environment for developing an end-to-end analytics solution while avoiding the limitations of proprietary production datasets.

---

# Business Challenges

As StreamFlow expanded its subscriber base, business leaders recognized that operational data was becoming increasingly fragmented across multiple business functions. Individual departments generated independent reports, but there was no centralized platform capable of delivering a consistent and organization-wide view of business performance.

This fragmented reporting environment made it difficult to monitor revenue trends, understand customer behavior, evaluate content performance, measure marketing effectiveness, and proactively identify customers at risk of churn.

Without a centralized analytics solution, answering strategic business questions required significant manual effort and often resulted in delayed or inconsistent decision-making.

Key business questions included:

- Which subscription plans generate the highest recurring revenue?
- Which customer segments are most likely to churn?
- Which content categories generate the highest engagement?
- Which marketing campaigns deliver the strongest return on investment?
- Which geographic regions contribute the highest customer lifetime value?
- How effectively is the customer support team resolving customer issues?
- Which customer behaviors indicate future subscription cancellations?

These challenges highlighted the need for a scalable analytics platform capable of transforming operational data into a single source of truth for business stakeholders.

---

# Business Objectives

To support long-term business growth, StreamFlow established the following strategic objectives for its analytics initiative:

- Reduce customer churn
- Improve customer retention
- Increase Monthly Recurring Revenue (MRR)
- Analyze customer engagement
- Evaluate content performance
- Measure marketing campaign effectiveness
- Improve customer support efficiency
- Monitor subscription growth
- Deliver executive dashboards for data-driven decision-making

---

# Project Overview

This repository documents my implementation of **StreamFlow Platform Analytics**, an end-to-end Business Intelligence and Data Analytics project developed for the fictional StreamFlow platform.

Rather than analyzing an existing public dataset, I designed a complete analytics ecosystem that simulates how a modern subscription-based streaming business collects, stores, analyzes, and visualizes operational data.

The project demonstrates the responsibilities typically performed by Data Analysts and Business Intelligence Engineers throughout an analytics project lifecycle.

The implementation includes:

- Designing a dimensional data warehouse using a Star Schema
- Generating realistic synthetic business datasets using Python
- Building a data validation and preprocessing workflow
- Implementing a cloud-based analytical repository using Google BigQuery
- Developing business-focused SQL analytics
- Creating interactive Power BI dashboards
- Managing project documentation and version control using GitHub

Although StreamFlow is fictional, the architecture, workflows, analytical methodologies, and reporting techniques closely reflect enterprise analytics implementations used by subscription-based digital businesses.

---

# Solution Architecture

```text
                  Python
                     │
                     ▼
      Synthetic Data Generation
                     │
                     ▼
            Data Validation
                     │
                     ▼
             CSV Datasets
                     │
                     ▼
      Google BigQuery Data Warehouse
                     │
                     ▼
      Dimensional Star Schema Model
                     │
                     ▼
          Business SQL Analytics
                     │
                     ▼
           Executive Dashboards
                     │
                     ▼
      Data-Driven Business Decisions
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Cloud Data Warehouse | Google BigQuery |
| Database | BigQuery SQL, MySQL |
| Business Intelligence | UI based Dashboards|
| Version Control | Git & GitHub |
| Documentation | Markdown |

---

# Data Architecture

The StreamFlow Platform Analytics project follows a **dimensional modeling approach** using a **Star Schema** to support analytical workloads.

The warehouse consists of multiple fact and dimension tables designed to optimize query performance and simplify business reporting.

### Fact Tables

- Fact Subscriptions
- Fact Payments
- Fact Watch History
- Fact Campaign Responses
- Fact Customer Support

### Dimension Tables

- Customers
- Subscription Plans
- Content
- Time
- Geography
- Campaigns
- Support Agents

This architecture provides a scalable foundation for Business Intelligence reporting while supporting efficient analytical queries across multiple business domains.

> **📌 ER Diagram / Star Schema:** *(Add diagram here)*

---

# Project Workflow

```text
Business Requirements
          │
          ▼
Data Modeling
          │
          ▼
Python Data Generation
          │
          ▼
Data Validation
          │
          ▼
Google BigQuery
          │
          ▼
Star Schema Design
          │
          ▼
SQL Business Analytics
          │
          ▼
Dashboards
          │
          ▼
Business Insights
```

---

# Analytical Modules

The StreamFlow Platform Analytics project is organized into multiple analytical domains, each addressing a specific business function.

## 👥 Customer Analytics

- Customer acquisition analysis
- Customer segmentation
- Churn analysis
- Retention metrics
- Customer Lifetime Value (CLV)

---

## Revenue Analytics

- Monthly Recurring Revenue (MRR)
- Revenue trends
- Subscription plan performance
- Payment analysis

---

## Content Analytics

- Most watched content
- Genre performance
- Viewer engagement
- Average watch duration

---

## Marketing Analytics

- Campaign ROI
- Conversion rate
- Customer acquisition cost
- Marketing effectiveness

---

## Customer Support Analytics

- Ticket volume
- Resolution time
- Agent performance
- Customer satisfaction trends

---

# Dashboard Portfolio

The Power BI solution consists of multiple executive dashboards designed to support business stakeholders at different organizational levels.

### Executive Dashboard

High-level business KPIs and overall platform performance.

### Customer Dashboard

Customer acquisition, churn, retention, and segmentation insights.

### Revenue Dashboard

Revenue performance, subscription trends, and MRR analysis.

### Content Dashboard

Content popularity, watch trends, and viewer engagement.

### Marketing Dashboard

Campaign performance, ROI, and conversion metrics.

### Customer Support Dashboard

Support efficiency, ticket resolution, and agent performance.

> **Dashboard screenshots will be added after project completion.**

---

# Business Impact

StreamFlow Platform Analytics transforms fragmented operational data into actionable business intelligence through centralized reporting and interactive dashboards.

The solution enables business stakeholders to:

- Monitor subscription growth
- Identify customer churn risks
- Analyze customer engagement
- Evaluate marketing performance
- Track revenue trends
- Measure content popularity
- Improve customer support operations
- Support strategic decision-making through reliable analytics

Although developed as a portfolio project, the overall analytical workflow closely mirrors the architecture, methodologies, and reporting practices commonly implemented within enterprise Business Intelligence environments.

---

# Repository Structure

```text
StreamFlow-Platform-Analytics/
│
├── datasets/
│
├── python/
│   ├── data_generation/
│   ├── validation/
│   └── utilities/
│
├── sql/
│   ├── customer_analytics.sql
│   ├── revenue_analytics.sql
│   ├── content_analytics.sql
│   ├── marketing_analytics.sql
│   └── support_analytics.sql
│
│
├── dashboards/
│
├── docs/
│
├── images/
│
├── README.md
│
└── LICENSE
```

---

# Project Roadmap

| Phase | Status |
|--------|:------:|
| Project Planning | ✅ Completed |
| Business Understanding | ✅ Completed |
| Data Modeling | ✅ Completed |
| Python Data Generation | ✅ Completed |
| Data Validation | ✅ Completed |
| Google BigQuery Implementation | ✅ Completed |
| SQL Analytics | ✅ Completed |
| Dashboards | ✅ Completed |
| Documentation | 🚧 In Progress |

---

# Future Enhancements

- Machine Learning-based churn prediction
- Personalized recommendation engine
- Real-time streaming analytics
- Automated ETL orchestration
- BigQuery scheduled queries
- CI/CD for analytics workflows
- KPI monitoring and alerting
- Executive performance scorecards

---

# Contributing

Contributions, suggestions, and feedback are welcome. Feel free to fork the repository, raise issues, or submit pull requests to improve the project.

---

# License

This project is licensed under the **MIT License**.

---

<p align="center">
Built with ❤️ to demonstrate how modern analytics can transform business data into strategic insights for a fictional video streaming platform.
</p>