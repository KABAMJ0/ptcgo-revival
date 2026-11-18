from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31956e9d-b098-5538-9019-60e0dedecd1a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name",
    display_name="Groudon-EX",
    searchable_by=["Groudon-EX", "Basic", "EX", "GroudonEX"],
    subtypes=["Basic", "EX"],
    collector_number=42,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Rip Claw",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Massive Rend",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)