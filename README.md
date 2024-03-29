# old-town-jewels
# About
Old Town Jewels is an online jewellery store built using the Django web framework. It was developed as a part of a Fullstack course with Code Institute.

The store offers a wide variety of beautiful and unique jewellery pieces, including rings, earrings, necklaces, and more. Customers can browse the store's inventory, add items to their cart, and complete their purchase securely through the website.

Old Town Jewels is designed to be user-friendly and easy to navigate. The store features a clean and modern design, with high-quality product photos and detailed product descriptions to help customers make informed purchasing decisions.

Whether you're looking for a special piece of jewellery for yourself or a gift for someone else, Old Town Jewels has something for everyone. We hope you enjoy shopping with us!

# Table of Contents

[User Experience](#user-experience)

- [Strategy](#strategy)

- [User Stories](#user-stories)

- [Scope](#scope)

- [Structure](#structure)
    - [Wireframes](#wireframes)

[Marketing Strategies](#marketing-strategies)

[Features](#features)

[Features to be Implemented](#features-to-be-implemented)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Validator Testing](#validator-testing)

[Responsive Testing](#responsive-testing)

[Bugs Found](#bugs-found)

[User Feedback](#user-feedback)

[Search Engine Optimisation (SEO)](#search-engine-optimisation-seo)

[Deployment](#deployment)

[Credit](#credit)

[Acknowledgments](#Acknowledgments)


# User experience

At Old Town Jewels, our goal is to provide an enjoyable and seamless shopping experience for both our customers and the store owner. To achieve this, we have implemented the following strategies:

# Strategy
## For Customer
1. Easy navigation: We have designed the store's layout and menu to be intuitive and easy to use, so customers can easily find  what they are looking for.

2. Clear product descriptions: We have provided detailed descriptions of each product, including information on materials, sizing, and care instructions. This helps customers make informed purchasing decisions.

3. Secure checkout: We have implemented secure payment methods and encrypted data transmission to protect our customers' personal and financial information.

## For Owner 
1. Easy inventory management: We have provided tools for the owner to easily add, update, and delete products from the store's inventory.

2. Detailed sales reports: The owner can access reports on sales data, including total revenue.

By following these strategies, we hope to create a positive user experience for our customers and encourage them to shop with us again in the future.

# User Stories
As the superuser of Old Town Jewels, I want to be able to:

1. **Add and manage products**: I want to be able to easily add new products to the store's inventory, as well as update and delete existing products.

2. **View and analyze sales data**: I want to be able to access detailed reports on sales data, including total revenue and popular products.

3. **Manage user accounts**: I want to be able to add, update, and delete user accounts, including customer and employee accounts.

4. **Manage orders**: I want to be able to view and manage orders, including marking orders as shipped and canceling orders if necessary.

5. **Create and manage coupons**: I want to be able to create and manage coupons, including setting expiration dates and usage limits, and track their usage.

By being able to perform these tasks, I can effectively manage and maintain the Old Town Jewels store.

As a shopper at Old Town Jewels, I want to be able to:

1. **Easily browse and search for products**: I want to be able to easily browse through the store's inventory and use section filters to find specific products.

2. **View detailed product information**: I want to be able to see photos of the products and read detailed descriptions, including information on materials, sizing, and care instructions.

3. **Add items to my cart and complete my purchase**: I want to be able to easily add items to my cart and complete my purchase securely through the website.

4. **Apply coupons to my order**: I want to be able to enter a coupon code at checkout and have the discount applied to my order.

By being able to perform these tasks, I can easily shop and make purchases at Old Town Jewels.

# Scope

# User Story 1: Easily browse and search for products
Customers can easily browse through the store's inventory and use search filters to find specific products.

# User Story 2: View detailed product information
Customers can view high-quality photos of the products and read detailed descriptions, including information on materials, sizing, and care instructions.

# User Story 3: Add items to my cart and complete my purchase
Customers can easily add items to their cart and complete their purchase securely through the website.

# User Story 4: Apply coupons to my order
Customers have the option to apply coupons to their orders at checkout by entering a coupon code.

# Superuser

# User Story 5: Add and manage products
As the superuser of the store, I can easily add and manage products.

# User Story 6: View and analyze sales data
As the superuser of the store, I can view and analyze sales data, including total revenue and popular products.

# User Story 7: Manage user accounts
As the superuser of the store, I can manage user accounts, including customer and employee accounts. 

# User Story 8: View and analyze sales data
As the superuser of the store, I can access detailed reports on sales data, including total revenue and popular products.

# User Story 9: Manage user accounts
As the superuser of the store, I can add, update, and delete user accounts, .

# User Story 10: Manage orders
As the superuser of the store, I can view and manage orders, including marking orders as shipped and canceling orders if necessary.

# User Story 11: Create and manage coupons
As the superuser of the store, I can create and manage coupons, including setting expiration dates and usage limits, and track their usage.

By providing these features, Old Town Jewels aims to create a positive shopping experience for both customers and the store owner.


# Structure

This project is structured with a homepage with the website's logo and a message that greets the user with a clear navigation bar at the top of the page where the user can login or sign up. Old Town Jewels shop enables clients to browse products, add them to the cart, apply discount codes, go through the checkout process, pay with a credit card, and obtain an invoice.

**The website is made of the following apps**:

1. MyShop
2. Accounts
3. Cart
4. Coupons
5. Login
6. Orders
7. Payment
8. Shop

# Unresolved Bugs

1. **Deployment to Heroku failed**: 
The project could not be deployed to Heroku due to an error with the database configuration.

2. **Images not showing**: 
Some images were not being displayed correctly on the website.

3. **Payment processed page not accessible**: 
The payment processed page was not accessible and returned a "server could not be reached" error.

# What I have tried to resolve them

To resolve the bugs identified in the project, the following actions were taken:

1.  - Check the logs for Django application and web server for any error messages that might provide more information about the problem.
    - Make sure that all dependencies and libraries required by your application are installed and up-to-date.
    - Incorrect configuration: Check Heroku app's configuration to make sure it is set up correctly. Procfile and any environment variables that are required for your application to run.

2. **Images not showing**: 
I checked the file paths for the images and made sure that the images were located in the correct directory. I also checked the file permissions to make sure the images were readable by the web server.

3. **Payment processed page not accessible** 
    -  Incorrect URL: Made sure that the URL being used to access the payment processed page is correct. Double-check the spelling and formatting of the URL to ensure that it is correct.

    - Network issues: If the payment processed page is being accessed from a different server or network, there could be network issues that are preventing the page from being reached. Checked with service provider to see if there are any issues that need to be addressed.

    - Application errors: If the payment processed page is not working properly, there could be errors in the application that are preventing the page from being accessed. Reviewed the logs for my application and check for any error messages that might provide more information about the issue.

    - Server issues: If the payment processed page is hosted on a server, there could be issues with the server itself that are preventing the page from being accessed. In this case, you may need to check with your hosting provider or server administrator to see if there are any issues that need to be addressed.

# Acknowledgments

I have done this project using the book "DJANGO 3 KROZ PRIMERE"
I heavily relied on the book.


# Project Status
Unfortunately, I was not able to complete this project due to time constraints. I apologize for any inconvenience this may cause.
# Project Challenges
While working on this project, I encountered a number of challenges that made it difficult to complete. These challenges included:

1. Time constraints: The project was very time-consuming and I was not able to dedicate as much time to it as I would have liked.
2. Technical difficulties: I encountered several technical issues that made it difficult to implement certain features of the project.
3. Lack of experience: As a beginner developer, I found some aspects of the project to be beyond my current skill level.


Despite these challenges, I did my best to work through them and make progress on the project. However, in the end, I was not able to complete it as planned.











