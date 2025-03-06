# setup stuff
library(tidyverse)
library(janitor)
netflix <- read_csv('private-ViewingActivity.csv')

# rename variables - auto
netflix <- clean_names(netflix)

# rename variables - manual
netflix <- netflix %>%
  rename(type = supplemental_video_type)

# filter data - remove B's profile and exclude unwanted columns
netflix %>%
  filter(profile != 'Bbbbbbb', is.na(type)) %>%
  select(-type, -country, -attributes)

# get things watched over 10 times
episode_count <- table(netflix$title)
netflix$title[netflix$title %in% names(episode_count[episode_count < 30])] <- NA
rewatched_episodes <- as.data.frame(episode_count)

# arrange most watched episodes by watch count
rewatched_episodes %>%
  arrange(-Freq)

# hide less commonly used devices
device_count <- table(netflix$device_type)
netflix$device_type[netflix$device_type %in% names(device_count[device_count < 75])] <- NA

# frequency that each device was used - a bad bar chart to practice ggplot
common_devices <- as.data.frame(device_count)

ggplot(common_devices, aes(x=reorder(Var1, Freq), y = Freq)) +
  geom_bar(stat = "identity", fill = "seagreen") +
  labs(x = 'Device',
       y = 'Frequency of Use',
       caption = 'x-axis uses log10 transformation') + 
  scale_y_log10() +
  theme_minimal() +
  coord_flip()