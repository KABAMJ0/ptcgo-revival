from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29c58481-ed25-5cb7-94b2-5448e9c115d4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacianex.Name",
    display_name="Zacian ex",
    searchable_by=["Zacian ex", "Basic", "ex", "Zacianex"],
    subtypes=["Basic", "ex"],
    collector_number=198,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Attack(
            title="Steel Armament",
            game_text="Search your deck for a Basic Metal Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Slashing Strike.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)