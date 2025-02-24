# setup stuff
library(tidyverse)
library(janitor)
netflix <- read_csv('private-ViewingActivity.csv')

# rename variables - auto
netflix <- clean_names(netflix)

# rename variables - manual
netflix <- netflix %>%
  rename(type = supplemental_video_type)

# filter data - remove B's profile and types that are not NA
netflix %>%
  filter(profile != 'Bbbbbbb', is.na(type))

# frequency that each device was used - a bad bar chart to practice ggplot
device_count <- as.data.frame(table(netflix$device_type))

ggplot(device_count, aes(y = Var1, x = Freq)) +
  geom_bar(stat = "identity", fill = "lightgreen", color = "black") +
  labs(y = 'Device')