from space_crew import CrewMember, Rank


sarah_connor = CrewMember(
    member_id="sarah1",
    name="Sarah Connor",
    rank=Rank.commander,
    age="35",
    specialization="Mission Command",
    years_experience="15",
    is_active=True,
)


john_smith = CrewMember(
    member_id="john2",
    name="John Smith",
    rank=Rank.lieutenant,
    age="28",
    specialization="Navigation",
    years_experience="10",
    is_active=True,
)


alice_johnson = CrewMember(
    member_id="alice3",
    name="Alice Johnson",
    rank=Rank.officer,
    age="24",
    specialization="Engineering",
    years_experience="5",
    is_active=True,
)
