---
cssclass: dashboard
---

# 📊 Knowledge Dashboard

**Today:** `= date(today)` | **This Week:** Week `= dateformat(date(today), "ww")`

---

## ⏰ Due Today
```tasks
not done
due today
sort by priority
```

## 📅 Due This Week
```tasks
not done
due after today
due before in 7 days
sort by due
```

## 🔴 Overdue!
```tasks
not done
due before today
```

---

## 📚 Currently Reading
```dataview
TABLE status, date(file.cday) as "Started"
FROM "Papers"
WHERE status = "🟡 reading"
SORT file.ctime DESC
```

## 🎯 Active Projects
```dataview
LIST
FROM "Projects"
WHERE contains(status, "active")
```

---

## 📈 This Week's Stats

**Papers completed:** 
**CP problems:** 
**Commits:** 
**Daily notes:** 

---

## 🔗 Quick Links
- [[Questions]] - Open questions
- [[Review-Schedule]] - Revision tracker  
- [[Weekly-Reviews/{{date:YYYY-[W]ww}}]] - This week's review
- [[CP/Patterns]] - CP patterns reference

---

## 🔥 Recently Modified
```dataview
TABLE file.mtime as "Modified"
FROM ""
SORT file.mtime DESC
LIMIT 10
```
