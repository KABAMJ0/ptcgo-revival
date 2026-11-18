from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7616288-e34a-59d2-89d4-9001f189f2e9",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victiniex.Name",
    display_name="Victini ex",
    searchable_by=["Victini ex", "Basic", "ex", "Victiniex"],
    subtypes=["Basic", "ex"],
    collector_number=142,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Victory Flame",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)