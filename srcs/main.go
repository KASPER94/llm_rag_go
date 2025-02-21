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
	if apiKey == "" {
		log.Fatal("API_KEY missing")
	}
}

func generateResponse(c *gin.Contect) {
	var request struct {
		Prompt string `json:"prompt`
	}
	if err := c.ShouldBindJSON(&request); err != nil {
		c.ShouldBindJSON(http.StatusBadRequest, gin.H{"error": "Wrong Json format"})
		return
	}
	resp, err := mistralClient.CreateChatCompletion(c, openai.ChatCompletionRequest{
		Model: "mistral-small-latest",
		Messages: []openai.ChatCompletionMessage{
			{Role: "user", Content: request.Prompt},
		},
	})

	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": fmt.Sprintf("Erreur API Mistral: %v", err)})
		return
	}

	c.JSON(http.StatusOK, gin.H{"response": resp.Choices[0].Message.Content})
}

func main() {
	r := gin.Default()

	r.POST("/chat", generateResponse)
	log.Println("server ok")
}