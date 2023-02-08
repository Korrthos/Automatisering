#include <Arduino.h>
#include <map>

using namespace std;

enum StringValue {
  RED,
  GREEN,
  BLUE,
  YELLOW,
  ORANGE,
  BROWN,
  RESET
};

static std::map<String, StringValue> StringValues = {
  { "RED", RED },
  { "GREEN", GREEN },
  { "BLUE", BLUE },
  { "YELLOW", YELLOW },
  { "ORANGE", ORANGE },
  { "BROWN", BROWN },
  { "RESET", RESET }
};


static std::map<String, std::map<String, int>> ServoPositions = {
  {
    "RED",  {
      { "FSM", 45 },
      { "ASV", 45 },
      { "ASH", 90 },
      { "TSV", 45 },
      { "TSM", 90 },
      { "TSH", 90 }
    }
  },
  {
    "GREEN",  {
      { "FSM", 45 },
      { "ASV", 45 },
      { "ASH", 90 },
      { "TSV", 135 },
      { "TSM", 90 },
      { "TSH", 90 }
    }
  },
  {
    "BLUE",  {
      { "FSM", 45 },
      { "ASV", 135 },
      { "ASH", 90 },
      { "TSV", 90 },
      { "TSM", 135 },
      { "TSH", 90 }
    }
  },
  {
    "YELLOW",  {
      { "FSM", 135 },
      { "ASV", 90 },
      { "ASH", 45 },
      { "TSV", 90 },
      { "TSM", 135 },
      { "TSH", 90 }
    }
  },
  {
    "ORANGE",  {
      { "FSM", 135 },
      { "ASV", 90 },
      { "ASH", 135 },
      { "TSV", 90 },
      { "TSM", 90 },
      { "TSH", 45 }
    }
  },
  {
    "BROWN",  {
      { "FSM", 135 },
      { "ASV", 90 },
      { "ASH", 135 },
      { "TSV", 90 },
      { "TSM", 90 },
      { "TSH", 135 }
    }
  },
  {
    "RESET",  {
      { "FSM", 90 },
      { "ASV", 90 },
      { "ASH", 90 },
      { "TSV", 90 },
      { "TSM", 90 },
      { "TSH", 90 }
    }
  },
};
