# Supermarket Products API: [Deploy](https://supermarket-products-api.up.railway.app/)

### English

This API was created with **FastAPI** and stores **AI-generated** supermarkets, products, brands and categories (which may have real names or not, and unrelated or not brands/categories/products) in a PostgreSQL database for study purposes.<br>
Product prices are updated daily at `*08:00 (8am) SÃO PAULO TIMEZONE*`.<br>
You "cannot" (and don't need to) `CREATE` and `DELETE` items because, as mentioned, this API is read-only. It's designed for use in the development of study/practice applications (such as simulations of supermarkets, grocery stores, e-commerce, etc.) or for data-related studies.<br>

---

### Portuguese

Esta API foi criada com **FastAPI** e armazena supermercados, produtos, marcas e categorias **gerados por IA** (que podem ter nomes reais ou não, e marcas/categorias/produtos relacionados ou não) em um banco de dados **PostgreSQL** para fins de estudo.<br>
Os preços dos produtos são atualizados diariamente às *08:00 (8am) no fuso horário de SÃO PAULO*.<br>
Você "não pode" (e não precisa) criar ou excluir itens porque, como mencionado, esta API é somente para leitura. Foi pensada para uso no desenvolvimento de apps de estudo/prática (como simulações de supermercados, lojas de conveniência, e-commerce, etc.) ou para estudos relacionados a dados.<br>

---

#### Endpoints:
- **infos**: `/api`
- **for devs**: `/api/dev`
- **supermarkets**: `/api/supermarkets`
- **supermarkets by id**: `/api/supermarkets/id(integer)`
- **brands**: `/api/brands`
- **brands by id**: `/api/brands/id(integer)`
- **categories**: `/api/categories`
- **categories by id**: `/api/categories/id(integer)`
- **products**: `/api/products`
- **products by id**: `/api/products/id(integer)`
