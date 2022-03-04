#!/usr/local/bin/Rscript

args = commandArgs(trailingOnly=TRUE)
library(knitr)
library(rmarkdown)
Sys.setenv(RSTUDIO_PANDOC="/Applications/RStudio.app/Contents/MacOS/pandoc")

for(arg in args){
	render( arg,  output_format="bookdown::pdf_document2", output_dir="output", output_file=gsub('.Rmd$','.pdf',arg) ) #intermediates_dir="output" #Will create tons of empty directories of referenced directories for some reason
}
