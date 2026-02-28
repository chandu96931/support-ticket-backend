const express = require('express');
const cors = require('cors');
const jwt = require('jsonwebtoken');

const app = express();
app.use(cors()); // allow React or Postman requests
app.use(express.json()); // parse JSON bodies

// Token endpoint: accepts any username/password
app.post('/api/token', (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: 'Username and password required' });
  }

  // Generate JWT token dynamically
  const token = jwt.sign({ username }, 'SECRET_KEY', { expiresIn: '1h' });

  console.log(`Token generated for: ${username}`);
  return res.json({ token });
});

// Test endpoint to make sure server is running
app.get('/api/health', (req, res) => {
  res.send('Server is running!');
});

// Start server
app.listen(5000, () => console.log('Backend running on http://localhost:5000'));