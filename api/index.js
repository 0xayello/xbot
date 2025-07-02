const Parser = require('rss-parser');

module.exports = async (req, res) => {
  const parser = new Parser();
  const feed = await parser.parseURL('https://www.bomdigma.com.br/feed');
  const latest = feed.items[0];

  res.status(200).json({
    title: latest.title,
    summary: latest.contentSnippet,
    link: latest.link
  });
};
