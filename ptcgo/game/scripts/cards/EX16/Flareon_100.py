from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf063794-9356-5643-839d-7d071217dd36",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon ★",
    searchable_by=["Flareon \u2605", "Basic", "Star", "Flareon"],
    subtypes=["Basic", "Star"],
    collector_number=100,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Ability(
            title="Crimson Ray",
            game_text="Once during your turn, when you put Flareon Star from your hand onto your Bench, you may use this power. Each Active Pok\u00e9mon (both yours and your opponent's) is now Burned.",
            effect=unimplemented,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard a Fire Energy attached to Flareon Star.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)