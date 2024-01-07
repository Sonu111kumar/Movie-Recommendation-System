# Movie-Recommendation-System using Machine Learning.
# ABSTRACT 
 Movie recommendation systems have transformed the way we explore and enjoy films in the digital age. This research paper provides an extensive analysis of movie recommendation systems, delving into their evolution, algorithmic techniques, data sources, challenges, ethical dimensions, applications in the film industry, and the promising future developments.
  It highlights the filtering criteria in the recommender systems, algorithms implemented in movie recommender systems, the performance measurement criteria, the challenges in implementation, and recommendations for future research. Some of the most popular machine learning algorithms used in movie recommender systems such as K-means clustering, principal component analysis, and self-organizing maps with principal component analysis, cosine similarity.  This paper aims to offer a comprehensive understanding of the complexity and significance of movie recommendation systems. 
Keyword: content-based-filtering, cosine similarity, Movie Recommendation.


#                                1.	INTRODUCTION
 In an era characterized by an overwhelming abundance of information and choices, recommendation systems have emerged as indispensable tools to assist individuals in making decisions, whether it be selecting a movie to watch, a book to read, or a product to purchase. The exponential growth of digital content and e-commerce platforms has led to a demand for personalized recommendations that cater to users' specific preferences, thus enhancing their overall experience. Recommendation systems, also known as recommender systems, have become ubiquitous in our daily lives, shaping the way we interact with content and make choices. Recommender Systems produce recommendations, which the user can choose to accept or reject. The user can also give implicit or explicit input at any time, either right away or later on. The recommender database has the ability to retain user actions and comments, which can then be utilized to generate new recommendations during further user-system interactions. Some of the largest e-commerce companies (such as Amazon.com, snapdeal.com), as well as the online movie rental service Netflix, have made these recommender systems a prominent feature of their websites due to their economic potential
#                                  2. HISTORICAL EVOLUTION 
The roots of recommendation systems trace back to early collaborative filtering techniques, such as J. L. Herlocker's "MovieLens" system. The Netflix Prize in 2006 marked a significant milestone in the field by promoting collaborative filtering algorithms. Since then, recommendation systems have evolved from rule-based methods to machine learning and deep learning approaches. 
 
 
  #                   3. TYPES OF  RECOMMENDATION SYSTEMS 

Movie recommendation systems can be categorized based on their underlying techniques: 
#                        3.1. Collaborative Filtering 
Collaborative filtering encompasses several techniques: 
•	User-based Collaborative Filtering:  Recommending movies based on the preferences of users with similar viewing histories. 
•	Item-based Collaborative Filtering:  Suggesting movies similar to those previously liked by the user. 
•	Matrix Factorization: Decomposing the user-movie interaction matrix to capture latent factors. 

#                        1.2.	Content-Based Filtering 
Content-based filtering is a recommendation system technique used to suggest items to users based on the properties and characteristics of the items themselves, as well as the user's past behavior or preferences. This approach is commonly used in various recommendation systems, including those that recommend movies, books, products, and more.

#                        1.3.	Hybrid Recommendation Systems  
A hybrid recommendation system is a type of recommendation system that combines two or more different recommendation approaches to provide more accurate and diverse recommendations. These approaches are typically collaborative filtering, content-based filtering, and sometimes other techniques, such as knowledge-based or context-aware recommendation methods. The goal of a hybrid recommendation system is to leverage the strengths of each approach while mitigating their individual weaknesses.




#                         4.	RESEARCH METHODOLOGY

#                         4.1	 Similarity Technique
      Cosine similarity is a metric, helpful in determining, how similar the data objects are irrespective of their size. We can measure the similarity between two sentences in Python using Cosine Similarity. In cosine similarity, data objects in a dataset are treated as a vector. The formula to find the cosine similarity between two vectors is –

 (x, y) = x . y / ||x||   ||y||

           where
•	x . y = product (dot) of the vectors ‘x’ and ‘y’.
•	||x|| and ||y|| = length (magnitude) of the two vectors ‘x’ and ‘y’.
•	||x||   ||y|| = regular product of the two vectors ‘x’ and ‘y’.

•	The cosine similarity between two vectors is measured in ‘θ’.
•	If θ = 0°, the ‘x’ and ‘y’ vectors overlap, thus proving they are similar.
•	If θ = 90°, the ‘x’ and ‘y’ vectors are dissimilar.

 
Cosine Similarity between two vectors
#                              4.2 Movie Recommendation System is divided into 4 modules:

1.	Dataset - Provide dataset (By this, we mean that the collected data should be uniform and understandable for a machine that doesn't see data in the same way that people do.)
Analytics for every dataset (i.e movies dataset, credits dataset) has helped to understand user-item interactions for movie recommendation.
2.	Pre-processing – A real-world data generally contains noises, missing values, and maybe in a format which cannot be directly used for machine learning models. Data pre cleaning the data and making it suitable for a machine learning model which also increases the accuracy and efficiency of a machine learning model.

	Null values treatment- We served with two dataset (i.e  movies dataset, credits dataset). We got null values in movies dataset (features are budget, homepage, id genres, overview, keywords, title, revenue). Credits dataset doesn’t contain any null values.

	Dropping and replacing data- Proceeding with data cleaning and feature selection is a crucial steps – we dropped feature like budget, homepage, revenue. Replaced feature with lowercase and ‘-‘ to built a space between words. Some of the null values were present in feature data, we replaced with mean of that particular feature. Only considering age between 5 90 we took users data to analysis and perform recommendation on it.       





	

	


                

	





3.	Training and Testing-Training data is the data you use to train an algorithm or machine learning model to predict the outcome you design your model to predict with help of test data test your model. you can evaluate the performance and progress.

4.	Content based filtering - Content-based filtering is a recommendation system technique used to suggest items to users based on the properties and characteristics of the items themselves, as well as the user's past behavior or preferences. This approach is commonly used in various recommendation systems, including those that recommend movies, books, products, and more.

  #                    5.  APPLICATIONS IN THE FILM INDUSTRY 
 
Movie recommendation systems have extensive applications within the film industry, including: 
Streaming Platforms:  Enhancing user experience on platforms like Netflix, Amazon Prime Video, and Hulu. 
Movie Theaters: Suggesting films for users to watch in theaters. 
Film Studios: Utilizing recommendation systems for marketing and distribution strategies. 
Film Festivals: Recommending movies for festival attendees to maximize their experience. 
 
 
 #                                        6.  FUTURE DIRECTIONS 
 
The future of movie recommendation systems holds the promise of exciting developments: 
Advanced Deep Learning Models:  Leveraging deep learning to better understand and predict user preferences. 
Interpretable Models:  Developing recommendation systems that are more transparent and user-friendly. 
Enhanced Privacy-Preserving Techniques:  Innovations in preserving user privacy while delivering personalized recommendations. 
Ethical and Regulatory Frameworks:  Establishing guidelines and regulations for responsible movie recommendation system design. 
 
#                                               7. CONCLUSION 
 
Movie recommendation systems have revolutionized the film industry and how audiences discover and engage with movies. While these systems offer numerous benefits, it is imperative to address ethical concerns related to user privacy and fairness. The future of movie recommendation systems holds the promise of more advanced, interpretable, and ethical models that will continue to shape the entertainment industry. 
 
  
 
 
  
 
 
 
 
 
 
  
 

