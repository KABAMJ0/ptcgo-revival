from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="118bdc78-8b23-5c29-be89-74f47cba4ee5",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="EX9",
    rarity=Rarities.RareSecret,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=83,
    abilities=[
        Attack(
            title="Spearhead",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Nosedive",
            game_text="Farfetch'd does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)