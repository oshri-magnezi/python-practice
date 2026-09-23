# Python Practice

תרגילי Python בסיסיים מהקורס — פונקציות, מחלקות, ובדיקות.

## Contents

- **`main.py`** — הקובץ הראשי. מכיל:
  - `Rectangle` — מחלקה פשוטה עם רוחב וגובה ומתודה שמחזירה שטח.
  - `second_largest(nums)` — מחזירה את המספר השני-בגודלו ברשימה, במעבר יחיד (O(n)).
- **`second_largest_another_solution.py`** — פתרון חלופי ל-`second_largest` בגישת מיון (`sorted` + `set`).
- **`test_second_largest.py`** — בדיקות ל-`second_largest` באמצעות `assert` (רשימה רגילה, כפילויות, מספרים שליליים).

## How to run

הרצת הקובץ הראשי:
```bash
python main.py
```

הרצת הבדיקות:
```bash
python test_second_largest.py
```

## Requirements

- Python 3.14