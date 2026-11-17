from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc23e398-1504-59b7-8af6-d7a5416b0769",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaExcadrillex.Name",
    display_name="Mega Excadrill ex",
    searchable_by=["Mega Excadrill ex", "Stage 1", "MEGA", "ex", "MegaExcadrillex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=103,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Undermine",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.METAL: 2},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Maximum Drilling",
            game_text="If this Pok\u00e9mon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 130 more damage.",
            cost={PokemonTypes.METAL: 3},
            damage=200,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)