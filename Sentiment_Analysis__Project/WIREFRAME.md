# UI/UX Wireframe - Sentiment Analysis Application

## 📱 Application Overview

This document outlines the user interface design for the Sentiment Analysis Application, a Streamlit-based web application for analyzing Amazon product reviews with interactive visualizations and filters.

---

## 🎨 Layout Structure

### Main Page Layout (Desktop View)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    🎯 Amazon Review Sentiment Analysis                  │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────┬─────────────────────────────────────────────────────────┐
│              │                                                         │
│   SIDEBAR    │              MAIN CONTENT AREA                         │
│              │                                                         │
│   [Filters]  │  ┌─────────────────────────────────────────────────┐  │
│              │  │  📊 Dataset Overview                            │  │
│              │  │  ─────────────────────────────────────────────  │  │
│              │  │  [Data Table Preview - First 10 rows]          │  │
│   [Stats]    │  │                                                 │  │
│              │  └─────────────────────────────────────────────────┘  │
│              │                                                         │
│              │  ┌──────────────────┬──────────────────┐               │
│              │  │ Rating           │ Review Count     │               │
│              │  │ Distribution     │ by Country       │               │
│              │  │ [Bar Chart]      │ [Line Chart]     │               │
│              │  └──────────────────┴──────────────────┘               │
│              │                                                         │
│              │  ┌──────────────────┬──────────────────┐               │
│              │  │ Country-wise     │ Average Rating   │               │
│              │  │ Sentiment        │ Comparison       │               │
│              │  │ [Pie Chart]      │ [Bar Chart]      │               │
│              │  └──────────────────┴──────────────────┘               │
│              │                                                         │
│              │  ┌─────────────────────────────────────┐               │
│              │  │  Review Date Timeline                │               │
│              │  │  [Area Chart]                        │               │
│              │  └─────────────────────────────────────┘               │
│              │                                                         │
└──────────────┴─────────────────────────────────────────────────────────┘
```

---

## 📍 Component Details

### 1. Header Section
**Location**: Top of page  
**Components**:
- Application title: "🎯 Amazon Review Sentiment Analysis"
- Subtitle: "Analyzing sentiment patterns across countries"
- Layout: Centered, large font (h1)

```
┌────────────────────────────────────────────────────────┐
│        🎯 Amazon Review Sentiment Analysis             │
│    Analyzing sentiment patterns across countries      │
└────────────────────────────────────────────────────────┘
```

---

### 2. Sidebar - Controls & Filters
**Location**: Left side (width: ~25%)  
**Background**: Light gray (#F5F5F5)  
**Components**:

#### 2.1 Filter Section
```
┌──────────────────────────────────┐
│ FILTERS                          │
├──────────────────────────────────┤
│                                  │
│ 🌍 Select Countries              │
│ ┌────────────────────────────┐  │
│ │ ☑ USA                      │  │
│ │ ☑ UK                       │  │
│ │ ☑ India                    │  │
│ │ ☑ Germany                  │  │
│ │ ☑ France                   │  │
│ │ ☑ Japan                    │  │
│ │ [Show more]                │  │
│ └────────────────────────────┘  │
│                                  │
│ ⭐ Rating Filter                 │
│ ┌────────────────────────────┐  │
│ │ ○ All Ratings              │  │
│ │ ○ Positive (4-5)           │  │
│ │ ○ Neutral (3)              │  │
│ │ ○ Negative (1-2)           │  │
│ └────────────────────────────┘  │
│                                  │
│ 📅 Date Range                    │
│ From: [Date Picker]              │
│ To:   [Date Picker]              │
│                                  │
│ [🔄 Reset Filters] [Apply]      │
│                                  │
└──────────────────────────────────┘
```

#### 2.2 Statistics Panel
```
┌──────────────────────────────────┐
│ 📊 STATISTICS                    │
├──────────────────────────────────┤
│                                  │
│ Total Reviews:                   │
│ ════════════════ 15,432          │
│                                  │
│ Total Countries:                 │
│ ════════════════ 8               │
│                                  │
│ Date Range:                      │
│ 2024-01-15 → 2025-12-20          │
│                                  │
│ Avg Rating:                      │
│ ════════════════ 4.2 / 5 ⭐      │
│                                  │
│ Positive Reviews:                │
│ ════════════════ 68%             │
│                                  │
└──────────────────────────────────┘
```

---

### 3. Main Content Area

#### 3.1 Dataset Overview Section
**Location**: Top of main content  
**Height**: Auto-expanding based on data

```
┌─────────────────────────────────────────────────────────┐
│ 📋 Dataset Overview                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ ┌─────────┬──────────┬────────┬──────────┬──────────┐  │
│ │ Country │ Rating   │ Review │ Avg      │ Count    │  │
│ │         │          │ Count  │ Rating   │          │  │
│ ├─────────┼──────────┼────────┼──────────┼──────────┤  │
│ │ USA     │ 4.5      │ 2,345  │ 4.5      │ 2345     │  │
│ │ UK      │ 4.2      │ 1,890  │ 4.2      │ 1890     │  │
│ │ India   │ 4.1      │ 1,567  │ 4.1      │ 1567     │  │
│ │ Germany │ 4.3      │ 1,234  │ 4.3      │ 1234     │  │
│ │ ...     │ ...      │ ...    │ ...      │ ...      │  │
│ └─────────┴──────────┴────────┴──────────┴──────────┘  │
│                                                         │
│ Showing 1-10 of 8 countries                             │
│ [Download as CSV]  [Download as Excel]                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### 3.2 Two-Column Visualization Section 1
**Layout**: 2 equal columns

```
┌──────────────────────────┬──────────────────────────┐
│  Rating Distribution     │ Review Count by Country  │
│  (Bar Chart)             │ (Line Chart)             │
│                          │                          │
│  ┌────┐                  │ ┌────────────────────┐  │
│  │ 5★ │████████████  45% │ │   5000             │  │
│  │ 4★ │████████  35%     │ │   ╱╲               │  │
│  │ 3★ │████  12%         │ │  ╱  ╲    ╱╲        │  │
│  │ 2★ │██  5%            │ │ ╱    ╲──╱  ╲   ╱╲ │  │
│  │ 1★ │█  3%             │ │             ╲─╱  ╲ │  │
│  └────┘                  │ │ ├──┼──┼──┼──┼──┼──┼ │  │
│                          │ │ US UK DE FR JP ...  │  │
│                          │ └────────────────────┘  │
└──────────────────────────┴──────────────────────────┘
```

#### 3.3 Two-Column Visualization Section 2
**Layout**: 2 equal columns

```
┌──────────────────────────┬──────────────────────────┐
│  Country-wise Sentiment  │ Average Rating           │
│  Distribution            │ Comparison               │
│  (Pie Chart)             │ (Horizontal Bar Chart)   │
│                          │                          │
│        ◯ USA 25%         │ USA      ████████ 4.5    │
│       ◯◯ UK 20%          │ Germany  ███████ 4.3     │
│      ◯◯◯ India 18%       │ UK       ██████ 4.2      │
│     ◯◯◯◯ Germany 15%     │ France   ██████ 4.1      │
│    ◯◯◯◯◯ Japan 12%       │ Japan    █████ 3.9       │
│   ◯◯◯◯◯◯ Other 10%       │ India    █████ 3.8       │
│                          │                          │
│                          │                          │
└──────────────────────────┴──────────────────────────┘
```

#### 3.4 Full-Width Visualization Section
**Layout**: Full width

```
┌──────────────────────────────────────────────────────┐
│  Review Date Timeline (Area Chart)                   │
│  Showing review volume over time                     │
├──────────────────────────────────────────────────────┤
│                                                      │
│            ╱╲      ╱╲                                │
│           ╱  ╲    ╱  ╲    ╱╲                         │
│          ╱    ╲  ╱    ╲  ╱  ╲    ╱╲                  │
│    ▁▂▃▄▅▆▇█▁▂▃▄▅▆▇█▁▂▃▄▅▆▇█▁▂▃▄▅▆▇█               │
│                                                      │
│  ├──────┼──────┼──────┼──────┼──────┼──────┤       │
│  Jan'24 Apr'24 Jul'24 Oct'24 Jan'25 Apr'25          │
│                                                      │
│  [Legend: __ USA  __ UK  __ India  __ Germany]      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🎯 User Flow

### Primary User Journeys

#### Journey 1: Country-Specific Analysis
```
1. User opens application
   ↓
2. Default view shows all countries (15,432 total reviews)
   ↓
3. User filters sidebar → Select specific countries (e.g., USA, UK)
   ↓
4. Click "Apply" or auto-update
   ↓
5. All visualizations update to show filtered data
   ↓
6. User views country-specific insights
   ↓
7. Option to download filtered data as CSV/Excel
```

#### Journey 2: Sentiment Trend Analysis
```
1. User views Review Date Timeline chart
   ↓
2. Identifies a spike in reviews during a period
   ↓
3. Filters by date range using sidebar date picker
   ↓
4. Further filters by rating (Positive/Neutral/Negative)
   ↓
5. Views filtered dataset in overview table
   ↓
6. Downloads insights as report
```

#### Journey 3: Performance Comparison
```
1. Views "Average Rating Comparison" bar chart
   ↓
2. Identifies top-performing countries
   ↓
3. Uses country filter to focus on specific regions
   ↓
4. Compares rating distributions across selected countries
   ↓
5. Exports visual comparisons for presentation
```

---

## 🎨 Color Scheme

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Primary | Red | #FF6B6B | Buttons, highlights, accents |
| Background | Light Gray | #F5F5F5 | Main background |
| Secondary Bg | White | #FFFFFF | Card backgrounds |
| Text | Dark Gray | #262730 | Primary text |
| Borders | Light Gray | #E0E0E0 | Dividers, borders |
| Positive | Green | #51CF66 | Positive sentiment, success |
| Negative | Red | #FF6B6B | Negative sentiment, warnings |
| Neutral | Orange | #FFD43B | Neutral sentiment |
| Chart 1 | Blue | #4C72B0 | Visualizations |
| Chart 2 | Green | #55A868 | Visualizations |
| Chart 3 | Orange | #DD8452 | Visualizations |

---

## 🔤 Typography

| Element | Font | Size | Weight | Usage |
|---------|------|------|--------|-------|
| Page Title | Sans-serif | 32px | Bold | Main heading |
| Section Title | Sans-serif | 20px | Bold | Section headers |
| Card Title | Sans-serif | 16px | Semi-bold | Card headings |
| Body Text | Sans-serif | 14px | Regular | Regular content |
| Small Text | Sans-serif | 12px | Regular | Captions, labels |
| Buttons | Sans-serif | 14px | Semi-bold | CTA buttons |

---

## 📐 Component Specifications

### Buttons
- **Primary Button** (Apply, Download)
  - Background: #FF6B6B
  - Text: White
  - Padding: 10px 20px
  - Border Radius: 4px
  - Hover: Darker red (#FF5252)

- **Secondary Button** (Reset, Show more)
  - Background: #E0E0E0
  - Text: #262730
  - Padding: 10px 20px
  - Border Radius: 4px
  - Hover: #D0D0D0

### Cards
- Border Radius: 8px
- Box Shadow: 0 2px 4px rgba(0,0,0,0.1)
- Padding: 20px
- Background: #FFFFFF

### Input Fields
- Border: 1px solid #E0E0E0
- Border Radius: 4px
- Padding: 10px
- Font Size: 14px
- Focus Border: #FF6B6B

---

## 📊 Chart Specifications

### Bar Charts
- Type: Horizontal/Vertical bar charts
- Color: Gradient from #FF6B6B to #FFB3B3
- Hover: Show value tooltip
- Legend: Bottom or right side

### Line Charts
- Type: Multi-line with markers
- Stroke Width: 2px
- Markers: 4px radius
- Area Fill: Transparent with 30% opacity
- Legend: Top right

### Pie Charts
- Donut style with center label
- Colors: Rainbow gradient palette
- Hover: Highlight slice with shadow
- Label: Country name + percentage

### Area Charts
- Stacked or overlapping
- Transparency: 60% fill opacity
- Grid: Subtle background grid
- Hover: Highlight specific area

---

## 📱 Responsive Design

### Desktop (1200px+)
- 2-column layout for visualizations
- Full-width tables with horizontal scroll
- Sidebar always visible
- All features accessible

### Tablet (768px - 1199px)
- Single-column layout for visualizations
- Sidebar becomes collapsible
- Tables with vertical scroll
- Touch-friendly buttons (48px min height)

### Mobile (< 768px)
- Full-width single column
- Sidebar as bottom drawer/menu
- Stacked visualizations
- Simplified data table (key columns only)
- Large touch targets (56px min height)

---

## ⚙️ Interactive Features

### 1. Dynamic Filtering
- Real-time chart updates on filter change
- Auto-update toggle option
- "Apply" button for manual update
- "Reset Filters" for quick reset to defaults

### 2. Data Export
- Download table as CSV
- Download table as Excel
- Download chart as PNG
- Export full report as PDF

### 3. Tooltips
- Hover on data points → Show exact value
- Hover on section titles → Show description
- Hover on country names → Show additional stats

### 4. Expandable Sections
- Click "Show more" to expand country list
- Collapsible filter panels
- Expandable data rows for details

### 5. Sorting & Pagination
- Sort tables by column (ascending/descending)
- Pagination controls for large datasets
- "Show X entries" dropdown (10, 25, 50, 100)

---

## 🔔 Notifications & Messages

### Success Messages
```
✓ Filters applied successfully
✓ Data downloaded successfully
```

### Error Messages
```
✗ Error loading data. Please try again.
✗ Invalid date range selected
```

### Info Messages
```
ⓘ Showing 1-10 of 100 records
ⓘ Last updated: 2026-01-15 14:30:00
```

---

## 🚀 Future Enhancements

1. **Advanced Analytics**
   - Predictive sentiment trends
   - Anomaly detection in review spikes
   - Customer segmentation analysis

2. **Additional Visualizations**
   - Word clouds for review text analysis
   - Network graphs for relationship analysis
   - Heat maps for time-based patterns

3. **Performance Features**
   - Search functionality across reviews
   - Bookmark favorite reports
   - Scheduled automated reports via email

4. **User Management**
   - User authentication
   - Role-based access control
   - Personal dashboards

5. **API Integration**
   - Real-time data import
   - Third-party dashboard integration
   - Webhook notifications

---

## 📝 Accessibility Standards

- ✓ WCAG 2.1 Level AA compliance
- ✓ Keyboard navigation support
- ✓ Screen reader compatible
- ✓ High contrast mode support
- ✓ Color-blind friendly palettes
- ✓ Alt text for all images/charts
- ✓ ARIA labels for interactive elements

---

## 🔒 Security Considerations

- Sensitive data not visible in URL parameters
- HTTPS encryption for all data transmission
- Session timeout after 30 minutes of inactivity
- User permissions validation on all API calls
- Data sanitization to prevent injection attacks

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Created by**: Design Team (LPU)
