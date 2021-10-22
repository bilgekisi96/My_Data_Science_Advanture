select *
from tblFilm
select * from tblDirector where DirectorID = 4
select * from tblDirector as f
         inner join tblFilm as d
		 on f.DirectorID=d.FilmDirectorID

select * from tblFilm 
          where FilmBoxOfficeDollars is NULL
        

         