fetch('/config/')
    .then(function (result) {return result.json()})
    .then(function (data) {
        const stripe = Stripe(data.publicKey)
        let btn = document.querySelector('.btn')
        if (btn !== null) {
            btn.addEventListener('click', function () {
                fetch('/buy/1/')
                    .then(function (result) {
                        return result.json()
                    })
                    .then(function (data) {
                        console.log(data);
                        return stripe.redirectToCheckout({sessionId: data.sessionId})
                    })
                    .then(function (res) {
                        console.log(res)
                    })
            })
        }
    })


