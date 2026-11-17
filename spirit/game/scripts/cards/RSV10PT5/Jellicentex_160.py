from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f8d5347-35f0-570e-b62c-5f0d8fd3b41f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicentex.Name",
    display_name="Jellicent ex",
    searchable_by=["Jellicent ex", "Stage 1", "ex", "Jellicentex"],
    subtypes=["Stage 1", "ex"],
    collector_number=160,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Ability(
            title="Oceanic Curse",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Item cards or Pok\u00e9mon Tool cards from their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Press",
            game_text="If this Pok\u00e9mon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)