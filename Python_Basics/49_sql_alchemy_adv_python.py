from sqlalchemy import String, Integer, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, relationship

# DEFINING THE SCHEMA
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(30), nullable= False)
    user_email: Mapped[str] = mapped_column(unique=True, nullable=False)
    user_comments: Mapped[list['Comments']] = relationship(back_populates='User')


    def __repr__(self) -> str:
        return f'User_Details = {User.user_id} -> {User.user_name} with email {User.user_email}'


class Comments(Base):
    __tablename__ = "Comments"

    comment_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    comment_user_id: Mapped[int] = mapped_column(ForeignKey('Users.user_id'),nullable=False)
    comment_text: Mapped[str] = mapped_column(String(100), nullable= False)
    commnter_user: Mapped['User'] = relationship(back_populates='Comments')

    def __repr__(self) -> str:
        return f'Comment_Details = {Comments.comment_id, Comments.commnter_user, Comments.comment_text}'


# CREATING A ENGINE
engine = create_engine("sqlite:///Python_Basics/49.1_practice_db", echo=True)
SessionLocal = sessionmaker()


# STUFF HAPPENS HERE...

Base.metadata.create_all(bind=engine)