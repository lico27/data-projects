library(readr)

simpsons_episodes <- read_csv("codingStuff/data-projects/tidy-tuesdays/private-simpsons/simpsons_episodes.csv")
View(simpsons_episodes)

library(ggplot2)

year_freq <- as.data.frame(table(simpsons_episodes$original_air_year))

ggplot(year_freq, aes(x = Var1, y = Freq)) +
  geom_col() +
  labs(x = "Release Year",
       y = "Number of episodes")

