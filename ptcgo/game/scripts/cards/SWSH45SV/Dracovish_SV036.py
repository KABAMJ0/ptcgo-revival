from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fc1fe761-8b30-5ea5-8cdc-b77f31db8197",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dracovish.Name",
    display_name="Dracovish",
    searchable_by=["Dracovish", "Stage 1", "Dracovish"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=882,
    abilities=[
        Ability(
            title="Primal Law",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Pok\u00e9mon from their hand to evolve their Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)