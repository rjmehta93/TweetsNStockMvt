
#loading packages
library(tidytext)
library(stringr)
library(dplyr)
library(ggplot2)


#importing data
tweets<-read.csv("msftT.csv")

# regex to clean tweets (from tidytext package)
replace_reg <- "https://t.co/[A-Za-z\\d]+|http://[A-Za-z\\d]+|&amp;|&lt;|&gt;|RT|https"
unnest_reg <- "([^A-Za-z_\\d#@']|'(?![A-Za-z_\\d#@]))"

# cleaning tweets
tidy_tweets <- tweets %>% 
  filter(!str_detect(Text, "^RT")) %>%
  mutate(text = str_replace_all(Text, replace_reg, "")) %>%
  unnest_tokens(word, text, token = "regex", pattern = unnest_reg) %>%
  filter(!word %in% stop_words$word,
         str_detect(word, "[a-z]"))

#write.csv(tidy_tweets, file = "tidy_tweets.csv")


#counting words
wordCount <- tidy_tweets %>% 
  count(word, sort = TRUE) 

#write.csv(wordCount, file = "wordCount.csv")
#using bing lexicon
bing <- get_sentiments("bing")

# finding sentiment by word similarity with bing liu lexicon
sentiment<-tidy_tweets%>%
  # inner join to find common words 
  inner_join(bing)

#write.csv(sentiment, file = "sentiment.csv")             
tidy_tweets%>% 
top_n(20) %>%
  mutate(word = reorder(word, freq)) %>%
  # Use aes() to put words on the x-axis and frequency on the y-axis
  ggplot(aes(x=word,y=freq))+
  # Make a bar chart with geom_col()
  geom_col() +
  coord_flip() 
