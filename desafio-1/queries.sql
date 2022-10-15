
select r.prof_id as professorId, count(r.student_id) as totalAlunos, p.teachingability as capEnsino from ra r
inner join prof p on p.prof_id = r.prof_id
group by r.prof_id;

select ra.prof_id  as professorId, count(distinct re.course_id) as totalCursos from ra 
inner join registration re on re.student_id = ra.student_id
group by  ra.prof_id;

