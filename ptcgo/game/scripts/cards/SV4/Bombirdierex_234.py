from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf71be2d-9bb5-526e-a83c-f9aabd4e17ec",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdierex.Name",
    display_name="Bombirdier ex",
    searchable_by=["Bombirdier ex", "Basic", "ex", "Bombirdierex"],
    subtypes=["Basic", "ex"],
    collector_number=234,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=962,
    abilities=[
        Attack(
            title="Fast Carrier",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for up to 3 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Shadowy Wind",
            game_text="You may put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)