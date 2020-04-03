# micro-service http

Ce micro-service a pour but de récupérer les données depuis la base mongo,
après que le parser ai attribué les sentiments de chaque item.
Si lors de l'appel les données sont deja existante il travaille avec ceux en
base, sinon il appel l'api du crawler par sujet.