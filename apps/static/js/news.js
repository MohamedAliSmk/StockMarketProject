$(document).ready(function() {
    var stocks = ['AAPL', 'MSFT', 'GOOG'];
    var url = 'https://api.worldtradingdata.com/api/v1/stock_news?symbol=' + stocks.join() + '&sort=newest&limit=5&api_token=MY_WORLD_TRADING_DATA_KEY';
    
    $.getJSON(url, function(data) {
        var newsContainer = $('#news-container');
        
        $.each(data.data, function(index, news) {
            var stockHeading = $('<h2>').text(news.symbol);
            var newsList = $('<ul>');
            
            $.each(news.news, function(index, article) {
                var articleLink = $('<a>').attr('href', article.url).text(article.title);
                var articleSource = $('<span>').text(' (' + article.source + ')');
                var articleItem = $('<li>').append(articleLink, articleSource);
                
                newsList.append(articleItem);
            });
            
            newsContainer.append(stockHeading, newsList);
        });
    });
});
