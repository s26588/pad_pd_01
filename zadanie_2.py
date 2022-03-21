class Worker:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary


workers = [
  Worker("Adam", 1983, 1500),
  Worker("Anna", 1981, 1700),
  Worker("Błażej", 1990, 1800),
  Worker("Beata", 1992, 1600),
  Worker("Czesław", 1980, 2000),
  Worker("Cecylia", 1983, 2100),
  Worker("Daniel", 1976, 1900)
]

sum = 0

sum_younger = 0
count_younger = 0

sum_older = 0
count_older = 0

decisive_age = 2022 - 30

for worker in workers:
  sum += worker.salary

  if worker.age > decisive_age:
    sum_younger += worker.salary
    count_younger += 1
  elif worker.age < decisive_age:
    sum_older += worker.salary
    count_older += 1


print(f"Średnie zarobki wynoszą {sum / len(workers)}")

if count_older > 0 and count_younger > 0:
  avg_older = sum_older / count_older
  avg_younger = sum_younger / count_younger

  if avg_older > avg_younger:
    print(f"Pracownicy starsi niż 30 lat zarabiają więcej ({avg_older}), niż młodsi ({avg_younger})")
  elif avg_younger > avg_older:
    print(f"Pracownicy młodsi niż 30 lat zarabiają więcej ({avg_younger}), niż starsi ({avg_older})")
  else:
    print(f"Pracownicy młodsi i starsi niż 30 lat zarabiają tyle samo ({avg_younger})")
else:
  if count_older == 0:
    print("Nie ma pracowników starszych niż 30 lat")

  if count_younger == 0:
    print("Nie ma pracowników młodszych niż 30 lat")
