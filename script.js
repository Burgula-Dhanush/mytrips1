function expandToFullScreen() {
    window.open('add_review.html', '_blank', 'fullscreen=yes');
}

function redirectToReviewPage(reviewPage, destination, review, rating) {
    // Construct the URL with query parameters
    var url = reviewPage + '?destination=' + encodeURIComponent(destination) + '&review=' + encodeURIComponent(review) + '&rating=' + encodeURIComponent(rating);
    // Redirect to the constructed URL
    window.location.href = url;
  }