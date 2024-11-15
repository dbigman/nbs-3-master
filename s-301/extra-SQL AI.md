<!-- # Using ChatGPT to Generate Business Questions for the Sakila Database -->

Welcome to this tutorial! You'll learn how to leverage AI tools like ChatGPT to create business questions that you can solve using SQL queries on the Sakila Database. This exercise will enhance your SQL skills and familiarize you with AI-assisted learning.

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Understanding the Sakila Database](#understanding-the-sakila-database)
- [Accessing ChatGPT](#accessing-chatgpt)
- [Crafting Effective Prompts](#crafting-effective-prompts)
  - [Basic Prompt Structure](#basic-prompt-structure)
  - [Example Prompts](#example-prompts)
- [Generating Business Questions](#generating-business-questions)
  - [Step-by-Step Guide](#step-by-step-guide)
  - [Refining Your Prompt](#refining-your-prompt)
- [Selecting and Organizing Questions](#selecting-and-organizing-questions)
  - [Example Selection](#example-selection)
- [Solving Questions with SQL Queries](#solving-questions-with-sql-queries)
  - [Example](#example)
- [Tips for Success](#tips-for-success)
- [Conclusion](#conclusion)

---

## Understanding the Sakila Database

Before you begin, make sure you're familiar with the Sakila Database schema:

- **Tables**: `actor`, `film`, `customer`, `rental`, `payment`, `inventory`, `store`, etc.
- **Relationships**: Understand how tables are connected (e.g., `film_actor` links films and actors).
- **Data**: It's a fictional DVD rental database designed for practice.

*Explore the schema diagram and table descriptions provided in your course materials or online resources.*

---

## Accessing ChatGPT

You'll need access to ChatGPT:

- **Website**: [OpenAI ChatGPT](https://chat.openai.com/)
- **Login**: Use your credentials or sign up if you don't have an account.

---

## Crafting Effective Prompts

To get useful business questions from ChatGPT, you need to write clear and specific prompts.

### Basic Prompt Structure

- **Introduce the Context**: Mention that you're working with the Sakila Database.
- **Specify the Request**: Ask for business questions that require SQL queries to solve.
- **Define the Scope**: You can limit the questions to certain tables or topics.
- **Set the Difficulty Level**: Basic, intermediate, or advanced.

### Example Prompts

- **General Questions**:

Please generate five business questions that can be answered using SQL queries on the Sakila Database.

markdown
Copiar código

- **Specific Focus**:

Generate three advanced-level business questions about customer rental patterns in the Sakila Database.

markdown
Copiar código

- **Topic-Oriented**:

Create four business questions related to film inventory and store performance in the Sakila Database.

markdown
Copiar código

---

## Generating Business Questions

### Step-by-Step Guide

1. **Open ChatGPT** and start a new conversation.
2. **Input Your Prompt** based on the guidelines above.
3. **Review the Output**:
 - Ensure the questions are clear and relevant.
 - If not satisfied, **refine your prompt**.

### Refining Your Prompt

- **If Too Broad**:

The previous questions were too general. Can you provide more specific questions about customer spending habits?

markdown
Copiar código

- **If Too Simple**:

Please provide more complex questions that involve multiple tables and require subqueries or joins.

markdown
Copiar código

---

## Selecting and Organizing Questions

1. **Choose Relevant Questions**:
 - Pick questions that interest you or align with your learning goals.
2. **Organize Them**:
 - Number the questions.
 - Keep them in a document for easy reference.

### Example Selection

1. **Question**: Which customers have rented the most films, and what are their top rented genres?
2. **Question**: What is the total revenue generated by each store, and how does it correlate with the number of staff?
3. **Question**: Identify the top five actors whose films generate the most revenue.

---

## Solving Questions with SQL Queries

For each selected question:

1. **Analyze the Question**:
 - Identify which tables and columns are needed.
2. **Write the SQL Query**:
 - Use appropriate SQL clauses (`SELECT`, `JOIN`, `WHERE`, `GROUP BY`, etc.).
3. **Execute the Query**:
 - Run it on the Sakila Database.
4. **Validate the Results**:
 - Check if the output makes sense.
 - Debug any errors.

### Example

**Question**: Which customers have rented the most films, and what are their top rented genres?

**Possible SQL Query**:

```sql
SELECT
  c.first_name,
  c.last_name,
  COUNT(r.rental_id) AS total_rentals,
  cat.name AS category,
  COUNT(f.film_id) AS genre_count
FROM
  customer c
  JOIN rental r ON c.customer_id = r.customer_id
  JOIN inventory i ON r.inventory_id = i.inventory_id
  JOIN film f ON i.film_id = f.film_id
  JOIN film_category fc ON f.film_id = fc.film_id
  JOIN category cat ON fc.category_id = cat.category_id
GROUP BY
  c.customer_id,
  cat.category_id
ORDER BY
  total_rentals DESC,
  genre_count DESC;
```
## Tips for Success
Be Specific with Prompts: The more detailed your prompt, the better the output.
Iterate as Needed: Don't hesitate to refine your prompts for better questions.
Understand the Schema: Knowing table relationships is crucial for writing complex queries.
Practice Regularly: The more you practice, the more comfortable you'll become with SQL and AI tools.

## Conclusion
By using ChatGPT to generate business questions, you're combining AI tools with your SQL skills to deepen your understanding of data analysis. This exercise not only enhances your technical abilities but also prepares you for real-world scenarios where asking the right questions is just as important as finding the answers.
