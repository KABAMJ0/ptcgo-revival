from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2bfd9a67-c56b-5aa0-a4ce-4a51f4dc84a0",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianArcanine.Name",
    display_name="Hisuian Arcanine",
    searchable_by=["Hisuian Arcanine", "Stage 1", "HisuianArcanine"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Proud Fangs",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 90 more damage.",
            cost={},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)