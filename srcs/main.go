package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"github.com/gin-gonic/gin"
	"github.com/sashabaranov/go-openai"
)

var mistralClient *openai.Client

func init() {
	apiKey := os.Getenv("MISTRAL_API_KEY")
}