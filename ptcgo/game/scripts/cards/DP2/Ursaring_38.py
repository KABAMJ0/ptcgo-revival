from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="118015fa-4531-5e2f-81a7-f98a5719f231",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="DP2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Bad Temper",
            game_text="The Defending Pok\u00e9mon is now Confused. During your opponent's next turn, that Pok\u00e9mon's attacks do 60 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Defensive Claw",
            game_text="If Teddiursa is on your Bench, this attack does 60 damage plus 20 more damage. If Teddiursa is on your Bench and has any damage counters on it, this attack does 60 damage plus 40 more damage and remove all damage counters from that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)