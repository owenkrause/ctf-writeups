# Challenge Info
Mini-ject

Category: web

Description: I made a private notes app and decided to release it out into the world. It's my first big project so hopefully nothing goes wrong!

Flag 1: 200 points

Access: http://mini-ject.ctf-league.osusec.org/

## Observations

The website contains a list of blog posts and an input labeled filter.
One of the posts contains a schema of an SQL table, (note the attribute private).
The filter hides posts where the text attribute does not contain the filter query.
```
create table posts (
  postid int,
  private bool,
  text varchar(1000),
  author varchar(255)
);
```

## Approach

The private attribute implies that there are hidden posts to be uncovered. The filter input must be the entry point to an SQL injection. If there are private blog posts, the SQL select statement must include a part where private is false. We can start stringing the query together: ``select * from posts where text like "%filter%" AND private = false``.
This query is susceptible to an injection. Consider if the filter is set to "OR" -> ``select * from posts where text like "%"OR"%" AND private = false``. This gives us two operands: ``where text like "%"`` OR ``"%" AND private = false``. The first part will always evaluate to true since "%" is just a wildcard. Thus, it doesn't matter whether private = false. 
Note: SQL interprets AND as higher precedence than OR so ``condition1 OR condition2 AND condition3`` is equivalent to ``condition1 OR (condition2 AND condition3)``. This is why our injection works. 
