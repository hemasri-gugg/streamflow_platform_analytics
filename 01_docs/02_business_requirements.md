# StreamFlow Platform Analytics
## Business Requirements Document (BRD)

**Project:** StreamFlow Platform Analytics  
**Document:** Business Requirements  
**Version:** 1.0  
**Status:** Working draft  
**Last updated:** 2 October 2026  
**Organization:** StreamFlow — a fictional subscription-based video-streaming service

---

## 1. Purpose

This document defines the business questions, reporting needs, analytical requirements, and expected outputs for the StreamFlow Platform Analytics project. It acts as a reference for the SQL analysis, data model, and Looker Studio dashboards.

The project uses synthetic data for portfolio demonstration. Findings should be described as analytical examples, not as real-world performance claims about an operating streaming company.

## 2. Business Background

StreamFlow is modeled as a subscription-based video-streaming platform. The business depends on acquiring subscribers, converting them to paid plans, retaining them over time, providing relevant content, and resolving customer issues efficiently.

Data is generated across customer profiles, subscription plans, subscriptions, payments, content, watch history, devices, marketing campaigns, campaign responses, and support tickets. The project brings these datasets together to demonstrate how data analysis can support operational monitoring and business decisions.

## 3. Problem Statement

When customer, subscription, payment, viewing, campaign, and support information is examined separately, it is difficult to build a consistent view of platform performance. Business stakeholders need a structured way to answer questions such as:

- How is the subscriber base changing?
- Which subscription plans contribute most to recorded payment revenue?
- How actively do customers use the platform and its content?
- Which marketing campaigns show stronger response or conversion patterns?
- What types of support issues occur, and how are they resolved?
- What are the key indicators that leadership should monitor together?

The project addresses these questions through documented data preparation, SQL-based analysis, and dashboard reporting.

## 4. Business Objectives

| ID | Objective | Expected outcome |
|---|---|---|
| BO-01 | Establish a consolidated view of platform activity | Consistent reporting across the available datasets |
| BO-02 | Analyze customer and subscription behavior | Visibility into customer segments, subscription status, and retention-related patterns supported by the data |
| BO-03 | Analyze payment and revenue patterns | Monthly and plan-level views of recorded payment activity |
| BO-04 | Understand content engagement | Visibility into watch time, sessions, content categories, and device usage |
| BO-05 | Evaluate campaign activity | Campaign-level response and conversion analysis where attribution fields support it |
| BO-06 | Review customer support operations | Visibility into ticket volume, issue types, resolution patterns, and satisfaction fields available in the data |
| BO-07 | Provide an executive summary | A high-level dashboard for monitoring selected KPIs and trends |
| BO-08 | Create a reproducible portfolio project | Documented data validation, SQL scripts, definitions, and dashboard specifications |

## 5. Stakeholders and Intended Users

The following are intended users for the fictional business scenario; they are not confirmed project sponsors or actual organizational roles.

| Stakeholder / user group | Information need |
|---|---|
| Executive leadership | High-level indicators covering customers, payments, engagement, campaigns, and support |
| Customer / subscription team | Subscriber mix, subscription status, and customer behavior patterns |
| Finance / revenue team | Recorded payment totals, monthly trends, payment status, and plan-level contribution |
| Content team | Viewing activity, watch time, content performance, category trends, and device usage |
| Marketing team | Campaign reach or response indicators, conversions, and campaign comparisons where supported |
| Customer support team | Ticket volumes, ticket categories, resolution status or time, and satisfaction measures where available |
| Data analyst / project maintainer | Validated datasets, reusable queries, documented metric definitions, and maintainable reporting assets |

## 6. Scope

### 6.1 In scope

- Use the project’s synthetic datasets as the analytical source.
- Validate dataset structure, key fields, data types, missing values, duplicates, and basic referential integrity where applicable.
- Document the dataset grain, key columns, and relationships.
- Use SQL to create analytical outputs for:
  - Customer analytics
  - Revenue and payment analytics
  - Content engagement analytics
  - Marketing analytics
  - Customer support analytics
- Define KPI calculations and document known limitations.
- Build a Looker Studio executive overview and supporting analytical dashboards.
- Document the workflow, architecture, assumptions, and project roadmap.
- Use version control and a clear repository structure for project artifacts.

### 6.2 Out of scope

- Access to real StreamFlow customer or payment data.
- Production data pipelines, streaming ingestion, or automated warehouse orchestration.
- Changes to live subscription, billing, content recommendation, marketing, or support systems.
- Predictive churn models, recommendation engines, or machine-learning deployment unless separately scoped.
- Financial accounting, audited revenue recognition, or claims that payment totals equal recognized revenue.
- Causal claims about campaign effectiveness without an appropriate attribution design.
- Production security, compliance certification, and service-level guarantees.

## 7. Business Questions and Analytical Requirements

### 7.1 Executive Overview

**Business need:** Give leadership a concise view of selected platform indicators across the main analytical areas.

**Questions to answer**
- How many customers and subscriptions are represented in the available data?
- What payment activity is recorded over time?
- How much viewing activity is represented by sessions, watch minutes, or watch hours?
- What campaign response and support-ticket indicators are available?
- How are the selected indicators changing over the reporting period?

**Requirements**
- Provide clearly labeled KPI cards and time-based trends where the underlying dates support them.
- Include a reporting period or date filter where appropriate.
- Make metric definitions accessible in documentation.
- Avoid combining metrics with incompatible grains or time windows.

### 7.2 Customer Analytics

**Business need:** Understand the composition and observable behavior of the customer and subscription base.

**Questions to answer**
- How are customers distributed across available segments and demographics?
- How are subscriptions distributed by plan and status?
- What subscription patterns can be described from the available start and end dates?
- Which customer groups differ in observable subscription or engagement behavior?

**Requirements**
- Report customer counts using a clearly defined unique-customer key.
- Show subscription counts separately from unique-customer counts.
- Segment only by fields available in the datasets.
- Define retention, churn, or active-subscriber metrics explicitly before presenting them.
- Do not infer reasons for customer behavior from descriptive data alone.

### 7.3 Revenue and Payment Analytics

**Business need:** Understand recorded payment activity by time, status, plan, and other supported dimensions.

**Questions to answer**
- What payment amount is recorded over time?
- How are payments distributed by payment status and subscription plan?
- Which plans contribute the largest share of recorded successful-payment amounts?
- How do successful and unsuccessful payment records vary over time?

**Requirements**
- Clearly distinguish total payment records, successful payment records, and successful payment amounts.
- Use consistent currency and date handling.
- Exclude or separately report unsuccessful payments when calculating successful-payment totals.
- Document how refunds, failed payments, duplicate records, and missing values are handled if those fields exist.
- Do not label payment-based totals as recognized revenue without an appropriate accounting definition.
- Do not present MRR or ARR as definitive recurring-revenue measures unless the calculation is supported by subscription billing logic and documented assumptions.

### 7.4 Content Analytics

**Business need:** Understand how customers use the platform and which content or content categories receive viewing activity.

**Questions to answer**
- How much watch time and how many viewing sessions are recorded?
- Which titles or categories account for the most viewing activity?
- How does engagement vary over time?
- Which devices are associated with viewing activity?
- Are there observable differences across customer or content segments?

**Requirements**
- Define the grain of a viewing record and the meaning of a session.
- Use a consistent conversion between watch minutes and watch hours.
- Separate session counts from unique viewers and content counts.
- State whether rankings are based on watch time, session count, or another measure.
- Avoid interpreting watch time alone as proof of satisfaction or content quality.

### 7.5 Marketing Analytics

**Business need:** Describe campaign responses and conversion patterns using available campaign and response data.

**Questions to answer**
- How many campaign responses are recorded for each campaign?
- What response or conversion rates can be calculated from the available fields?
- How do campaign outcomes differ by campaign type or channel, where those fields exist?
- What campaign costs and outcomes are recorded, if cost and attribution fields are available?

**Requirements**
- Define the denominator for every response or conversion rate.
- Avoid treating a response record as a unique customer unless the data supports that interpretation.
- Define conversion windows and attribution rules before attributing subscriptions or payments to campaigns.
- Calculate CPA, ROI, or ROAS only when the required cost, outcome, and attribution fields are available and documented.
- Handle zero or missing campaign cost explicitly.
- Label descriptive associations as associations rather than causal campaign effects.

### 7.6 Customer Support Analytics

**Business need:** Understand support demand, issue types, resolution patterns, and available satisfaction measures.

**Questions to answer**
- How many support tickets are recorded over time?
- Which ticket categories or statuses occur most often?
- What resolution-time measures can be calculated from the available timestamps?
- What satisfaction measures are available, and how are they distributed?

**Requirements**
- Define ticket count using a unique ticket identifier.
- Document treatment of open, unresolved, or missing-timestamp tickets when calculating resolution time.
- Use the actual satisfaction field name present in the dataset and confirm its scale before charting it.
- Distinguish average resolution time from median resolution time where useful.
- Do not infer support-agent performance or customer sentiment beyond what the fields support.

## 8. Data Requirements

The project is expected to use the following synthetic datasets. Exact field definitions and data types should be maintained in `data_dictionary.md`.

| Dataset | Primary analytical purpose |
|---|---|
| `dim_customers` | Customer attributes and segmentation |
| `dim_subscription_plans` | Plan names, prices, and plan attributes |
| `dim_content` | Content metadata and categorization |
| `dim_devices` | Device attributes |
| `dim_campaigns` | Campaign metadata |
| `fact_subscriptions` | Subscription records and subscription lifecycle fields |
| `fact_payments` | Payment records, dates, amounts, and statuses |
| `fact_watch_history` | Viewing activity and engagement |
| `fact_campaign_responses` | Recorded campaign responses or outcomes |
| `fact_support_tickets` | Support requests, status, timestamps, and available satisfaction fields |

### Data quality requirements

- Confirm expected columns and data types before analysis.
- Identify missing values in fields required for joins and KPI calculations.
- Check uniqueness of primary identifiers where uniqueness is expected.
- Check whether foreign-key values correspond to known dimension records.
- Validate date ranges, numeric ranges, and allowed status values.
- Check for duplicate or potentially duplicated fact records.
- Record any exclusions, transformations, or assumptions in project documentation.
- Do not silently substitute a field name or metric definition when the source data differs from the documentation.

## 9. KPI Definition and Reporting Requirements

Every KPI shown in a dashboard must have a documented name, business meaning, calculation, grain, date basis, filters, and known limitations.

| KPI / measure | Required definition or control |
|---|---|
| Total customers | Count distinct customer identifiers |
| Subscription count | Count subscription records; do not assume one record per customer |
| Active subscriptions | Define the active-status and date logic used |
| Payment amount | Specify whether the measure includes all payment statuses or only successful payments |
| Successful payment amount | Sum payment amounts only for records meeting the documented successful-payment rule |
| Plan revenue contribution | Plan-level successful-payment amount divided by the corresponding total for the same period and filters |
| Total watch time | Sum valid watch-duration values using a documented unit |
| Watch hours | Watch minutes divided by 60 when source duration is measured in minutes |
| Viewing sessions | Count viewing records or session identifiers according to the dataset grain |
| Campaign response rate | Define numerator, eligible audience denominator, and response criteria |
| Campaign conversion rate | Define conversion event, denominator, attribution window, and deduplication rules |
| Support ticket count | Count distinct ticket identifiers |
| Resolution time | Define the start/end timestamps and handling of unresolved tickets |
| Satisfaction score | Confirm source field, scale, and missing-value handling before aggregation |

These are definition requirements, not a claim that all measures are already implemented or validated.

## 10. Functional Requirements

| ID | Requirement | Acceptance condition |
|---|---|---|
| FR-01 | Validate the input datasets | Validation steps and results are documented |
| FR-02 | Maintain a data dictionary | Datasets, grains, fields, and key relationships are documented |
| FR-03 | Maintain SQL analytics by workstream | Queries are organized, titled, and reproducible against the intended warehouse |
| FR-04 | Produce customer analytics | Outputs address the approved customer questions |
| FR-05 | Produce revenue and payment analytics | Outputs distinguish payment statuses and document revenue-related assumptions |
| FR-06 | Produce content analytics | Outputs distinguish watch time, sessions, viewers, and content counts |
| FR-07 | Produce marketing analytics | Rates and attributed outcomes include documented denominators and attribution assumptions |
| FR-08 | Produce support analytics | Ticket measures use documented timestamp and satisfaction-field logic |
| FR-09 | Build an executive overview dashboard | Selected KPIs and trends are presented with clear labels and filters |
| FR-10 | Build supporting dashboards | Each analytical workstream has relevant charts and business explanations |
| FR-11 | Document project architecture and workflow | Data flow, tools, and processing stages are documented |
| FR-12 | Maintain repository documentation | README, charter, business requirements, data dictionary, and technical documents remain aligned |

## 11. Non-Functional Requirements

- **Clarity:** Dashboard titles, labels, units, and date ranges must be understandable to a business audience.
- **Consistency:** Reused KPIs must use the same definitions across SQL outputs and dashboards.
- **Traceability:** Important dashboard metrics should be traceable to a query and source dataset.
- **Reproducibility:** Scripts and queries should be version-controlled and include setup or execution notes where necessary.
- **Maintainability:** Use a consistent naming convention for files, queries, fields, and dashboard pages.
- **Data privacy:** Use synthetic data only; do not add real personal or payment information.
- **Performance:** Keep queries and dashboard visuals practical for the project's dataset size and chosen platform.
- **Honest reporting:** Clearly disclose assumptions, data limitations, and incomplete implementation status.

## 12. Assumptions, Dependencies, and Constraints

### Assumptions
- All records represent synthetic data created for this portfolio project.
- Dataset and field names may need to be verified against the actual source files before implementation.
- SQL analytics and dashboard metrics will use documented definitions.
- Looker Studio is the selected dashboarding platform.

### Dependencies
- Availability of the source CSV files.
- Successful dataset validation and upload to the intended data platform.
- Correct join keys and compatible data types.
- Access to the relevant MySQL and/or BigQuery environment.
- Availability of the dashboard data source and required fields in Looker Studio.

### Constraints
- Synthetic data cannot establish actual business performance.
- Missing or incomplete fields may limit certain KPIs.
- Campaign effectiveness cannot be established causally from simple response or conversion comparisons.
- Payment records alone may not provide the information required for accounting revenue or recurring-revenue calculations.
- This is a portfolio analytics project, not a production-grade data platform.

## 13. Risks and Mitigations

| Risk | Potential impact | Mitigation |
|---|---|---|
| Inconsistent KPI definitions | Conflicting dashboard figures | Maintain a metric glossary and reuse definitions |
| Incorrect joins or duplicate fact records | Inflated counts or amounts | Validate keys, grains, and join cardinality |
| Missing or mismatched field names | Query failures or misleading metrics | Verify queries against the actual schema before dashboard use |
| Unclear revenue logic | Payment activity misrepresented as recognized revenue | Use precise labels and document assumptions |
| Weak campaign attribution | Unsupported claims about campaign performance | Document denominators, windows, and attribution rules |
| Incomplete timestamps or ticket statuses | Biased resolution-time metrics | Define exclusions and report unresolved records separately |
| Synthetic data mistaken for real results | Misleading portfolio presentation | Label the project and all example findings as synthetic |
| Dashboard complexity | Reduced usability | Prioritize key business questions and use consistent visual hierarchy |

## 14. Deliverables

- Business requirements document
- Project charter
- Data dictionary
- ER diagram and relationship documentation
- Data validation script and documented checks
- SQL analytics files for customer, revenue, content, marketing, and support
- Executive Overview dashboard in Looker Studio
- Supporting dashboards for the analytical workstreams
- Architecture and workflow documentation
- Main project README and roadmap

Deliverable completion should be confirmed against the repository and dashboard links; this list describes the intended project outputs.

## 15. Acceptance Criteria

The project will be considered ready for portfolio presentation when:

- All datasets used in analysis are documented and their synthetic nature is disclosed.
- Data validation steps and important findings are recorded.
- The ER diagram reflects verified keys and relationships.
- SQL scripts are organized by workstream and have clear titles.
- Core KPIs have definitions that can be traced to SQL or dashboard calculations.
- Revenue, campaign, retention, and support metrics include relevant assumptions and caveats.
- Dashboard labels, units, date filters, and chart titles are clear.
- The executive overview and supporting dashboards answer the business questions in this document.
- Documentation is aligned with the implemented schema, queries, and dashboards.
- Known limitations and unfinished items are explicitly recorded rather than presented as complete.

## 16. Traceability Matrix

| Business objective | Analytical area | Expected output |
|---|---|---|
| BO-01 Consolidated platform view | Executive Overview | Cross-functional KPI summary |
| BO-02 Customer and subscription behavior | Customer Analytics | Customer segments and subscription patterns |
| BO-03 Payment and revenue patterns | Revenue Analytics | Payment trends, status breakdown, plan contribution |
| BO-04 Content engagement | Content Analytics | Watch time, sessions, content and device analysis |
| BO-05 Campaign activity | Marketing Analytics | Response and supported conversion analysis |
| BO-06 Support operations | Support Analytics | Ticket volumes, resolution patterns, satisfaction measures where available |
| BO-07 Leadership reporting | Executive Overview | High-level metrics and trends |
| BO-08 Reproducible portfolio | Documentation and repository | Validated data, SQL, definitions, and project documentation |

## 17. Change Control

Changes to business questions, KPI definitions, scope, or dashboard requirements should be recorded in the project documentation. When a metric definition changes, update the relevant SQL, dashboard calculation, data dictionary or metric glossary, and this document as appropriate.

## 18. Related Documents

- [`README.md`](../README.md) — project overview and navigation
- [`project_charter.md`](01_project_charter.md) — project purpose, scope, governance, risks, and milestones
- [`data_dictionary.md`](03_data_dictionary.md) — dataset and field definitions
- `er_diagram.md` — entity relationships and key structure
- `architecture.md` — technical architecture and data flow
- SQL analytics files — implemented analytical queries
- Looker Studio dashboards — visual reporting outputs

---

**Document note:** This is a working business requirements document for a fictional, synthetic-data portfolio project. Verify field names, calculation logic, dashboard links, and implementation status against the actual repository before treating any requirement as completed.
