library(ggplot2)
library(readr)
library(dplyr)
episodes <- read_csv("/Users/liamcottrell/codingStuff/data-projects/tidy-tuesdays/simpsons/simpsons_episodes.csv")
episodes_id <- episodes$id

# find the column titles
names(episodes)

# find the first and last episodes
first_ep <- episodes %>%
  filter(id == min(id)) %>%
  pull(title)

first_ep_year <- episodes %>%
  filter(id == min(id)) %>%
  pull(original_air_year)

last_ep <- episodes %>%
  filter(id == max(id)) %>%
  pull(title)

last_ep_year <- episodes %>%
  filter(id == max(id)) %>%
  pull(original_air_year)

# find highest IMDb ratings
highest_rated_one <- episodes %>%
  filter(imdb_rating == max(imdb_rating, na.rm = TRUE)) %>%
  slice(1) %>%
  pull(title)

highest_rated_one_season <- episodes %>%
  filter(imdb_rating == max(imdb_rating, na.rm = TRUE)) %>%
  slice(1) %>%
  pull(season)

highest_rated_two <- episodes %>%
  filter(imdb_rating == max(imdb_rating, na.rm = TRUE)) %>%
  slice(2) %>%
  pull(title)

highest_rated_two_season <- episodes %>%
  filter(imdb_rating == max(imdb_rating, na.rm = TRUE)) %>%
  slice(2) %>%
  pull(season)

highest_rating <- episodes %>%
  filter(imdb_rating == max(imdb_rating, na.rm = TRUE)) %>%
  slice(1) %>%
  pull(imdb_rating)

# find lowest IMDb ratings
lowest_rated <- episodes %>%
  filter(imdb_rating == min(imdb_rating, na.rm = TRUE)) %>%
  pull(title)

lowest_rated_season <- episodes %>%
  filter(imdb_rating == min(imdb_rating, na.rm = TRUE)) %>%
  pull(season)

lowest_rating <- episodes %>%
  filter(imdb_rating == min(imdb_rating, na.rm = TRUE)) %>%
  pull(imdb_rating)

# find character names in episode titles
main_characters <- c("Homer", "Marge", "Bart", "Lisa", "Maggie")
name_counts <- sapply(main_characters, function(p) sum(grepl(p, episodes$title)))
name_freq <- data.frame(Name = names(name_counts), Count = name_counts)

# visualise frequency of character names appearing in episode titles
ggplot(name_freq, aes(x = Name, y = Count)) +
  geom_bar(stat = "identity") +
  theme_minimal()
