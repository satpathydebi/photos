const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongodb = require('mongodb');

const app = express();

app.use(cors());
app.use(bodyParser.json());

const mongoClient = mongodb.MongoClient;
const mongoUrl = 'mongodb://localhost:27017';
const dbName = 'todo-app';

mongoClient.connect(mongoUrl, { useNewUrlParser: true, useUnifiedTopology: true }, (err, client) => {
  if (err) {
    console.error(err);
    return;
  }

  const db = client.db(dbName);
  const todosCollection = db.collection('todos');

  app.get('/todos', async (req, res) => {
    const todos = await todosCollection.find().toArray();
    res.json(todos);
  });

  app.post('/todos', async (req, res) => {
    const { text } = req.body;
    const todo = { text, completed: false };
    const result = await todosCollection.insertOne(todo);
    res.json(result.ops[0]);
  });

  app.listen(8080, () => {
    console.log('Server is running on http://localhost:8080');
  });
});
