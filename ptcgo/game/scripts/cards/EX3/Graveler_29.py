from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="71f9ed92-b48b-56f7-bea5-5ea0786f2eba",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1", "Graveler"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Grind",
            game_text="Does 10 damage times the amount of Energy attached to Graveler.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Big Explosion",
            game_text="Does 80 damage to each Active Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)