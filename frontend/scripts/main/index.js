// Homepage for KnowledgeBytes

$(function () {
    var result = {}, summary;

    $(".search-btn").on('click', function () {
        ajaxReq( "query=" + $(".search-txt").val() ).done(function (data) {
            result = data;
            summary = scrapeResults(result);
            $(".search-box").html(summary);
            $(".search-box").css("height", "140px");
        })
    });
});

function ajaxReq(data) {

    return $.ajax({
        url: "http://127.0.0.1:8000/",
        contentType: 'application/json',
        dataType: "json",
        type: "GET",
        data: data,
    });
}

function scrapeResults(scrape) {

    var scraped = scrape;
    
    var results = "<p style = \"" + "text-align: center;"+"\">"  + scraped[0]["name"] + "</p>";
    results += "<p style = \"" + "text-align: center;" + "\">" + "it costs about " + scraped[1]["price"] + " per year to attend. " + "</p>";

    for (var i = 2; i < 6; i++) 
    {
        results += "<div>";
        results += "<a href=\"" + scraped[i]["url"] + "\"target = \"" + "_blank" + "\">" + scraped[i]["url"] + "</a>";
        results += "</div>";
    }
    
    return results;
}

