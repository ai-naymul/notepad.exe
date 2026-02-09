---
tags: [review, system]
---

# 📅 Review Schedule

> **Spaced Repetition System**
> Review at: 1 day → 3 days → 1 week → 2 weeks → 1 month → 3 months

---

## 🔴 URGENT - Due Today
```tasks
not done
description includes review
due today
```

## 📅 This Week
```tasks
not done
description includes review
due after today
due before in 7 days
sort by due
```

## 📆 Next Week
```tasks
not done
description includes review
due after in 7 days
due before in 14 days
sort by due
```

## 📊 All Pending Reviews
```tasks
not done
description includes review
sort by due
```

---

## 📖 Papers to Review
```dataview
TABLE review-date as "Next Review"
FROM "Papers"
WHERE review-date
SORT review-date ASC
```

## 💡 Concepts to Practice
```dataview
TABLE mastery, last-reviewed
FROM "Concepts"
WHERE mastery != "🟢 mastered"
SORT last-reviewed ASC
```

---

## ➕ Quick Add Review

**Today: 2026-02-04** (update this daily)

Copy-paste and fill in:
```markdown
- [ ] Review [[___]] (1 day) 📅 2026-02-05
- [ ] Review [[___]] (3 days) 📅 2026-02-07
- [ ] Review [[___]] (1 week) 📅 2026-02-11
- [ ] Review [[___]] (2 weeks) 📅 2026-02-18
- [ ] Review [[___]] (1 month) 📅 2026-03-04
```

---

## 📋 Review Log

### Completed This Week
- [x] 

### Completed Last Week
- [x] 
