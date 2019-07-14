const NewsAPI = require("newsapi");
const newsapi = new NewsAPI("5bee2e586cb545648223aa8c7c92b69b");
// To query /v2/everything
// You must include at least one q, source, or domain
newsapi.v2
  .everything({
    q: "oi%20oi",
    sources: "globo",
    domains: "globo.com",
    language: "pt",
    sortBy: "relevancy",
    page: 1
  })
  .then(response => {
    console.log(response);
    /*
      {
        status: "ok",
        articles: [...]
      }
    */
  });
