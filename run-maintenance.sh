#!/bin/bash

# Colors for better readability
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Navigate to project directory
cd /Users/lucascufre/Documents/CookingDocumentation

# Create logs directory if it doesn't exist
mkdir -p logs

# If command line argument provided, use it; otherwise prompt interactively
if [ -n "$1" ]; then
  choice="$1"
  NON_INTERACTIVE=true
else
  NON_INTERACTIVE=false
  clear
  echo -e "${BLUE}╔════════════════════════════════════════════╗${NC}"
  echo -e "${BLUE}║   Knowledge Base Maintenance Menu         ║${NC}"
  echo -e "${BLUE}╚════════════════════════════════════════════╝${NC}"
  echo ""
  echo -e "${GREEN}1.${NC} Daily Parse          ${YELLOW}(~5 min)${NC}  - Process new documents"
  echo -e "${GREEN}2.${NC} Weekly Validation    ${YELLOW}(~15 min)${NC} - Check quality & duplicates"
  echo -e "${GREEN}3.${NC} Monthly Cleanup      ${YELLOW}(~30 min)${NC} - Archive & consolidate"
  echo -e "${GREEN}4.${NC} Full Maintenance     ${YELLOW}(~50 min)${NC} - Run all tasks"
  echo -e "${GREEN}5.${NC} Quick Status                  - View recent logs"
  echo -e "${GREEN}6.${NC} Exit"
  echo ""
  echo -e "${BLUE}────────────────────────────────────────────${NC}"
  read -p "Select option (1-6): " choice
fi

case $choice in
  1)
    echo ""
    echo -e "${BLUE}Starting Daily Parse...${NC}"
    ./scripts/daily-parse.sh
    ;;
  2)
    echo ""
    echo -e "${BLUE}Starting Weekly Validation...${NC}"
    ./scripts/weekly-validation.sh
    ;;
  3)
    echo ""
    echo -e "${BLUE}Starting Monthly Cleanup...${NC}"
    ./scripts/monthly-cleanup.sh
    ;;
  4)
    echo ""
    echo -e "${BLUE}Starting Full Maintenance...${NC}"
    echo ""
    echo "1/3 - Daily Parse"
    ./scripts/daily-parse.sh
    echo ""
    echo "2/3 - Weekly Validation"
    ./scripts/weekly-validation.sh
    echo ""
    echo "3/3 - Monthly Cleanup"
    ./scripts/monthly-cleanup.sh
    ;;
  5)
    echo ""
    echo -e "${BLUE}Recent Maintenance Activity:${NC}"
    echo ""
    if [ -d "logs" ]; then
      echo -e "${YELLOW}Last 5 log files:${NC}"
      ls -lt logs/*.log 2>/dev/null | head -5
      echo ""
      echo -e "${YELLOW}Latest daily parse:${NC}"
      tail -20 logs/daily-parse-*.log 2>/dev/null | tail -10
    else
      echo "No logs found yet"
    fi
    echo ""
    if [ "$NON_INTERACTIVE" = false ]; then
      read -p "Press Enter to continue..."
      "$0"
    fi
    exit 0
    ;;
  6)
    echo ""
    echo -e "${GREEN}✓ Maintenance complete. Check logs/ directory for reports.${NC}"
    exit 0
    ;;
  *)
    echo ""
    echo -e "${RED}Invalid option. Please select 1-6.${NC}"
    if [ "$NON_INTERACTIVE" = false ]; then
      sleep 2
      "$0"
    fi
    exit 1
    ;;
esac

echo ""
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ Done!${NC}"
echo ""
echo "📁 Check these locations:"
echo "   • logs/ - Execution logs and reports"
echo "   • 08-documents-to-parse/review-needed/ - Files needing manual review"
echo ""
if [ "$NON_INTERACTIVE" = false ]; then
  read -p "Press Enter to return to menu or Ctrl+C to exit..."
  "$0"
fi
