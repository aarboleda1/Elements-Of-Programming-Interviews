"""
LinkedIn is a social network for professionals. The main goal of the site is to
enable its members to connect with people they know and trust professionally,
as well as to find new opportunities to grow their careers.

A LinkedIn member’s profile page, which emphasizes their skills, employment
history, and education, has professional network news feeds with customizable
modules.

LinkedIn is very similar to Facebook in terms of its layout and design. These
features are more specialized because they cater to professionals, but in
general, if you know how to use Facebook or any other similar social network,
LinkedIn is somewhat comparable.



Use Cases:
- User should be able to search for a person
- User should be be ablet to connect with a professional
- User
- Company
- follow a company


https://sketchboard.me/pBFmSVVEHBiE#/
"""
class LookupService:
    pass

class UserGraphService:
    def shortest_path(source_id, target_id):
        person = self.lookup_service(source)
        queue = deque([person])
        seen = set()
        while queue:
            node = queue.popleft()
            if node.connections:
                for connection in node.connections:
                    if connection.id not in seen:
                        queue.append(connection)
        return None
